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


class TestSubInterval(int, Enum):
    """
    Subinterval for round-robin testing (in seconds). Must be less than or equal to interval and must evenly divide interval.
    """

    """
    allowed enum values
    """
    NUMBER_60 = 60
    NUMBER_120 = 120
    NUMBER_300 = 300
    NUMBER_600 = 600
    NUMBER_900 = 900
    NUMBER_1200 = 1200
    NUMBER_1800 = 1800
    NUMBER_3600 = 3600
    NUMBER_11184809 = 11184809

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of TestSubInterval from a JSON string"""
        return cls(json.loads(json_str))

    @classmethod
    def _missing_(cls, value):
        """Handle unknown values"""
        return cls.UNKNOWN

