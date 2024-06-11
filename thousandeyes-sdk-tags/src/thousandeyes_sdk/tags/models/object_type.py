# coding: utf-8

"""
    Tags API

    The ThousandEyes Tags API provides a tagging system with key/value pairs. It allows you to tag assets within the ThousandEyes platform (such as agents, tests, or alert rules) with meaningful metadata. For example: `branch:sfo`, `branch:nyc`, and `team:netops`.  This feature provides:  * Support for automation. * Powerful and flexible reports/dashboards. * Support for third-party integrations.  Things to note with the ThousandEyes Tags API:  * Tags are backwards-compatible with existing labels. * Tags are separated by Tests (CEA), Agents (CEA), Endpoint Agents, Scheduled Endpoint Tests, and Reports. A single tag can only apply to one type of target object, so each tag must specify the target type of object via a `type` field. * Tags are defined in a single table so that they can be represented using a single model - `Tag`. 

    The version of the OpenAPI document: 7.0.7
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class ObjectType(str, Enum):
    """
    The object type associated with the tag
    """

    """
    allowed enum values
    """
    TEST = 'test'
    DASHBOARD = 'dashboard'
    ENDPOINT_MINUS_TEST = 'endpoint-test'
    V_MINUS_AGENT = 'v-agent'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ObjectType from a JSON string"""
        return cls(json.loads(json_str))


