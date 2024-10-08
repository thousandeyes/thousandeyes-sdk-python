# coding: utf-8

"""
    Dashboards API

    Manage ThousandEyes Dashboards.

    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class LegacyAgentWidgetShow(str, Enum):
    """
    Ownership of the agent.
    """

    """
    allowed enum values
    """
    OWNED_AGENTS = 'Owned Agents'
    ALL_ASSIGNED_AGENTS = 'All Assigned Agents'
    UNKNOWN = 'unknown'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of LegacyAgentWidgetShow from a JSON string"""
        return cls(json.loads(json_str))

    @classmethod
    def _missing_(cls, value):
        """Handle unknown values"""
        return cls.UNKNOWN

