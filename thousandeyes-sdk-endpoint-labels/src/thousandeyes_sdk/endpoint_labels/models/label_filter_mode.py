# coding: utf-8

"""
    Endpoint Agent Labels API

    Manage labels applied to endpoint agents using this API. 

    The version of the OpenAPI document: 7.0.14
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class LabelFilterMode(str, Enum):
    """
    Type of matching to be applied for the values:  * `in`: The value on the agent must match one of the list of values provided. * `not-in`: The value on the agent must not match any of the list of values provided. 
    """

    """
    allowed enum values
    """
    IN = 'in'
    NOT_MINUS_IN = 'not-in'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of LabelFilterMode from a JSON string"""
        return cls(json.loads(json_str))


