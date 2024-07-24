# coding: utf-8

"""
    Endpoint Agents API

    Manage ThousandEyes Endpoint Agents using this API.   For more information about Endpoint Agents, see [Endpoint Agents](https://docs.thousandeyes.com/product-documentation/global-vantage-points/endpoint-agents).

    The version of the OpenAPI document: 7.0.10
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class AddressType(str, Enum):
    """
    AddressType
    """

    """
    allowed enum values
    """
    LOOPBACK = 'loopback'
    UNSPECIFIED = 'unspecified'
    UNIQUE_MINUS_LOCAL = 'unique-local'
    LINK_MINUS_LOCAL = 'link-local'
    UNIQUE_MINUS_GLOBAL = 'unique-global'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of AddressType from a JSON string"""
        return cls(json.loads(json_str))


