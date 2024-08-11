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


class NumbersCardDatasource(str, Enum):
    """
    Datasource of the numbers card widget.
    """

    """
    allowed enum values
    """
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

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of NumbersCardDatasource from a JSON string"""
        return cls(json.loads(json_str))


