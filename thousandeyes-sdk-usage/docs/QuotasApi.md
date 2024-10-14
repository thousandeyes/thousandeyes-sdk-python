# thousandeyes_sdk.usage.QuotasApi

All URIs are relative to *https://api.thousandeyes.com/v7*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assign_organizations_account_groups_quotas**](QuotasApi.md#assign_organizations_account_groups_quotas) | **POST** /quotas/account-groups/assign | Create or update accout group quotas
[**assign_organizations_quotas**](QuotasApi.md#assign_organizations_quotas) | **POST** /quotas/assign | Create or update organizations quotas
[**get_quotas**](QuotasApi.md#get_quotas) | **GET** /quotas | Get organization and account group usage quota
[**unassign_organizations_account_groups_quotas**](QuotasApi.md#unassign_organizations_account_groups_quotas) | **POST** /quotas/account-groups/unassign | Remove account group quotas from organizations
[**unassign_organizations_quotas**](QuotasApi.md#unassign_organizations_quotas) | **POST** /quotas/unassign | Remove organization quotas


# **assign_organizations_account_groups_quotas**
> OrganizationsQuotasAssign assign_organizations_account_groups_quotas(organizations_quotas_assign=organizations_quotas_assign)

Create or update accout group quotas

This operation assigns quota values to multiple account groups across multiple organizations. To use this endpoint, you need the `Edit organization and account group quotas` permission, which is a management-level permission. This operation follows a cumulative behavior––This means that the quotas are assigned to the designated account groups, and any previous assignments remain in place without any unassignment occurring.

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.usage
from thousandeyes_sdk.usage.models.organizations_quotas_assign import OrganizationsQuotasAssign
from thousandeyes_sdk.usage.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.thousandeyes.com/v7
# See configuration.py for a list of all supported configuration parameters.
configuration = thousandeyes_sdk.core.Configuration(
    host = "https://api.thousandeyes.com/v7"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = thousandeyes_sdk.core.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with thousandeyes_sdk.core.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = thousandeyes_sdk.usage.QuotasApi(api_client)
    organizations_quotas_assign = thousandeyes_sdk.usage.OrganizationsQuotasAssign() # OrganizationsQuotasAssign |  (optional)

    try:
        # Create or update accout group quotas
        api_response = api_instance.assign_organizations_account_groups_quotas(organizations_quotas_assign=organizations_quotas_assign)
        print("The response of QuotasApi->assign_organizations_account_groups_quotas:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotasApi->assign_organizations_account_groups_quotas: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizations_quotas_assign** | [**OrganizationsQuotasAssign**](OrganizationsQuotasAssign.md)|  | [optional] 

### Return type

[**OrganizationsQuotasAssign**](OrganizationsQuotasAssign.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json, application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Insufficient permissions to query endpoint |  -  |
**404** | Not found |  -  |
**429** | Exhausted rate limit for the organization |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assign_organizations_quotas**
> QuotasAssignResponse assign_organizations_quotas(quotas_assign_request=quotas_assign_request)

Create or update organizations quotas

This operation recieves a list of organization quotas to create or update. If there's no specific `orgId` defined for a quota, it defaults to using the authenticated organization. To use this endpoint, you need the `Edit organization and account group quotas` permission, which is a management-level permission. This operation follows cumulative behavior––This means that the quotas are assigned to the specified organizations, and any previous assignments remain unchanged; no unassignments occur.

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.usage
from thousandeyes_sdk.usage.models.quotas_assign_request import QuotasAssignRequest
from thousandeyes_sdk.usage.models.quotas_assign_response import QuotasAssignResponse
from thousandeyes_sdk.usage.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.thousandeyes.com/v7
# See configuration.py for a list of all supported configuration parameters.
configuration = thousandeyes_sdk.core.Configuration(
    host = "https://api.thousandeyes.com/v7"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = thousandeyes_sdk.core.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with thousandeyes_sdk.core.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = thousandeyes_sdk.usage.QuotasApi(api_client)
    quotas_assign_request = thousandeyes_sdk.usage.QuotasAssignRequest() # QuotasAssignRequest |  (optional)

    try:
        # Create or update organizations quotas
        api_response = api_instance.assign_organizations_quotas(quotas_assign_request=quotas_assign_request)
        print("The response of QuotasApi->assign_organizations_quotas:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotasApi->assign_organizations_quotas: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quotas_assign_request** | [**QuotasAssignRequest**](QuotasAssignRequest.md)|  | [optional] 

### Return type

[**QuotasAssignResponse**](QuotasAssignResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json, application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Insufficient permissions to query endpoint |  -  |
**404** | Not found |  -  |
**429** | Exhausted rate limit for the organization |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_quotas**
> Quotas get_quotas()

Get organization and account group usage quota

This operation retrieves usage quotas for both organization and account groups. To use this endpoint, you need the `Edit organization and account group quotas` permission, which is a management-level permission. If a user has quota update permission in multiple organizations, the API returns data from all such organizations.

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.usage
from thousandeyes_sdk.usage.models.quotas import Quotas
from thousandeyes_sdk.usage.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.thousandeyes.com/v7
# See configuration.py for a list of all supported configuration parameters.
configuration = thousandeyes_sdk.core.Configuration(
    host = "https://api.thousandeyes.com/v7"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = thousandeyes_sdk.core.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with thousandeyes_sdk.core.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = thousandeyes_sdk.usage.QuotasApi(api_client)

    try:
        # Get organization and account group usage quota
        api_response = api_instance.get_quotas()
        print("The response of QuotasApi->get_quotas:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotasApi->get_quotas: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Quotas**](Quotas.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json, application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Insufficient permissions to query endpoint |  -  |
**404** | Not found |  -  |
**429** | Exhausted rate limit for the organization |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unassign_organizations_account_groups_quotas**
> unassign_organizations_account_groups_quotas(organizations_quotas_unassign=organizations_quotas_unassign)

Remove account group quotas from organizations

This operation removes quotas from multiple account groups across multiple organizations. To use this endpoint, you need the `Edit organization and account group quotas` permission, which is a management-level permission.

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.usage
from thousandeyes_sdk.usage.models.organizations_quotas_unassign import OrganizationsQuotasUnassign
from thousandeyes_sdk.usage.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.thousandeyes.com/v7
# See configuration.py for a list of all supported configuration parameters.
configuration = thousandeyes_sdk.core.Configuration(
    host = "https://api.thousandeyes.com/v7"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = thousandeyes_sdk.core.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with thousandeyes_sdk.core.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = thousandeyes_sdk.usage.QuotasApi(api_client)
    organizations_quotas_unassign = thousandeyes_sdk.usage.OrganizationsQuotasUnassign() # OrganizationsQuotasUnassign |  (optional)

    try:
        # Remove account group quotas from organizations
        api_instance.unassign_organizations_account_groups_quotas(organizations_quotas_unassign=organizations_quotas_unassign)
    except Exception as e:
        print("Exception when calling QuotasApi->unassign_organizations_account_groups_quotas: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizations_quotas_unassign** | [**OrganizationsQuotasUnassign**](OrganizationsQuotasUnassign.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No content |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Insufficient permissions to query endpoint |  -  |
**404** | Not found |  -  |
**429** | Exhausted rate limit for the organization |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unassign_organizations_quotas**
> unassign_organizations_quotas(quotas_unassign=quotas_unassign)

Remove organization quotas

This operation recieves a list of organization IDs to remove their current quota. To use this endpoint, you need the `Edit organization and account group quotas` permission, which is a management-level permission.

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.usage
from thousandeyes_sdk.usage.models.quotas_unassign import QuotasUnassign
from thousandeyes_sdk.usage.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.thousandeyes.com/v7
# See configuration.py for a list of all supported configuration parameters.
configuration = thousandeyes_sdk.core.Configuration(
    host = "https://api.thousandeyes.com/v7"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = thousandeyes_sdk.core.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with thousandeyes_sdk.core.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = thousandeyes_sdk.usage.QuotasApi(api_client)
    quotas_unassign = thousandeyes_sdk.usage.QuotasUnassign() # QuotasUnassign |  (optional)

    try:
        # Remove organization quotas
        api_instance.unassign_organizations_quotas(quotas_unassign=quotas_unassign)
    except Exception as e:
        print("Exception when calling QuotasApi->unassign_organizations_quotas: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quotas_unassign** | [**QuotasUnassign**](QuotasUnassign.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No content |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Insufficient permissions to query endpoint |  -  |
**404** | Not found |  -  |
**429** | Exhausted rate limit for the organization |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

