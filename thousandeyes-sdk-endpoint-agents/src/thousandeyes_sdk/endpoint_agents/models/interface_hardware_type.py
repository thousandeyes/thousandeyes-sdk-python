# coding: utf-8

"""
    Endpoint Agents API

    Manage ThousandEyes Endpoint Agents using this API.   For more information about Endpoint Agents, see [Endpoint Agents](https://docs.thousandeyes.com/product-documentation/global-vantage-points/endpoint-agents).

    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class InterfaceHardwareType(str, Enum):
    """
    InterfaceHardwareType
    """

    """
    allowed enum values
    """
    UNKNOWN = 'unknown'
    WIRELESS = 'wireless'
    ETHERNET = 'ethernet'
    MODEM = 'modem'
    VIRTUAL = 'virtual'
    LOOPBACK = 'loopback'
    OTHER = 'other'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of InterfaceHardwareType from a JSON string"""
        return cls(json.loads(json_str))

    @classmethod
    def _missing_(cls, value):
        """Handle unknown values"""
        return cls.UNKNOWN

