# usage.QuotasApi

All URIs are relative to *https://api.thousandeyes.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assign_organizations_account_groups_quotas**](QuotasApi.md#assign_organizations_account_groups_quotas) | **POST** /v7/quotas/account-groups/assign | Create or update accout group quotas
[**assign_organizations_quotas**](QuotasApi.md#assign_organizations_quotas) | **POST** /v7/quotas/assign | Create or update organizations quotas
[**get_quotas**](QuotasApi.md#get_quotas) | **GET** /v7/quotas | Get organization and account group usage quota
[**unassign_organizations_account_groups_quotas**](QuotasApi.md#unassign_organizations_account_groups_quotas) | **POST** /v7/quotas/account-groups/unassign | Remove account group quotas from organizations
[**unassign_organizations_quotas**](QuotasApi.md#unassign_organizations_quotas) | **POST** /v7/quotas/unassign | Remove organization quotas


# **assign_organizations_account_groups_quotas**
> OrganizationsQuotasAssign assign_organizations_account_groups_quotas(organizations_quotas_assign=organizations_quotas_assign)

Create or update accout group quotas

This endpoint assigns quota values to multiple account groups across multiple organizations. To use this endpoint, you need the `Edit organization and account group quotas` permission, which is a management-level permission. This endpoint follows a cumulative behavior––This means that the quotas are assigned to the designated account groups, and any previous assignments remain in place without any unassignment occurring.

### Example

* Bearer Authentication (BearerAuth):

```python
import usage
from usage.models.organizations_quotas_assign import OrganizationsQuotasAssign
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
 - **Accept**: application/hal+json, application/problem+json

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

This endpoint recieves a list of organization quotas to create or update. If there's no specific `orgId` defined for a quota, it defaults to using the authenticated organization. To use this endpoint, you need the `Edit organization and account group quotas` permission, which is a management-level permission. This endpoint follows cumulative behavior––This means that the quotas are assigned to the specified organizations, and any previous assignments remain unchanged; no unassignments occur.

### Example

* Bearer Authentication (BearerAuth):

```python
import usage
from usage.models.quotas_assign_request import QuotasAssignRequest
from usage.models.quotas_assign_response import QuotasAssignResponse
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
    quotas_assign_request = usage.QuotasAssignRequest() # QuotasAssignRequest |  (optional)

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
 - **Accept**: application/hal+json, application/problem+json

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
> GetQuotas200Response get_quotas()

Get organization and account group usage quota

This endpoint retrieves usage quotas for both organization and account groups. To use this endpoint, you need the `Edit organization and account group quotas` permission, which is a management-level permission. If a user has quota update permission in multiple organizations, the API returns data from all such organizations.

### Example

* Bearer Authentication (BearerAuth):

```python
import usage
from usage.models.get_quotas200_response import GetQuotas200Response
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

[**GetQuotas200Response**](GetQuotas200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json, application/problem+json

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

This endpoint removes quotas from multiple account groups across multiple organizations. To use this endpoint, you need the `Edit organization and account group quotas` permission, which is a management-level permission.

### Example

* Bearer Authentication (BearerAuth):

```python
import usage
from usage.models.organizations_quotas_unassign import OrganizationsQuotasUnassign
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
    organizations_quotas_unassign = usage.OrganizationsQuotasUnassign() # OrganizationsQuotasUnassign |  (optional)

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
 - **Accept**: application/problem+json

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

This endpoint recieves a list of organization IDs to remove their current quota. To use this endpoint, you need the `Edit organization and account group quotas` permission, which is a management-level permission.

### Example

* Bearer Authentication (BearerAuth):

```python
import usage
from usage.models.quotas_unassign import QuotasUnassign
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
    quotas_unassign = usage.QuotasUnassign() # QuotasUnassign |  (optional)

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
 - **Accept**: application/problem+json

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
