# coding: utf-8

"""
    Tests API

    This API supports listing, creating, editing, and deleting Cloud and Enterprise Agent (CEA) based tests. 

    The version of the OpenAPI document: 7.0.6
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class Severity(str, Enum):
    """
    The severity of the alert.
    """

    """
    allowed enum values
    """
    INFO = 'info'
    MAJOR = 'major'
    MINOR = 'minor'
    CRITICAL = 'critical'
    UNKNOWN = 'unknown'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of Severity from a JSON string"""
        return cls(json.loads(json_str))


