# coding: utf-8

# flake8: noqa

"""
    Labels API

    ### Overview This is API for the Labels API (formerly called groups).

    The version of the OpenAPI document: 7.0.13
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


# import apis into sdk package
from thousandeyes_sdk.labels.api.agent_api import AgentApi
from thousandeyes_sdk.labels.api.all_labels_api import AllLabelsApi
from thousandeyes_sdk.labels.api.dashboard_api import DashboardApi
from thousandeyes_sdk.labels.api.endpoint_test_api import EndpointTestApi
from thousandeyes_sdk.labels.api.test_api import TestApi


# import models into sdk package
from thousandeyes_sdk.labels.models.error import Error
from thousandeyes_sdk.labels.models.label import Label
from thousandeyes_sdk.labels.models.label_detail import LabelDetail
from thousandeyes_sdk.labels.models.label_request import LabelRequest
from thousandeyes_sdk.labels.models.label_type import LabelType
from thousandeyes_sdk.labels.models.labels import Labels
from thousandeyes_sdk.labels.models.link import Link
from thousandeyes_sdk.labels.models.self_links import SelfLinks
from thousandeyes_sdk.labels.models.unauthorized_error import UnauthorizedError
from thousandeyes_sdk.labels.models.validation_error import ValidationError
from thousandeyes_sdk.labels.models.validation_error_item import ValidationErrorItem
