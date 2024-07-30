# coding: utf-8

"""
    Usage API

     These usage endpoints define the following operations:  * **Usage**: Retrieve usage data for the specified time period (default is one month).          * Users must have the `View Billing` permission to access this endpoint.     * This endpoint offers visibility across all account groups within the organization.     * Users with `View Billing` permission in multiple organizations should query the endpoint with the `aid` query string parameter (see optional parameters) for each organization.  * **Quotas**: Obtain organization and account usage quotas. Additionally, users with the appropriate permissions can create, update, or delete these quotas.          * Users must have the necessary permissions to perform quota-related actions.  Refer to the Usage API endpoints for detailed usage instructions and optional parameters. 

    The version of the OpenAPI document: 7.0.12
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class Expand(str, Enum):
    """
    Expand
    """

    """
    allowed enum values
    """
    TEST = 'test'
    ENTERPRISE_MINUS_AGENT = 'enterprise-agent'
    ENTERPRISE_MINUS_AGENT_MINUS_UNIT = 'enterprise-agent-unit'
    ENDPOINT_MINUS_AGENT = 'endpoint-agent'
    ENDPOINT_MINUS_AGENT_MINUS_ESSENTIAL = 'endpoint-agent-essential'
    ENDPOINT_MINUS_AGENT_MINUS_EMBEDDED = 'endpoint-agent-embedded'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of Expand from a JSON string"""
        return cls(json.loads(json_str))


