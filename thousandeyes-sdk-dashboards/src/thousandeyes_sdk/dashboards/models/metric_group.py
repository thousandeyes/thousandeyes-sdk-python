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


class MetricGroup(str, Enum):
    """
    Metric group of widget as it appears in the UI. Note: may not be required in some cases.
    """

    """
    allowed enum values
    """
    AGENT_TO_AGENT = 'AGENT_TO_AGENT'
    AGENT_TO_SERVER = 'AGENT_TO_SERVER'
    HTTP_SERVER = 'HTTP_SERVER'
    FTP_SERVER = 'FTP_SERVER'
    PAGE_LOAD = 'PAGE_LOAD'
    TRANSACTIONS_CLASSIC = 'TRANSACTIONS_CLASSIC'
    TRANSACTIONS = 'TRANSACTIONS'
    API = 'API'
    ENDPOINT_BROWSER_SESSION_NETWORK = 'ENDPOINT_BROWSER_SESSION_NETWORK'
    ENDPOINT_BROWSER_SESSION_SYSTEM = 'ENDPOINT_BROWSER_SESSION_SYSTEM'
    ENDPOINT_BROWSER_SESSION_VISITED_PAGES = 'ENDPOINT_BROWSER_SESSION_VISITED_PAGES'
    ENDPOINT_SCHEDULED_TEST_HTTP_SERVER = 'ENDPOINT_SCHEDULED_TEST_HTTP_SERVER'
    ENDPOINT_SCHEDULED_TEST_NETWORK = 'ENDPOINT_SCHEDULED_TEST_NETWORK'
    ENDPOINT_SCHEDULED_TEST_SYSTEM = 'ENDPOINT_SCHEDULED_TEST_SYSTEM'
    ENDPOINT_AST_TEST_NETWORK = 'ENDPOINT_AST_TEST_NETWORK'
    ENDPOINT_AST_TEST_SYSTEM = 'ENDPOINT_AST_TEST_SYSTEM'
    ENDPOINT_LOCAL_NETWORK_GATEWAY = 'ENDPOINT_LOCAL_NETWORK_GATEWAY'
    ENDPOINT_LOCAL_NETWORK_AGENTS = 'ENDPOINT_LOCAL_NETWORK_AGENTS'
    ENDPOINT_LOCAL_NETWORK_DNS = 'ENDPOINT_LOCAL_NETWORK_DNS'
    ENDPOINT_LOCAL_NETWORK_NETWORK_ACCESS = 'ENDPOINT_LOCAL_NETWORK_NETWORK_ACCESS'
    ENDPOINT_LOCAL_NETWORK_PROXY = 'ENDPOINT_LOCAL_NETWORK_PROXY'
    ENDPOINT_LOCAL_NETWORK_SYSTEM = 'ENDPOINT_LOCAL_NETWORK_SYSTEM'
    ENDPOINT_LOCAL_NETWORK_VPN = 'ENDPOINT_LOCAL_NETWORK_VPN'
    ENDPOINT_LOCAL_NETWORK_WIRELESS = 'ENDPOINT_LOCAL_NETWORK_WIRELESS'
    BGP = 'BGP'
    DEVICE = 'DEVICE'
    VOIP = 'VOIP'
    SIP = 'SIP'
    ALERTS = 'ALERTS'
    DNS = 'DNS'
    DOMAIN_TRACE = 'DOMAIN_TRACE'
    DNSSEC = 'DNSSEC'
    DNSP = 'DNSP'
    NETWORK_OUTAGES = 'NETWORK_OUTAGES'
    APPLICATION_OUTAGES = 'APPLICATION_OUTAGES'
    APPDYNAMICS_SERVICE_HEALTH = 'APPDYNAMICS_SERVICE_HEALTH'
    CLOUD_NATIVE_MONITORING_MINUS_TRAFFIC_FLOW = 'CLOUD_NATIVE_MONITORING-TRAFFIC_FLOW'
    CLOUD_NATIVE_MONITORING_MINUS_EVENTS = 'CLOUD_NATIVE_MONITORING-EVENTS'
    TRAFFIC_INSIGHTS_MONITORING_MINUS_TRAFFIC_FLOW = 'TRAFFIC_INSIGHTS_MONITORING-TRAFFIC_FLOW'
    UNKNOWN = 'unknown'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of MetricGroup from a JSON string"""
        return cls(json.loads(json_str))

    @classmethod
    def _missing_(cls, value):
        """Handle unknown values"""
        return cls.UNKNOWN

