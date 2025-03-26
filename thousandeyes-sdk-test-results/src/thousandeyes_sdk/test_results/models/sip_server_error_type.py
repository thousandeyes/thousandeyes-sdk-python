# coding: utf-8

"""
    Test Results API

    Get test result metrics for Network and Application Synthetics tests.

    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class SipServerErrorType(str, Enum):
    """
    Error type, none if there is no error
    """

    """
    allowed enum values
    """
    NONE = 'none'
    DNS = 'dns'
    CONNECT = 'connect'
    REGISTER = 'register'
    INVITE = 'invite'
    OPTION = 'option'
    SERVER = 'server'
    SSL = 'ssl'
    UNKNOWN = 'unknown'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of SipServerErrorType from a JSON string"""
        return cls(json.loads(json_str))

    @classmethod
    def _missing_(cls, value):
        """Handle unknown values"""
        return cls.UNKNOWN

