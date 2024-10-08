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


class HttpEndpointTestsDataSearchSortKey(str, Enum):
    """
    HttpEndpointTestsDataSearchSortKey
    """

    """
    allowed enum values
    """
    ROUND_MINUS_ID = 'round-id'
    RESPONSE_MINUS_TIME = 'response-time'
    DNS_MINUS_TIME = 'dns-time'
    CONNECT_MINUS_TIME = 'connect-time'
    SSL_MINUS_TIME = 'ssl-time'
    WAIT_MINUS_TIME = 'wait-time'
    RESPONSE_MINUS_CODE = 'response-code'
    WIRE_MINUS_SIZE = 'wire-size'
    UNKNOWN = 'unknown'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of HttpEndpointTestsDataSearchSortKey from a JSON string"""
        return cls(json.loads(json_str))

    @classmethod
    def _missing_(cls, value):
        """Handle unknown values"""
        return cls.UNKNOWN

