# coding: utf-8

"""
    ThousandEyes for OpenTelemetry API

    ThousandEyes for OpenTelemetry provides machine-to-machine integration between ThousandEyes and its customers. It allows you to export ThousandEyes telemetry data in OTel format, which is widely used in the industry. With ThousandEyes for OTel, you can leverage frameworks widely used in the observability domain - such as Splunk, Grafana, and Honeycomb - to capture and analyze ThousandEyes data. Any client that supports OTel can use ThousandEyes for OpenTelemetry.  ThousandEyes for OTel is made up of the following components:  * Data streaming APIs that you can use to configure and enable your ThousandEyes tests with OTel-compatible streams, in particular to configure how ThousandEyes telemetry data is exported to client integrations. * A set of streaming pipelines called _collectors_ that actively fetch ThousandEyes network test data, enrich the data with some additional detail, filter, and push the data to the customer-configured endpoints, depending on what you configure via the public APIs. * Third-party OTel collectors that receive, transform, filter, and export different metrics to client applications such as AppD, or any other OTel-capable client configuration.  For more information about ThousandEyes for OpenTelemetry, see the [documentation](https://docs.thousandeyes.com/product-documentation/api/opentelemetry). 

    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class TestType(str, Enum):
    """
    This is a read only value, as test type is implicit in the test creation url.
    """

    """
    allowed enum values
    """
    API = 'api'
    AGENT_MINUS_TO_MINUS_AGENT = 'agent-to-agent'
    AGENT_MINUS_TO_MINUS_SERVER = 'agent-to-server'
    BGP = 'bgp'
    HTTP_MINUS_SERVER = 'http-server'
    PAGE_MINUS_LOAD = 'page-load'
    WEB_MINUS_TRANSACTIONS = 'web-transactions'
    FTP_MINUS_SERVER = 'ftp-server'
    DNS_MINUS_TRACE = 'dns-trace'
    DNS_MINUS_SERVER = 'dns-server'
    DNSSEC = 'dnssec'
    SIP_MINUS_SERVER = 'sip-server'
    VOICE = 'voice'
    UNKNOWN = 'unknown'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of TestType from a JSON string"""
        return cls(json.loads(json_str))

    @classmethod
    def _missing_(cls, value):
        """Handle unknown values"""
        return cls.UNKNOWN

