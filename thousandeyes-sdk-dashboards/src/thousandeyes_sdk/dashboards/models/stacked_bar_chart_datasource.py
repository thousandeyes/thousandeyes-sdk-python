# coding: utf-8

"""
    Dashboards API

    Manage ThousandEyes Dashboards.

    The version of the OpenAPI document: 7.0.12
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class StackedBarChartDatasource(str, Enum):
    """
    Datasource of the stacked bar chart widget.
    """

    """
    allowed enum values
    """
    CLOUD_AND_ENTERPRISE_AGENTS = 'CLOUD_AND_ENTERPRISE_AGENTS'
    ENDPOINT_AGENTS = 'ENDPOINT_AGENTS'
    ENDPOINT_BROWSER_SESSION = 'ENDPOINT_BROWSER_SESSION'
    ENDPOINT_SCHEDULED_TEST = 'ENDPOINT_SCHEDULED_TEST'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of StackedBarChartDatasource from a JSON string"""
        return cls(json.loads(json_str))


