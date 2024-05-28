# coding: utf-8

"""
    Dashboards API

    Manage ThousandEyes Dashboards.

    The version of the OpenAPI document: 7.0.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class WidgetMeasureType(str, Enum):
    """
    Determines how to aggregate the the metric.
    """

    """
    allowed enum values
    """
    MINIMUM = 'MINIMUM'
    MAXIMUM = 'MAXIMUM'
    MEAN = 'MEAN'
    MEDIAN = 'MEDIAN'
    NTH_PERCENTILE = 'NTH_PERCENTILE'
    PERCPOSITIVE = 'PERCPOSITIVE'
    PERCZERO = 'PERCZERO'
    STDDEV = 'STDDEV'
    TOTAL = 'TOTAL'
    VALUES = 'VALUES'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of WidgetMeasureType from a JSON string"""
        return cls(json.loads(json_str))

