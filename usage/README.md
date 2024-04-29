# usage

These usage endpoints define the following operations:

* **Usage**: Retrieve usage data for the specified time period (default is one month).
    
    * Users must have the `View Billing` permission to access this endpoint.
    * This endpoint offers visibility across all account groups within the organization.
    * Users with `View Billing` permission in multiple organizations should query the endpoint with the `aid` query string parameter (see optional parameters) for each organization.

* **Quotas**: Obtain organization and account usage quotas. Additionally, users with the appropriate permissions can create, update, or delete these quotas.
    
    * Users must have the necessary permissions to perform quota-related actions.

Refer to the Usage API endpoints for detailed usage instructions and optional parameters.


This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 7.0.2
- Package version: 1.0.0
- Generator version: 7.5.0
- Build package: com.thousandeyes.api.codegen.ThousandeyesPythonGenerator

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import usage
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import usage
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import usage
from usage.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.thousandeyes.com
# See configuration.py for a list of all supported configuration parameters.
configuration = usage.Configuration(
    host = "https://api.thousandeyes.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = usage.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)


# Enter a context with an instance of the API client
with usage.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = usage.QuotasApi(api_client)
    organizations_quotas_assign = usage.OrganizationsQuotasAssign() # OrganizationsQuotasAssign |  (optional)

    try:
        # Create or update accout group quotas
        api_response = api_instance.assign_organizations_account_groups_quotas(organizations_quotas_assign=organizations_quotas_assign)
        print("The response of QuotasApi->assign_organizations_account_groups_quotas:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling QuotasApi->assign_organizations_account_groups_quotas: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.thousandeyes.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*QuotasApi* | [**assign_organizations_account_groups_quotas**](docs/QuotasApi.md#assign_organizations_account_groups_quotas) | **POST** /v7/quotas/account-groups/assign | Create or update accout group quotas
*QuotasApi* | [**assign_organizations_quotas**](docs/QuotasApi.md#assign_organizations_quotas) | **POST** /v7/quotas/assign | Create or update organizations quotas
*QuotasApi* | [**get_quotas**](docs/QuotasApi.md#get_quotas) | **GET** /v7/quotas | Get organization and account group usage quota
*QuotasApi* | [**unassign_organizations_account_groups_quotas**](docs/QuotasApi.md#unassign_organizations_account_groups_quotas) | **POST** /v7/quotas/account-groups/unassign | Remove account group quotas from organizations
*QuotasApi* | [**unassign_organizations_quotas**](docs/QuotasApi.md#unassign_organizations_quotas) | **POST** /v7/quotas/unassign | Remove organization quotas
*UsageApi* | [**get_enterprise_agents_units_usage**](docs/UsageApi.md#get_enterprise_agents_units_usage) | **GET** /v7/usage/units/enterprise-agents | Get enterprise agent usage
*UsageApi* | [**get_test_units_usage**](docs/UsageApi.md#get_test_units_usage) | **GET** /v7/usage/units/tests | Get cloud and enterprise agents units usage
*UsageApi* | [**get_usage**](docs/UsageApi.md#get_usage) | **GET** /v7/usage | Get usage information for the last month


## Documentation For Models

 - [AccountGroup](docs/AccountGroup.md)
 - [AccountGroupId](docs/AccountGroupId.md)
 - [AccountGroupQuota](docs/AccountGroupQuota.md)
 - [EndpointAgentsEmbeddedInner](docs/EndpointAgentsEmbeddedInner.md)
 - [EndpointAgentsEssentialsInner](docs/EndpointAgentsEssentialsInner.md)
 - [EndpointAgentsInner](docs/EndpointAgentsInner.md)
 - [EnterpriseAgentUnitsByTestOwnerAccountGroup](docs/EnterpriseAgentUnitsByTestOwnerAccountGroup.md)
 - [EnterpriseAgentUnitsByTestOwnerAccountGroupBreakdownsInner](docs/EnterpriseAgentUnitsByTestOwnerAccountGroupBreakdownsInner.md)
 - [EnterpriseAgentUnitsInner](docs/EnterpriseAgentUnitsInner.md)
 - [EnterpriseAgentsInner](docs/EnterpriseAgentsInner.md)
 - [Error](docs/Error.md)
 - [Expand](docs/Expand.md)
 - [GetEnterpriseAgentsUnitsUsage200Response](docs/GetEnterpriseAgentsUnitsUsage200Response.md)
 - [GetQuotas200Response](docs/GetQuotas200Response.md)
 - [GetTestUnitsUsage200Response](docs/GetTestUnitsUsage200Response.md)
 - [GetUsage200Response](docs/GetUsage200Response.md)
 - [Link](docs/Link.md)
 - [OrganizationQuota](docs/OrganizationQuota.md)
 - [OrganizationsQuotasAssign](docs/OrganizationsQuotasAssign.md)
 - [OrganizationsQuotasAssignOrganizationsInner](docs/OrganizationsQuotasAssignOrganizationsInner.md)
 - [OrganizationsQuotasUnassign](docs/OrganizationsQuotasUnassign.md)
 - [OrganizationsQuotasUnassignOrganizationsInner](docs/OrganizationsQuotasUnassignOrganizationsInner.md)
 - [PaginationLinks](docs/PaginationLinks.md)
 - [PaginationLinksLinks](docs/PaginationLinksLinks.md)
 - [Quotas](docs/Quotas.md)
 - [QuotasAssignRequest](docs/QuotasAssignRequest.md)
 - [QuotasAssignResponse](docs/QuotasAssignResponse.md)
 - [QuotasQuotasInner](docs/QuotasQuotasInner.md)
 - [QuotasUnassign](docs/QuotasUnassign.md)
 - [SelfLinks](docs/SelfLinks.md)
 - [SelfLinksLinks](docs/SelfLinksLinks.md)
 - [TestsInner](docs/TestsInner.md)
 - [UnauthorizedError](docs/UnauthorizedError.md)
 - [UnitsByTests](docs/UnitsByTests.md)
 - [UnitsByTestsBreakdownsInner](docs/UnitsByTestsBreakdownsInner.md)
 - [Usage](docs/Usage.md)
 - [UsageUsage](docs/UsageUsage.md)
 - [UsageUsageQuota](docs/UsageUsageQuota.md)
 - [ValidationError](docs/ValidationError.md)
 - [ValidationErrorAllOfErrors](docs/ValidationErrorAllOfErrors.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="BearerAuth"></a>
### BearerAuth

- **Type**: Bearer authentication


## Author



