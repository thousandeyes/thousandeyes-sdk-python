# coding: utf-8

"""
    Endpoint Tests API

     Manage endpoint agent dynamic and scheduled tests using the Endpoint Tests API. 

    The version of the OpenAPI document: 7.0.10
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class EndpointTestProtocol(str, Enum):
    """
    Protocol used to perform the test.
    """

    """
    allowed enum values
    """
    ICMP = 'icmp'
    ICMP_MINUS_WITH_MINUS_TCP_MINUS_CONNECT = 'icmp-with-tcp-connect'
    TCP = 'tcp'
    PREFER_MINUS_TCP = 'prefer-tcp'
    AST_MINUS_AUTODETECT = 'ast-autodetect'
    AUTODETECT = 'autodetect'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of EndpointTestProtocol from a JSON string"""
        return cls(json.loads(json_str))


