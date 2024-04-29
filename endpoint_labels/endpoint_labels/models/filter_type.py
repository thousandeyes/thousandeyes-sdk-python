# coding: utf-8

"""
    Endpoint Agent Labels API

    Manage labels applied to endpoint agents using this API. 

    The version of the OpenAPI document: 7.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class FilterType(str, Enum):
    """
    Type of filter - the data that will be used to filter.
    """

    """
    allowed enum values
    """
    AGENT_MINUS_ID = 'agent-id'
    PUBLIC_MINUS_NETWORK = 'public-network'
    LOCAL_MINUS_NETWORK = 'local-network'
    CONNECTION = 'connection'
    GATEWAY = 'gateway'
    PLATFORM = 'platform'
    AGENT_MINUS_TYPE = 'agent-type'
    VPN_MINUS_VENDOR = 'vpn-vendor'
    VPN_MINUS_GATEWAY_MINUS_ADDRESS = 'vpn-gateway-address'
    VPN_MINUS_CLIENT_MINUS_NETWORK = 'vpn-client-network'
    VPN_MINUS_CLIENT_MINUS_ADDRESS = 'vpn-client-address'
    IP_MINUS_ADDRESS_MINUS_FAMILY = 'ip-address-family'
    SSID = 'ssid'
    BSSID = 'bssid'
    HOSTNAME = 'hostname'
    USERNAME = 'username'
    ASN = 'asn'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of FilterType from a JSON string"""
        return cls(json.loads(json_str))

