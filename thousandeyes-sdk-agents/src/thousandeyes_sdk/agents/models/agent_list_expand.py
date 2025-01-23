# coding: utf-8

"""
    Agents API

     ## Overview Manage Cloud and Enterprise Agents available to your account in ThousandEyes.

    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class AgentListExpand(str, Enum):
    """
    AgentListExpand
    """

    """
    allowed enum values
    """
    CLUSTER_MINUS_MEMBER = 'cluster-member'
    UNKNOWN = 'unknown'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of AgentListExpand from a JSON string"""
        return cls(json.loads(json_str))

    @classmethod
    def _missing_(cls, value):
        """Handle unknown values"""
        return cls.UNKNOWN

