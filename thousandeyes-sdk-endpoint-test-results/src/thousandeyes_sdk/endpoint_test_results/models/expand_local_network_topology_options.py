# coding: utf-8

"""
    Endpoint Test Results API

    Retrieve results for scheduled and dynamic tests on endpoint agents.

    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class ExpandLocalNetworkTopologyOptions(str, Enum):
    """
    ExpandLocalNetworkTopologyOptions
    """

    """
    allowed enum values
    """
    SYSTEM_MINUS_METRIC_MINUS_DETAIL = 'system-metric-detail'
    UNKNOWN = 'unknown'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ExpandLocalNetworkTopologyOptions from a JSON string"""
        return cls(json.loads(json_str))

    @classmethod
    def _missing_(cls, value):
        """Handle unknown values"""
        return cls.UNKNOWN

