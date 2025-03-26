# coding: utf-8

"""
    Tests API

    This API allows you to list, create, edit, and delete Network and Application Synthetics tests. 

    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class TestDnsTransportProtocol(str, Enum):
    """
    Transport protocol used for DNS requests.
    """

    """
    allowed enum values
    """
    UDP = 'udp'
    TCP = 'tcp'
    UNKNOWN = 'unknown'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of TestDnsTransportProtocol from a JSON string"""
        return cls(json.loads(json_str))

    @classmethod
    def _missing_(cls, value):
        """Handle unknown values"""
        return cls.UNKNOWN

