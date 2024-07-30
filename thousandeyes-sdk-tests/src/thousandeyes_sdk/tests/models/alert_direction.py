# coding: utf-8

"""
    Tests API

    This API supports listing, creating, editing, and deleting Cloud and Enterprise Agent (CEA) based tests. 

    The version of the OpenAPI document: 7.0.12
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class AlertDirection(str, Enum):
    """
    Direction for applicable alert types (eg. path trace, End-to-End (Agent) etc.)
    """

    """
    allowed enum values
    """
    TO_MINUS_TARGET = 'to-target'
    FROM_MINUS_TARGET = 'from-target'
    BIDIRECTIONAL = 'bidirectional'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of AlertDirection from a JSON string"""
        return cls(json.loads(json_str))


