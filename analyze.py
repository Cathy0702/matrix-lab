#!/usr/bin/env python3
"""
Analyze RESTler network log files to verify that custom checkers
(ForgetJoinChecker, RedactContentChecker, LeaveSendChecker) fire
requests when they should.

Supports split log files: pass multiple files in order and they are
parsed as one continuous stream.  Incomplete blocks at the very start
and very end of the combined stream are silently dropped.

Usage:
    python3 analyze_checkers.py file1.txt [file2.txt ...]

Logic:
  1. Stream through all files in order, building "sequence blocks".
     A block = the Sending/Received pairs (sequence replay) followed
     by the full checker run (ForgetJoinChecker … InvalidValueChecker).
  2. A block is finalised when InvalidValueChecker kicks out.
  3. For each complete block, determine the LAST request+response sent
     before the checkers and whether it got a 2xx response ("valid").
  4. Check whether each of the three checkers fired (sent requests).
  5. Compare expected vs. actual.

Checker rules:
  - ForgetJoinChecker:      should fire if last request is a valid "forget"
  - RedactContentChecker:   should fire if last request is a valid "redact"
  - LeaveSendChecker:       should fire if last request is a valid "leave"
"""

import re
import sys
from dataclasses import dataclass, field
from enum import Enum, auto


# ---------------------------------------------------------------------------
# Patterns (compiled once)
# ---------------------------------------------------------------------------

RE_CHECKER_IN  = re.compile(r'Checker:\s+(\w+)\s+kicks\s+in')
RE_CHECKER_OUT = re.compile(r'Checker:\s+(\w+)\s+kicks\s+out')
RE_SENDING     = re.compile(r"Sending:\s+'(GET|PUT|POST|DELETE|PATCH)\s+(/[^\s]+)\s+HTTP")
RE_RECEIVED    = re.compile(r"Received:\s+'HTTP/1\.\d\s+(\d{3})")
RE_GENERATION  = re.compile(r'Generation-\d+:\s+Rendering\s+Sequence-(\d+)')


# ---------------------------------------------------------------------------
# Endpoint classifiers
# ---------------------------------------------------------------------------

def is_forget(path: str) -> bool:
    return path.rstrip('/').endswith('/forget')

def is_redact(path: str) -> bool:
    return '/redact/' in path

def is_leave(path: str) -> bool:
    return path.rstrip('/').endswith('/leave')


# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------

class Verdict(Enum):
    PASS         = auto()
    FAIL_NO_FIRE = auto()   # should have fired but didn't
    FAIL_EXTRA   = auto()   # fired but shouldn't have


@dataclass
class CheckerResult:
    name: str
    fired: bool = False


@dataclass
class SequenceBlock:
    """One complete sequence execution + checker run."""
    seq_id: str = ""
    location: str = ""          # "filename:line" where the block's traffic starts

    last_method: str = ""       # last request before checkers
    last_path: str = ""
    last_status: int = 0        # 0 = no response parsed

    checker_results: dict = field(default_factory=dict)


@dataclass
class CheckVerdict:
    checker: str
    expected_fire: bool
    actual_fire: bool
    verdict: Verdict
    seq_id: str
    location: str
    last_request: str
    last_status: int


# ---------------------------------------------------------------------------
# Multi-file line iterator
# ---------------------------------------------------------------------------

def iter_lines(filepaths: list[str]):
    """Yield (filename, line_number, line_text) across all files in order."""
    for fp in filepaths:
        with open(fp, 'r', errors='replace') as fh:
            for line_no, raw in enumerate(fh, start=1):
                yield fp, line_no, raw.rstrip('\n')


# ---------------------------------------------------------------------------
# Parser
# ---------------------------------------------------------------------------

CHECKERS_WE_CARE = frozenset({"ForgetJoinChecker", "RedactContentChecker", "LeaveSendChecker"})


