"""Implements logic for specific rule: cannot access message content after redacting."""

from __future__ import print_function

import copy
import json

from checkers.checker_base import *

from engine.core.sequences import Sequence
from engine.bug_bucketing import BugBuckets

from utils.logger import raw_network_logging as RAW_LOGGING


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
        RAW_LOGGING(f"DEBUG: HI")
        import re
        last_sent = self._sequence.sent_request_data_list[-1]
        match = re.search(r"/rooms/([^/]+)/redact/([^/]+)/", last_sent.rendered_data)
        if not match:
            RAW_LOGGING("DEBUG: could not extract ids")
            return

        room_id = match.group(1)
        event_id = match.group(2)
        RAW_LOGGING(f"DEBUG: room_id={room_id!r}, event_id={event_id!r}")

        targets = self._get_event_id_endpoints()
        self._send_extended_reqs(targets, room_id, event_id)

    # dumb hard-coded stuff, take it for now ^^
    def _get_event_id_endpoints(self):
        targets = []
        RAW_LOGGING(f"_get_event_id_endpoints:")
        for request in self._fuzzing_requests:
            endpoint = getattr(request, "endpoint", "") or ""
            RAW_LOGGING(f"DEBUG: endpoint={endpoint!r}")
            # Match /_matrix/client/.../rooms/.../event/... GET requests
            if "/event/" in endpoint and getattr(request, "method", "") == "GET":
                targets.append(copy.copy(request))
        RAW_LOGGING(f"DEBUG: found {len(targets)} targets")
        return targets

    def _send_extended_reqs(self, targets, room_id, event_id):
        
        for target in targets:
            rendered_values, parser, _, _, _ = next(target.render_iter(
                self._req_collection.candidate_values_pool,
                preprocessing=False,
                value_list=True
            ))

            # Substitute room_id and event_id by finding their positions structurally
            path_parts = [i for i, v in enumerate(rendered_values) if v in ('rooms', 'event')]
            for idx, v in enumerate(rendered_values):
                if v == 'rooms' and idx + 2 < len(rendered_values):
                    rendered_values[idx + 2] = room_id
                elif v == 'event' and idx + 2 < len(rendered_values):
                    rendered_values[idx + 2] = event_id

            rendered_data = "".join(rendered_values)
            RAW_LOGGING(f"DEBUG: rendered_data={rendered_data!r}")

            response = request_utilities.send_request_data(rendered_data)
            if not response:
                RAW_LOGGING("DEBUG: no response")
                return
            RAW_LOGGING(f"DEBUG: response status={response.status_code}")
            body = getattr(response, "json_body", None)
            if not body:
                RAW_LOGGING("DEBUG: no body")
                return
            try:
                resp_json = json.loads(body)
            except (TypeError, ValueError):
                return
            content = resp_json.get("content", None)
            if content is None:
                RAW_LOGGING("DEBUG: no content field")
                return
            if content != {} and any(k in content for k in ("body", "msgtype", "url", "filename")):
                RAW_LOGGING(f"DEBUG: BUG FOUND - content still readable: {content}")
                self._print_suspect_sequence(self._sequence, response)
                BugBuckets.Instance().update_bug_buckets(
                    self._sequence,
                    response.status_code,
                    origin=self.__class__.__name__,
                )
            else:
                RAW_LOGGING(f"DEBUG: content is empty after redaction, no bug")
            
            
    def _false_alarm(self, seq, response):
        return False