# coding: utf-8

"""
    Agents API

     ## Overview Manage all agents available to your account in ThousandEyes, including both Cloud and Enterprise Agents.

    The version of the OpenAPI document: 7.0.0
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

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of TestType from a JSON string"""
        return cls(json.loads(json_str))


