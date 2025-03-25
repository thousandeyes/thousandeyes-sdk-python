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


class TestDirection(str, Enum):
    """
    Direction of the test, which affects how results are shown.
    """

    """
    allowed enum values
    """
    TO_MINUS_TARGET = 'to-target'
    FROM_MINUS_TARGET = 'from-target'
    BIDIRECTIONAL = 'bidirectional'
    UNKNOWN = 'unknown'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of TestDirection from a JSON string"""
        return cls(json.loads(json_str))

    @classmethod
    def _missing_(cls, value):
        """Handle unknown values"""
        return cls.UNKNOWN

