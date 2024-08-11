# coding: utf-8

"""
    Agents API

     ## Overview Manage all agents available to your account in ThousandEyes, including both Cloud and Enterprise Agents.

    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class ProxyType(str, Enum):
    """
    The type of proxy, STATIC or PAC.
    """

    """
    allowed enum values
    """
    STATIC = 'static'
    PAC = 'pac'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ProxyType from a JSON string"""
        return cls(json.loads(json_str))


