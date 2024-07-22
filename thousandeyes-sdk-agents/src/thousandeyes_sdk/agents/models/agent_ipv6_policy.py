# coding: utf-8

"""
    Agents API

     ## Overview Manage all agents available to your account in ThousandEyes, including both Cloud and Enterprise Agents.

    The version of the OpenAPI document: 7.0.10
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class AgentIpv6Policy(str, Enum):
    """
    IP version policy, (Enterprise Agents and Enterprise Clusters only)
    """

    """
    allowed enum values
    """
    FORCE_MINUS_IPV4 = 'force-ipv4'
    PREFER_MINUS_IPV6 = 'prefer-ipv6'
    FORCE_MINUS_IPV6 = 'force-ipv6'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of AgentIpv6Policy from a JSON string"""
        return cls(json.loads(json_str))


