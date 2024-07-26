# coding: utf-8

# flake8: noqa
"""
    BGP Monitors API

     Retrieve information about BGP monitors available to your ThousandEyes account. ThousandEyes ingests BGP routing data from dozens of global BGP collectors and automatically integrates that visibility as a configurable layer under service, network, and path visualization layers.  When you specify a service URL in a test, layered BGP tests automatically track reachability and path changes for any relevant prefix. When you use an IP address as the target for a test, the ThousandEyes platform monitors the relevant internet-routed prefix. You can also create specific BGP monitoring for a prefix, and can alert on hijacks and leaks.  For more information about monitors, see [Inside-Out BGP Visibility](https://docs.thousandeyes.com/product-documentation/internet-and-wan-monitoring/tests/bgp-tests/inside-out-bgp-visibility). 

    The version of the OpenAPI document: 7.0.11
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


# import models into model package
from thousandeyes_sdk.bgp_monitors.models.error import Error
from thousandeyes_sdk.bgp_monitors.models.link import Link
from thousandeyes_sdk.bgp_monitors.models.monitor import Monitor
from thousandeyes_sdk.bgp_monitors.models.monitor_type import MonitorType
from thousandeyes_sdk.bgp_monitors.models.monitors import Monitors
from thousandeyes_sdk.bgp_monitors.models.self_links import SelfLinks
from thousandeyes_sdk.bgp_monitors.models.unauthorized_error import UnauthorizedError
