# coding: utf-8

"""
    Dashboards API

    Manage ThousandEyes Dashboards.

    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class ApiWidgetSortProperty(str, Enum):
    """
    Determines the card sorting criterion.
    """

    """
    allowed enum values
    """
    ALPHABETICAL = 'alphabetical'
    VALUE = 'value'
    UNKNOWN = 'unknown'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ApiWidgetSortProperty from a JSON string"""
        return cls(json.loads(json_str))

    @classmethod
    def _missing_(cls, value):
        """Handle unknown values"""
        return cls.UNKNOWN

