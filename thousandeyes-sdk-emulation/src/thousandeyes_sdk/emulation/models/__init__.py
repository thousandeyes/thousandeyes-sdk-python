# coding: utf-8

# flake8: noqa
"""
    Emulation API

    The Emulation API facilitates the retrieval of user-agent strings for HTTP, pageload, and transaction tests. It also enables the retrieval and addition of emulated devices for pageload and transaction tests.  To access Emulation API endpoints, the following permissions are required:  * `Settings Tests Read` for read operations. * `Settings Tests Update` for write operations. 

    The version of the OpenAPI document: 7.0.14
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


# import models into model package
from thousandeyes_sdk.emulation.models.emulated_device import EmulatedDevice
from thousandeyes_sdk.emulation.models.emulated_device_category import EmulatedDeviceCategory
from thousandeyes_sdk.emulation.models.emulated_device_response import EmulatedDeviceResponse
from thousandeyes_sdk.emulation.models.emulated_device_responses import EmulatedDeviceResponses
from thousandeyes_sdk.emulation.models.error import Error
from thousandeyes_sdk.emulation.models.expand import Expand
from thousandeyes_sdk.emulation.models.link import Link
from thousandeyes_sdk.emulation.models.self_links import SelfLinks
from thousandeyes_sdk.emulation.models.unauthorized_error import UnauthorizedError
from thousandeyes_sdk.emulation.models.user_agent import UserAgent
from thousandeyes_sdk.emulation.models.user_agents import UserAgents
