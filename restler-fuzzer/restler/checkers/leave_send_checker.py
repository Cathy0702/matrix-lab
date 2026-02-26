"""Implements logic for specific rule: cannot send message to a room after leave that room."""

from __future__ import print_function

import copy
import json

from checkers.checker_base import *

from engine.core.sequences import Sequence
from engine.bug_bucketing import BugBuckets

class LeaveSendChecker(CheckerBase):
    def __init__(self, req_collection, fuzzing_requests):
        super(LeaveSendChecker, self).__init__(req_collection, fuzzing_requests)

    def apply(self, rendered_sequence, lock):
        if not rendered_sequence.valid:
            return
        
        self._sequence = rendered_sequence.sequence
        self._lock = lock

        last_req = self._sequence.last_request
        endpoint = getattr(last_req, "endpoint", "") or ""

        if "leave" not in endpoint:
            return
        target = self._get_send_endpoint()
        if not target:
            return
        self._send_extended_req(target)

        
    def _get_send_endpoint(self):
        for request in self._fuzzing_requests:
            endpoint = getattr(request, "endpoint", "") or ""
            if "send/m.room.message" in endpoint:
                return copy.copy(request)
        return None
    
    def _send_extended_req(self, target):
        seq = self._sequence + Sequence(target)
        response, _ = self._render_and_send_data(seq, target)
        if response and self._rule_violation(seq, response):
            self._print_suspect_sequence(seq, response)
            BugBuckets.Instance().update_bug_buckets(
                seq,
                response.status_code,
                origin=self.__class__.__name__,
            )
        
