# coding: utf-8

# flake8: noqa

"""
    Tags API

    The ThousandEyes Tags API provides a tagging system with key/value pairs. It allows you to tag assets within the ThousandEyes platform (such as agents, tests, or alert rules) with meaningful metadata. For example: `branch:sfo`, `branch:nyc`, and `team:netops`.  This feature provides:  * Support for automation. * Powerful and flexible reports/dashboards. * Support for third-party integrations.  Things to note with the ThousandEyes Tags API:  * Tags are backwards-compatible with existing labels. * Tags are separated by Tests (CEA), Agents (CEA), Endpoint Agents, Scheduled Endpoint Tests, and Reports. A single tag can only apply to one type of target object, so each tag must specify the target type of object via a `type` field. * Tags are defined in a single table so that they can be represented using a single model - `Tag`. 

    The version of the OpenAPI document: 7.0.6
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


# import apis into sdk package
from thousandeyes_sdk.tags.api.tag_assignment_api import TagAssignmentApi
from thousandeyes_sdk.tags.api.tags_api import TagsApi


# import models into sdk package
from thousandeyes_sdk.tags.models.access_type import AccessType
from thousandeyes_sdk.tags.models.api_error import ApiError
from thousandeyes_sdk.tags.models.assignment import Assignment
from thousandeyes_sdk.tags.models.assignment_type import AssignmentType
from thousandeyes_sdk.tags.models.bulk_tag_assignment import BulkTagAssignment
from thousandeyes_sdk.tags.models.bulk_tag_assignments import BulkTagAssignments
from thousandeyes_sdk.tags.models.bulk_tag_response import BulkTagResponse
from thousandeyes_sdk.tags.models.error import Error
from thousandeyes_sdk.tags.models.expand import Expand
from thousandeyes_sdk.tags.models.link import Link
from thousandeyes_sdk.tags.models.object_type import ObjectType
from thousandeyes_sdk.tags.models.self_links import SelfLinks
from thousandeyes_sdk.tags.models.tag import Tag
from thousandeyes_sdk.tags.models.tag_assignment import TagAssignment
from thousandeyes_sdk.tags.models.tag_bulk_create_error import TagBulkCreateError
from thousandeyes_sdk.tags.models.tag_info import TagInfo
from thousandeyes_sdk.tags.models.tags import Tags
from thousandeyes_sdk.tags.models.unauthorized_error import UnauthorizedError
from thousandeyes_sdk.tags.models.validation_error import ValidationError
from thousandeyes_sdk.tags.models.validation_error_item import ValidationErrorItem
