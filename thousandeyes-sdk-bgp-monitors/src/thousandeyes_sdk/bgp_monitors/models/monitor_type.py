# coding: utf-8

"""
    BGP Monitors API

     Retrieve information about BGP monitors available to your ThousandEyes account. ThousandEyes ingests BGP routing data from dozens of global BGP collectors and automatically integrates that visibility as a configurable layer under service, network, and path visualization layers.  When you specify a service URL in a test, layered BGP tests automatically track reachability and path changes for any relevant prefix. When you use an IP address as the target for a test, the ThousandEyes platform monitors the relevant internet-routed prefix. You can also create specific BGP monitoring for a prefix, and can alert on hijacks and leaks.  For more information about monitors, see [Inside-Out BGP Visibility](https://docs.thousandeyes.com/product-documentation/internet-and-wan-monitoring/tests/bgp-tests/inside-out-bgp-visibility). 

    The version of the OpenAPI document: 7.0.10
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class MonitorType(str, Enum):
    """
    Type of monitor
    """

    """
    allowed enum values
    """
    PUBLIC = 'public'
    PRIVATE = 'private'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of MonitorType from a JSON string"""
        return cls(json.loads(json_str))


