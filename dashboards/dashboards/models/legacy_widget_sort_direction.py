# coding: utf-8

"""
    Dashboards API

    Manage ThousandEyes Dashboards.

    The version of the OpenAPI document: 7.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class LegacyWidgetSortDirection(str, Enum):
    """
    Specifies the order in which cards are sorted.
    """

    """
    allowed enum values
    """
    ASCENDING = 'Ascending'
    DESCENDING = 'Descending'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of LegacyWidgetSortDirection from a JSON string"""
        return cls(json.loads(json_str))


