# coding: utf-8

"""
    Tests API

    This API supports listing, creating, editing, and deleting Cloud and Enterprise Agent (CEA) based tests. 

    The version of the OpenAPI document: 7.0.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class TestDscpId(str, Enum):
    """
    DSCP ID [to see list for acceptable values](https://docs.thousandeyes.com/product-documentation/tests/dscp-options-in-network-tests)
    """

    """
    allowed enum values
    """
    ENUM_0 = '0'
    ENUM_8 = '8'
    ENUM_16 = '16'
    ENUM_24 = '24'
    ENUM_32 = '32'
    ENUM_40 = '40'
    ENUM_48 = '48'
    ENUM_56 = '56'
    ENUM_10 = '10'
    ENUM_12 = '12'
    ENUM_14 = '14'
    ENUM_18 = '18'
    ENUM_20 = '20'
    ENUM_22 = '22'
    ENUM_26 = '26'
    ENUM_28 = '28'
    ENUM_30 = '30'
    ENUM_34 = '34'
    ENUM_36 = '36'
    ENUM_38 = '38'
    ENUM_46 = '46'
    ENUM_44 = '44'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of TestDscpId from a JSON string"""
        return cls(json.loads(json_str))

