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


class ColorGridDatasource(str, Enum):
    """
    Datasource of the color grid widget.
    """

    """
    allowed enum values
    """
    THIRD_PARTY_APPLICATIONS = 'THIRD_PARTY_APPLICATIONS'
    ALERTS = 'ALERTS'
    CLOUD_AND_ENTERPRISE_AGENTS = 'CLOUD_AND_ENTERPRISE_AGENTS'
    DEVICES = 'DEVICES'
    ENDPOINT_AGENTS = 'ENDPOINT_AGENTS'
    ENDPOINT_AST_TEST = 'ENDPOINT_AST_TEST'
    ENDPOINT_BROWSER_SESSION = 'ENDPOINT_BROWSER_SESSION'
    ENDPOINT_LOCAL_NETWORK = 'ENDPOINT_LOCAL_NETWORK'
    ENDPOINT_LOCAL_NETWORK_WIRELESS = 'ENDPOINT_LOCAL_NETWORK_WIRELESS'
    ENDPOINT_SCHEDULED_TEST = 'ENDPOINT_SCHEDULED_TEST'
    INTERNET_INSIGHTS = 'INTERNET_INSIGHTS'
    ROUTING = 'ROUTING'
    UNKNOWN = 'unknown'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ColorGridDatasource from a JSON string"""
        return cls(json.loads(json_str))

    @classmethod
    def _missing_(cls, value):
        """Handle unknown values"""
        return cls.UNKNOWN

