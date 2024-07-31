# coding: utf-8

"""
    Endpoint Agents API

    Manage ThousandEyes Endpoint Agents using this API.   For more information about Endpoint Agents, see [Endpoint Agents](https://docs.thousandeyes.com/product-documentation/global-vantage-points/endpoint-agents).

    The version of the OpenAPI document: 7.0.13
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class VpnType(str, Enum):
    """
    Name of the VPN provider.
    """

    """
    allowed enum values
    """
    CISCO_MINUS_ANYCONNECT = 'cisco-anyconnect'
    PALO_MINUS_ALTO_MINUS_GLOBALPROTECT = 'palo-alto-globalprotect'
    IVANTI_MINUS_CONNECT_MINUS_SECURE = 'ivanti-connect-secure'
    ZSCALER_MINUS_INTERNET_MINUS_ACCESS = 'zscaler-internet-access'
    F5_MINUS_BIG_MINUS_IP = 'f5-big-ip'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of VpnType from a JSON string"""
        return cls(json.loads(json_str))


