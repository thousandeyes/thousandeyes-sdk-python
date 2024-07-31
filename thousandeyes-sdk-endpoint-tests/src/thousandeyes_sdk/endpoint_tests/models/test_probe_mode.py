# coding: utf-8

"""
    Endpoint Tests API

     Manage endpoint agent dynamic and scheduled tests using the Endpoint Tests API. 

    The version of the OpenAPI document: 7.0.13
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class TestProbeMode(str, Enum):
    """
    Probe mode used by network test, only valid when the protocol is set to TCP.
    """

    """
    allowed enum values
    """
    AUTO = 'auto'
    SACK = 'sack'
    SYN = 'syn'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of TestProbeMode from a JSON string"""
        return cls(json.loads(json_str))


