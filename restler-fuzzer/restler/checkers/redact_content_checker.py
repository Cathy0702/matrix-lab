"""Checker for the rule: message content should not remain accessible after redaction."""

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
        method = getattr(last_req, "method", "") or ""

        if method != "PUT" or "redact" not in endpoint:
            return

        self._checker_log.checker_print(
            f"RedactContentChecker: Detected redact endpoint in last request: {endpoint}"
        )

        targets = self._get_followup_requests(endpoint)
        self._send_extended_reqs(targets)

    def _get_followup_requests(self, redact_endpoint):
        targets = []
        event_marker = self._extract_event_marker(redact_endpoint)

        for request in self._fuzzing_requests:
            endpoint = getattr(request, "endpoint", "") or ""
            method = getattr(request, "method", "") or ""

            if method != "GET":
                continue

            if "events" in endpoint and event_marker and event_marker in endpoint.split("/")[-1] :
                targets.append(copy.copy(request))
                continue

            if "relations" in endpoint:
                targets.append(copy.copy(request))

        return targets

    def _extract_event_marker(self, endpoint):
        if "event_id_msg" in endpoint:
            return "event_id_msg"
        if "event_id_reaction" in endpoint:
            return "event_id_reaction"
        return None

    def _send_extended_reqs(self, targets):
        for target in targets:
            self._sequence = self._sequence + Sequence(target)
            response, _ = self._render_and_send_data(self._sequence, target)
            if not response:
                continue

            resp_json = self._parse_json_body(response)
            if resp_json is None:
                continue

            endpoint = getattr(target, "endpoint", "") or ""

            if self._response_leaks_content(endpoint, resp_json):
                self._print_suspect_sequence(self._sequence, response)
                BugBuckets.Instance().update_bug_buckets(
                    self._sequence,
                    response.status_code,
                    origin=self.__class__.__name__,
                )

    def _parse_json_body(self, response):
        body = getattr(response, "json_body", None)
        if not body:
            return None

        try:
            return json.loads(body)
        except (TypeError, ValueError):
            return None

    def _response_leaks_content(self, endpoint, resp_json):
        if "events" in endpoint:
            content = resp_json.get("content")
            return self._has_meaningful_content(content)

        if "relations" in endpoint:
            chunk = resp_json.get("chunk")
            if not isinstance(chunk, list):
                return False

            for event in chunk:
                if not isinstance(event, dict):
                    continue
                if self._has_meaningful_content(event.get("content")):
                    return True

            return False

        return False

    def _has_meaningful_content(self, content):
        return content not in (None, {})

    def _false_alarm(self, seq, response):
        return False