def parse_logs(filepaths: list[str]) -> list[SequenceBlock]:
    """
    Single-pass parse across all files treated as one continuous log.
    Only complete blocks (ending with InvalidValueChecker kicks out)
    are returned.
    """
    blocks: list[SequenceBlock] = []
    current: SequenceBlock | None = None
    seq_counter = 0

    # Track last Sending/Received before the first checker in a block
    last_method    = ""
    last_path      = ""
    last_status    = 0
    pending_method = ""
    pending_path   = ""

    in_checker: str | None = None
    checker_saw_send = False

    for filename, line_no, line in iter_lines(filepaths):

        # --- Generation header (sequence definition) ------------------------
        m = RE_GENERATION.search(line)
        if m:
            seq_counter += 1
            continue

        # --- Sending line ---------------------------------------------------
        m = RE_SENDING.search(line)
        if m:
            method, path = m.group(1), m.group(2)

            if in_checker is not None:
                checker_saw_send = True
            else:
                if current is None:
                    current = SequenceBlock(
                        seq_id=str(seq_counter),
                        location=f"{filename}:{line_no}",
                    )
                pending_method = method
                pending_path   = path
            continue

        # --- Received line --------------------------------------------------
        m = RE_RECEIVED.search(line)
        if m:
            status = int(m.group(1))
            if in_checker is None:
                last_method = pending_method
                last_path   = pending_path
                last_status = status
            continue

        # --- Checker kicks in -----------------------------------------------
        m = RE_CHECKER_IN.search(line)
        if m:
            checker_name = m.group(1)
            in_checker = checker_name
            checker_saw_send = False

            # First checker finalises the "last request" for this block
            if current is not None and not current.last_path:
                current.last_method = last_method
                current.last_path   = last_path
                current.last_status = last_status
            continue

        # --- Checker kicks out ----------------------------------------------
        m = RE_CHECKER_OUT.search(line)
        if m:
            checker_name = m.group(1)

            if current is not None and checker_name in CHECKERS_WE_CARE:
                current.checker_results[checker_name] = CheckerResult(
                    name=checker_name,
                    fired=checker_saw_send,
                )

            # InvalidValueChecker kicks out = end of block
            if checker_name == "InvalidValueChecker":
                if current is not None:
                    blocks.append(current)
                current = None
                last_method    = ""
                last_path      = ""
                last_status    = 0
                pending_method = ""
                pending_path   = ""

            in_checker = None
            checker_saw_send = False
            continue

    # Trailing incomplete block is intentionally dropped.
    return blocks


# ---------------------------------------------------------------------------
# Analysis
# ---------------------------------------------------------------------------

def analyse(blocks: list[SequenceBlock]) -> list[CheckVerdict]:
    verdicts: list[CheckVerdict] = []

    for blk in blocks:
        valid = 200 <= blk.last_status < 300

        checks = [
            ("ForgetJoinChecker",    valid and is_forget(blk.last_path)),
            ("RedactContentChecker", valid and is_redact(blk.last_path)),
            ("LeaveSendChecker",     valid and is_leave(blk.last_path)),
        ]

        for checker_name, should_fire in checks:
            cr = blk.checker_results.get(checker_name)
            if cr is None:
                continue

            actual = cr.fired
            if should_fire == actual:
                v = Verdict.PASS
            elif should_fire and not actual:
                v = Verdict.FAIL_NO_FIRE
            else:
                v = Verdict.FAIL_EXTRA

            verdicts.append(CheckVerdict(
                checker=checker_name,
                expected_fire=should_fire,
                actual_fire=actual,
                verdict=v,
                seq_id=blk.seq_id,
                location=blk.location,
                last_request=f"{blk.last_method} {blk.last_path}",
                last_status=blk.last_status,
            ))

    return verdicts


# ---------------------------------------------------------------------------
# Reporting
# ---------------------------------------------------------------------------

