# coding: utf-8

"""
    Dashboards API

    Manage ThousandEyes Dashboards.

    The version of the OpenAPI document: 7.0.12
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class ApiAgentWidgetShow(str, Enum):
    """
    Ownership of the agent.
    """

    """
    allowed enum values
    """
    OWNED = 'owned'
    ALL = 'all'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ApiAgentWidgetShow from a JSON string"""
        return cls(json.loads(json_str))


