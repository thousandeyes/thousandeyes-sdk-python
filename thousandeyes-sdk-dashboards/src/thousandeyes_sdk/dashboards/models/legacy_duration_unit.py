# coding: utf-8

"""
    Dashboards API

    Manage ThousandEyes Dashboards.

    The version of the OpenAPI document: 7.0.6
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class LegacyDurationUnit(str, Enum):
    """
    Timespan unit.
    """

    """
    allowed enum values
    """
    MINUTES = 'Minutes'
    HOURS = 'Hours'
    DAYS = 'Days'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of LegacyDurationUnit from a JSON string"""
        return cls(json.loads(json_str))


