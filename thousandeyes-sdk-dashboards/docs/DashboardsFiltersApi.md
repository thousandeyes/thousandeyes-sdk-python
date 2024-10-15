# thousandeyes_sdk.dashboards.DashboardsFiltersApi

All URIs are relative to *https://api.thousandeyes.com/v7*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_dashboard_filter**](DashboardsFiltersApi.md#create_dashboard_filter) | **POST** /dashboards/filters | Create dashboard filter
[**delete_dashboard_filter**](DashboardsFiltersApi.md#delete_dashboard_filter) | **DELETE** /dashboards/filters/{id} | Delete dashboard filter
[**get_dashboard_filter**](DashboardsFiltersApi.md#get_dashboard_filter) | **GET** /dashboards/filters/{id} | Get dashboard filter
[**get_dashboards_filters**](DashboardsFiltersApi.md#get_dashboards_filters) | **GET** /dashboards/filters | List dashboard filters
[**update_dashboard_filter**](DashboardsFiltersApi.md#update_dashboard_filter) | **PUT** /dashboards/filters/{id} | Update dashboard filter


# **create_dashboard_filter**
> ApiContextFilterResponse create_dashboard_filter(api_context_filter_request, aid=aid)

Create dashboard filter

Creates a new dashboard filter in your account group. To create a filter,  you must have one of the following permissions: * `Edit dashboard templates for all users in account group` permission (Account Admin). * `Edit own dashboard templates` permission (Regular User). 

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.dashboards
from thousandeyes_sdk.dashboards.models.api_context_filter_request import ApiContextFilterRequest
from thousandeyes_sdk.dashboards.models.api_context_filter_response import ApiContextFilterResponse
from thousandeyes_sdk.dashboards.rest import ApiException
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
    api_instance = thousandeyes_sdk.dashboards.DashboardsFiltersApi(api_client)
    api_context_filter_request = thousandeyes_sdk.dashboards.ApiContextFilterRequest() # ApiContextFilterRequest | Dashboard filter object to be created and saved
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Create dashboard filter
        api_response = api_instance.create_dashboard_filter(api_context_filter_request, aid=aid)
        print("The response of DashboardsFiltersApi->create_dashboard_filter:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardsFiltersApi->create_dashboard_filter: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_context_filter_request** | [**ApiContextFilterRequest**](ApiContextFilterRequest.md)| Dashboard filter object to be created and saved | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

[**ApiContextFilterResponse**](ApiContextFilterResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json, application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  * Location -  <br>  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Insufficient permissions to query endpoint |  -  |
**404** | Not found |  -  |
**429** | Exhausted rate limit for the organization |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dashboard_filter**
> delete_dashboard_filter(id, aid=aid)

Delete dashboard filter

Deletes a dashboard filter using the `filterId` provided in the request.    **Note**:   * Users with the `Edit dashboard templates for all users in account group` permission (Account Admin) can delete any dashboard filter.   * Users with the `Edit own dashboard templates` permission (Regular User) can only delete the dashboard filters they have created themselves. 

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.dashboards
from thousandeyes_sdk.dashboards.rest import ApiException
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
    api_instance = thousandeyes_sdk.dashboards.DashboardsFiltersApi(api_client)
    id = '65bc18e8f2073a4a469cd958' # str | Unique dashboard filter ID.
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Delete dashboard filter
        api_instance.delete_dashboard_filter(id, aid=aid)
    except Exception as e:
        print("Exception when calling DashboardsFiltersApi->delete_dashboard_filter: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique dashboard filter ID. | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **get_dashboard_filter**
> ApiContextFilterResponse get_dashboard_filter(id, aid=aid)

Get dashboard filter

Returns a list of data source filters and their metadata within the dashboard filter. 

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.dashboards
from thousandeyes_sdk.dashboards.models.api_context_filter_response import ApiContextFilterResponse
from thousandeyes_sdk.dashboards.rest import ApiException
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
    api_instance = thousandeyes_sdk.dashboards.DashboardsFiltersApi(api_client)
    id = '65bc18e8f2073a4a469cd958' # str | Unique dashboard filter ID.
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Get dashboard filter
        api_response = api_instance.get_dashboard_filter(id, aid=aid)
        print("The response of DashboardsFiltersApi->get_dashboard_filter:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardsFiltersApi->get_dashboard_filter: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique dashboard filter ID. | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

[**ApiContextFilterResponse**](ApiContextFilterResponse.md)

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

# **get_dashboards_filters**
> ApiContextFiltersResponse get_dashboards_filters(search_pattern=search_pattern, aid=aid)

List dashboard filters

Returns a list of dashboard filters and its context within your account group. 

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.dashboards
from thousandeyes_sdk.dashboards.models.api_context_filters_response import ApiContextFiltersResponse
from thousandeyes_sdk.dashboards.rest import ApiException
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
    api_instance = thousandeyes_sdk.dashboards.DashboardsFiltersApi(api_client)
    search_pattern = 'cea-filter' # str | Optional search pattern parameter to filter list of dashboard filters by either name or description values. (optional)
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # List dashboard filters
        api_response = api_instance.get_dashboards_filters(search_pattern=search_pattern, aid=aid)
        print("The response of DashboardsFiltersApi->get_dashboards_filters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardsFiltersApi->get_dashboards_filters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_pattern** | **str**| Optional search pattern parameter to filter list of dashboard filters by either name or description values. | [optional] 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

[**ApiContextFiltersResponse**](ApiContextFiltersResponse.md)

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

# **update_dashboard_filter**
> ApiContextFilterResponse update_dashboard_filter(id, api_context_filter_request, aid=aid)

Update dashboard filter

Updates an existing dashboard filter in your account group.                        **Note**:    * Users with the `Edit dashboard templates for all users in account group` permission (Account Admin) can update any dashboard filter.    * Users with the `Edit own dashboard templates` permission (Regular User) can only update the dashboard filters they have created themselves. 

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.dashboards
from thousandeyes_sdk.dashboards.models.api_context_filter_request import ApiContextFilterRequest
from thousandeyes_sdk.dashboards.models.api_context_filter_response import ApiContextFilterResponse
from thousandeyes_sdk.dashboards.rest import ApiException
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
    api_instance = thousandeyes_sdk.dashboards.DashboardsFiltersApi(api_client)
    id = '65bc18e8f2073a4a469cd958' # str | Unique dashboard filter ID.
    api_context_filter_request = thousandeyes_sdk.dashboards.ApiContextFilterRequest() # ApiContextFilterRequest | Updated dashboard filter context object
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Update dashboard filter
        api_response = api_instance.update_dashboard_filter(id, api_context_filter_request, aid=aid)
        print("The response of DashboardsFiltersApi->update_dashboard_filter:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardsFiltersApi->update_dashboard_filter: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique dashboard filter ID. | 
 **api_context_filter_request** | [**ApiContextFilterRequest**](ApiContextFilterRequest.md)| Updated dashboard filter context object | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

[**ApiContextFilterResponse**](ApiContextFilterResponse.md)

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

