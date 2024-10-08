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


class AlertListAlertType(str, Enum):
    """
    Name of the alert type
    """

    """
    allowed enum values
    """
    NETWORK_MINUS_END_MINUS_TO_MINUS_END_MINUS_SERVER = 'network-end-to-end-server'
    NETWORK_MINUS_END_MINUS_TO_MINUS_END_MINUS_AGENT = 'network-end-to-end-agent'
    NETWORK_MINUS_PATH_MINUS_TRACE = 'network-path-trace'
    DNS_MINUS_SERVER = 'dns-server'
    DNS_MINUS_TRACE = 'dns-trace'
    DNSSEC = 'dnssec'
    DNS_MINUS_PLUS_MINUS_DOMAIN = 'dns-plus-domain'
    DNS_MINUS_PLUS_MINUS_SERVER = 'dns-plus-server'
    WEB_MINUS_HTTP_MINUS_SERVER = 'web-http-server'
    WEB_MINUS_PAGE_MINUS_LOAD = 'web-page-load'
    WEB_MINUS_TRANSACTION_MINUS_CLASSIC = 'web-transaction-classic'
    WEB_MINUS_TRANSACTION = 'web-transaction'
    WEB_MINUS_FTP_MINUS_SERVER = 'web-ftp-server'
    VOICE_MINUS_SIP_MINUS_SERVER = 'voice-sip-server'
    VOICE_MINUS_RTP_MINUS_STREAM = 'voice-rtp-stream'
    DEVICE = 'device'
    DEVICE_MINUS_INTERFACE = 'device-interface'
    ENDPOINT_MINUS_END_MINUS_TO_MINUS_END_MINUS_SERVER = 'endpoint-end-to-end-server'
    ENDPOINT_MINUS_WEB_MINUS_HTTP_MINUS_SERVER = 'endpoint-web-http-server'
    ENDPOINT_MINUS_PATH_MINUS_TRACE = 'endpoint-path-trace'
    BROWSER_MINUS_SESSION_MINUS_AGENT = 'browser-session-agent'
    BROWSER_MINUS_SESSION_MINUS_APPLICATION = 'browser-session-application'
    ROUTING_MINUS_BGP = 'routing-bgp'
    UNKNOWN = 'unknown'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of AlertListAlertType from a JSON string"""
        return cls(json.loads(json_str))

    @classmethod
    def _missing_(cls, value):
        """Handle unknown values"""
        return cls.UNKNOWN

