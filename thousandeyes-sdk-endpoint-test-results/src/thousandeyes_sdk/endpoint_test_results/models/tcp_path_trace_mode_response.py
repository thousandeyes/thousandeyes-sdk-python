# coding: utf-8

"""
    Endpoint Test Results API

    Retrieve results for scheduled and dynamic tests on endpoint agents.

    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class TcpPathTraceModeResponse(str, Enum):
    """
    Path trace mode used by network test. Only valid when the protocol is set to TCP.
    """

    """
    allowed enum values
    """
    AUTO = 'auto'
    SYN = 'syn'
    UNKNOWN = 'unknown'
    DATA_MINUS_IN_MINUS_SESSION_MINUS_WITH_MINUS_DECREMENTING_MINUS_TTL = 'data-in-session-with-decrementing-ttl'
    DATA_MINUS_IN_MINUS_SESSION = 'data-in-session'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of TcpPathTraceModeResponse from a JSON string"""
        return cls(json.loads(json_str))

    @classmethod
    def _missing_(cls, value):
        """Handle unknown values"""
        return cls.UNKNOWN

