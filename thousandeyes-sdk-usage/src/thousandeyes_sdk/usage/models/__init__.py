# coding: utf-8

# flake8: noqa
"""
    Usage API

     These usage endpoints define the following operations:  * **Usage**: Retrieve usage data for the specified time period (default is one month).          * Users must have the `View organization usage` permission to access this endpoint.     * This endpoint offers visibility across all account groups within the organization.     * Users with `View organization usage` permission in multiple organizations should query the endpoint with the `aid` query string parameter (see optional parameters) for each organization.  * **Quotas**: Obtain organization and account usage quotas. Additionally, users with the appropriate permissions can create, update, or delete these quotas.          * Users must have the necessary permissions to perform quota-related actions.  Refer to the Usage API endpoints for detailed usage instructions and optional parameters. 

    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


# import models into model package
from thousandeyes_sdk.usage.models.account_group_quota import AccountGroupQuota
from thousandeyes_sdk.usage.models.endpoint_agents_embedded import EndpointAgentsEmbedded
from thousandeyes_sdk.usage.models.endpoint_agents_essentials import EndpointAgentsEssentials
from thousandeyes_sdk.usage.models.endpoint_agents_usage import EndpointAgentsUsage
from thousandeyes_sdk.usage.models.enterprise_agent_units import EnterpriseAgentUnits
from thousandeyes_sdk.usage.models.enterprise_agent_units_by_test_owner_account_group import EnterpriseAgentUnitsByTestOwnerAccountGroup
from thousandeyes_sdk.usage.models.enterprise_agents import EnterpriseAgents
from thousandeyes_sdk.usage.models.enterprise_agents_usage import EnterpriseAgentsUsage
from thousandeyes_sdk.usage.models.error import Error
from thousandeyes_sdk.usage.models.expand_usage_options import ExpandUsageOptions
from thousandeyes_sdk.usage.models.link import Link
from thousandeyes_sdk.usage.models.organization_quota import OrganizationQuota
from thousandeyes_sdk.usage.models.organization_quota_assignment import OrganizationQuotaAssignment
from thousandeyes_sdk.usage.models.organization_quota_unassignment import OrganizationQuotaUnassignment
from thousandeyes_sdk.usage.models.organizations_quotas_assign import OrganizationsQuotasAssign
from thousandeyes_sdk.usage.models.organizations_quotas_unassign import OrganizationsQuotasUnassign
from thousandeyes_sdk.usage.models.pagination_links import PaginationLinks
from thousandeyes_sdk.usage.models.quota import Quota
from thousandeyes_sdk.usage.models.quotas import Quotas
from thousandeyes_sdk.usage.models.quotas_assign_request import QuotasAssignRequest
from thousandeyes_sdk.usage.models.quotas_assign_response import QuotasAssignResponse
from thousandeyes_sdk.usage.models.quotas_unassign import QuotasUnassign
from thousandeyes_sdk.usage.models.self_links import SelfLinks
from thousandeyes_sdk.usage.models.test_usage import TestUsage
from thousandeyes_sdk.usage.models.tests_usage import TestsUsage
from thousandeyes_sdk.usage.models.unauthorized_error import UnauthorizedError
from thousandeyes_sdk.usage.models.units_by_tests import UnitsByTests
from thousandeyes_sdk.usage.models.usage import Usage
from thousandeyes_sdk.usage.models.usage_details import UsageDetails
from thousandeyes_sdk.usage.models.usage_quota import UsageQuota
from thousandeyes_sdk.usage.models.validation_error import ValidationError
from thousandeyes_sdk.usage.models.validation_error_item import ValidationErrorItem
