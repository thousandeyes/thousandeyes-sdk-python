# coding: utf-8

"""
    Dashboards API

    Manage ThousandEyes Dashboards.

    The version of the OpenAPI document: 7.0.10
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class ApiWidgetFixedYScalePrefix(str, Enum):
    """
    Prefix denoting the unit of measurement for the fixed Y-axis scale.
    """

    """
    allowed enum values
    """
    KBPS = 'Kbps'
    MBPS = 'Mbps'
    GBPS = 'Gbps'
    KPPS = 'Kpps'
    MPPS = 'Mpps'
    GPPS = 'Gpps'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ApiWidgetFixedYScalePrefix from a JSON string"""
        return cls(json.loads(json_str))


