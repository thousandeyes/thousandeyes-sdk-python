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


class AgentStatusDatasource(str, Enum):
    """
    Datasource of the agent to retrieve status.
    """

    """
    allowed enum values
    """
    ALERTS = 'ALERTS'
    DEVICES = 'DEVICES'
    DNSP = 'DNSP'
    ENDPOINT_AGENTS = 'ENDPOINT_AGENTS'
    ENDPOINT_SCHEDULED_TEST = 'ENDPOINT_SCHEDULED_TEST'
    ENDPOINT_AST_TEST = 'ENDPOINT_AST_TEST'
    ENDPOINT_BROWSER_SESSION = 'ENDPOINT_BROWSER_SESSION'
    ENDPOINT_LOCAL_NETWORK = 'ENDPOINT_LOCAL_NETWORK'
    ENDPOINT_LOCAL_NETWORK_WIRELESS = 'ENDPOINT_LOCAL_NETWORK_WIRELESS'
    ROUTING = 'ROUTING'
    CLOUD_AND_ENTERPRISE_AGENTS = 'CLOUD_AND_ENTERPRISE_AGENTS'
    INTERNET_INSIGHTS = 'INTERNET_INSIGHTS'
    APPDYNAMICS_SERVICE_HEALTH = 'APPDYNAMICS_SERVICE_HEALTH'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of AgentStatusDatasource from a JSON string"""
        return cls(json.loads(json_str))


