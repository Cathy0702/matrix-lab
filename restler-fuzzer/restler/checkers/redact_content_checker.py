"""Implements logic for specific rule: cannot access message content after redacting."""

from __future__ import print_function

import copy
import json

from checkers.checker_base import *

from engine.core.sequences import Sequence
from engine.bug_bucketing import BugBuckets


class RedactContentChecker(CheckerBase):
    def __init__(self, req_collection, fuzzing_requests):
        super(RedactContentChecker, self).__init__(req_collection, fuzzing_requests)

    def apply(self, rendered_sequence, lock):
        if not rendered_sequence.valid:
            return

        self._sequence = rendered_sequence.sequence
        self._lock = lock

        last_req = self._sequence.last_request
        endpoint = getattr(last_req, "endpoint", "") or ""
        if "redact" not in endpoint:
            return

        targets = self._get_event_id_endpoints()
        self._send_extended_reqs(targets)

    # dumb hard-coded stuff, take it for now ^^
    def _get_event_id_endpoints(self):
        targets = []
        for request in self._fuzzing_requests:
            endpoint = getattr(request, "endpoint", "") or ""
            last_chunk = endpoint.split("/")[-1]
            if "event_id" in last_chunk and getattr(request, "method", "") == "GET":
                targets.append(copy.copy(request))
        return targets

    def _send_extended_reqs(self, targets):
        for target in targets:
            seq = self._sequence + Sequence(target)
            response, _ = self._render_and_send_data(seq, target)
            if not response:
                # Don't abort the whole checker run because one request failed
                continue

            body = getattr(response, "json_body", None)
            if not body:
                continue

            try:
                resp_json = json.loads(body)
            except (TypeError, ValueError):
                # Not valid JSON; ignore for this checker
                continue

            content = resp_json.get("content", None)
            if content is None:
                continue

            # Flag only if content is present and not an empty dict
            if content != {}:
                self._print_suspect_sequence(seq, response)
                BugBuckets.Instance().update_bug_buckets(
                    seq,
                    response.status_code,
                    origin=self.__class__.__name__,
                )

    def _false_alarm(self, seq, response):
        return False