def report(verdicts: list[CheckVerdict], filepaths: list[str]):
    summary: dict[str, dict[str, int]] = {}
    failures: list[CheckVerdict] = []

    for v in verdicts:
        bucket = summary.setdefault(v.checker, {"PASS": 0, "FAIL_NO_FIRE": 0, "FAIL_EXTRA": 0})
        if v.verdict == Verdict.PASS:
            bucket["PASS"] += 1
        elif v.verdict == Verdict.FAIL_NO_FIRE:
            bucket["FAIL_NO_FIRE"] += 1
            failures.append(v)
        elif v.verdict == Verdict.FAIL_EXTRA:
            bucket["FAIL_EXTRA"] += 1
            failures.append(v)

    print("=" * 80)
    print("RESTler Checker Firing Analysis Report")
    print("=" * 80)

    print(f"\nFiles analysed ({len(filepaths)}):")
    for fp in filepaths:
        print(f"  - {fp}")

    total_pass = sum(s["PASS"] for s in summary.values())
    total_fail = sum(s["FAIL_NO_FIRE"] + s["FAIL_EXTRA"] for s in summary.values())
    total = total_pass + total_fail
    print(f"\nTotal checks: {total}  |  PASS: {total_pass}  |  FAIL: {total_fail}\n")

    CHECKER_NAMES = ["ForgetJoinChecker", "RedactContentChecker", "LeaveSendChecker"]

    print("-" * 80)
    print(f"{'Checker':<30} {'PASS':>6} {'MISS':>6} {'EXTRA':>6} {'Total':>6}")
    print("-" * 80)
    for name in CHECKER_NAMES:
        s = summary.get(name, {"PASS": 0, "FAIL_NO_FIRE": 0, "FAIL_EXTRA": 0})
        t = s["PASS"] + s["FAIL_NO_FIRE"] + s["FAIL_EXTRA"]
        print(f"{name:<30} {s['PASS']:>6} {s['FAIL_NO_FIRE']:>6} {s['FAIL_EXTRA']:>6} {t:>6}")
    print("-" * 80)

    print("\n--- Should-fire vs Did-fire breakdown ---\n")
    for name in CHECKER_NAMES:
        should_fire_total = sum(1 for v in verdicts if v.checker == name and v.expected_fire)
        should_fire_did   = sum(1 for v in verdicts if v.checker == name and v.expected_fire and v.actual_fire)
        should_not_total  = sum(1 for v in verdicts if v.checker == name and not v.expected_fire)
        should_not_did    = sum(1 for v in verdicts if v.checker == name and not v.expected_fire and v.actual_fire)
        print(f"  {name}:")
        print(f"    Should fire:     {should_fire_did}/{should_fire_total} did fire")
        print(f"    Should NOT fire: {should_not_did}/{should_not_total} incorrectly fired")
        print()

    if failures:
        print("=" * 80)
        print(f"FAILURES ({len(failures)} issues)")
        print("=" * 80)
        for f in failures:
            tag = "MISS" if f.verdict == Verdict.FAIL_NO_FIRE else "EXTRA"
            print(f"\n  [{tag}] {f.checker}")
            print(f"    Block #{f.seq_id} at {f.location}")
            print(f"    Last request:  {f.last_request}  (status {f.last_status})")
            print(f"    Expected fire: {f.expected_fire}  |  Actual fire: {f.actual_fire}")
    else:
        print("\nAll checks PASSED -- every checker fired exactly when expected.")

    print()


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <logfile> [<logfile2> ...]")
        print()
        print("Pass files in chronological order.  They will be treated as")
        print("one continuous log stream.  Incomplete blocks at the start")
        print("and end are automatically dropped.")
        sys.exit(1)

    filepaths = sys.argv[1:]

    print(f"\n>>> Parsing {len(filepaths)} file(s) as a single stream ...\n")
    blocks = parse_logs(filepaths)
    print(f"    Parsed {len(blocks)} complete sequence blocks.\n")

    verdicts = analyse(blocks)
    report(verdicts, filepaths)


if __name__ == "__main__":
    main()