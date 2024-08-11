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


class UdpPathTraceModeResponse(str, Enum):
    """
    Path trace mode used by network test. Only valid when the protocol is set to UDP.
    """

    """
    allowed enum values
    """
    STUN_MINUS_PCAP = 'stun-pcap'
    UNKNOWN = 'unknown'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of UdpPathTraceModeResponse from a JSON string"""
        return cls(json.loads(json_str))


