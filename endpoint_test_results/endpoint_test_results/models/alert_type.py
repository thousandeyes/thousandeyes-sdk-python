# coding: utf-8

"""
    Endpoint Test Results API

    Retrieve results for scheduled and dynamic tests on endpoint agents.

    The version of the OpenAPI document: 7.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class AlertType(str, Enum):
    """
    Type of alert being triggered. In multi-layered tests, this value represents the layer the alert relates to. See [Alert Details](https://developer.thousandeyes.com/v7/alerts/#/alert-details) documentation for a list of possible values
    """

    """
    allowed enum values
    """
    PAGE_MINUS_LOAD = 'page-load'
    HTTP_MINUS_SERVER = 'http-server'
    END_MINUS_TO_MINUS_END_MINUS_SERVER = 'end-to-end-server'
    END_MINUS_TO_MINUS_END_MINUS_AGENT = 'end-to-end-agent'
    VOICE = 'voice'
    DNS_MINUS_SERVER = 'dns-server'
    DNS_MINUS_TRACE = 'dns-trace'
    DNSSEC = 'dnssec'
    BGP = 'bgp'
    PATH_MINUS_TRACE = 'path-trace'
    FTP = 'ftp'
    SIP_MINUS_SERVER = 'sip-server'
    TRANSACTIONS = 'transactions'
    WEB_MINUS_TRANSACTIONS = 'web-transactions'
    AGENT = 'agent'
    NETWORK_MINUS_OUTAGE = 'network-outage'
    APPLICATION_MINUS_OUTAGE = 'application-outage'
    DEVICE_MINUS_DEVICE = 'device-device'
    DEVICE_MINUS_INTERFACE = 'device-interface'
    ENDPOINT_MINUS_NETWORK_MINUS_SERVER = 'endpoint-network-server'
    ENDPOINT_MINUS_HTTP_MINUS_SERVER = 'endpoint-http-server'
    ENDPOINT_MINUS_PATH_MINUS_TRACE = 'endpoint-path-trace'
    ENDPOINT_MINUS_BROWSER_MINUS_SESSIONS_MINUS_AGENT = 'endpoint-browser-sessions-agent'
    ENDPOINT_MINUS_BROWSER_MINUS_SESSIONS_MINUS_APPLICATION = 'endpoint-browser-sessions-application'
    API = 'api'
    WEB_MINUS_TRANSACTION = 'web-transaction'
    UNKNOWN = 'unknown'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of AlertType from a JSON string"""
        return cls(json.loads(json_str))

