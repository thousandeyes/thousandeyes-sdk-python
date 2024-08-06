# coding: utf-8

"""
    Dashboards API

    Manage ThousandEyes Dashboards.

    The version of the OpenAPI document: 7.0.14
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class TestTableFilterKey(str, Enum):
    """
    TestTableFilterKey
    """

    """
    allowed enum values
    """
    ANYTHING = 'Anything'
    TEST_NAME = 'Test Name'
    TARGET = 'Target'
    TEST_ID = 'Test ID'
    TEST_TYPE = 'Test type'
    LABEL_ID = 'Label ID'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of TestTableFilterKey from a JSON string"""
        return cls(json.loads(json_str))


