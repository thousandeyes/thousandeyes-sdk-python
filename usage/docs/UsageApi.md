# usage.UsageApi

All URIs are relative to *https://api.thousandeyes.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_enterprise_agents_units_usage**](UsageApi.md#get_enterprise_agents_units_usage) | **GET** /v7/usage/units/enterprise-agents | Get enterprise agent usage
[**get_test_units_usage**](UsageApi.md#get_test_units_usage) | **GET** /v7/usage/units/tests | Get cloud and enterprise agents units usage
[**get_usage**](UsageApi.md#get_usage) | **GET** /v7/usage | Get usage information for the last month


# **get_enterprise_agents_units_usage**
> GetEnterpriseAgentsUnitsUsage200Response get_enterprise_agents_units_usage(start_date=start_date, end_date=end_date, cursor=cursor)

Get enterprise agent usage

This endpoint returns the organization's enterprise agents usage for a specific time period, or the curent billing cycle if no time period is specified. In the `/v7/usage` API, a shared entprise agent's usage is reported in the account group where the agent was created (i.e Primary Account Group).  However in this API, the shared agent's usage is distributed among all the account groups where the tests are running on the particular agent. This API is also only available to customers on usage based pricing model.

### Example

* Bearer Authentication (BearerAuth):

```python
import usage
from usage.models.get_enterprise_agents_units_usage200_response import GetEnterpriseAgentsUnitsUsage200Response
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
    api_instance = usage.UsageApi(api_client)
    start_date = '2022-07-17T22:00:54Z' # datetime | Use with the `endDate` parameter. Include the complete time (hours, minutes, and seconds) in UTC time zone, following the ISO 8601 date-time format. See the example for reference. Please note that this parameter can't be used with `window`. (optional)
    end_date = '2022-07-18T22:00:54Z' # datetime | Defaults to current time the request is made. Use with the `startDate` parameter. Include the complete time (hours, minutes, and seconds) in UTC time zone, following the ISO 8601 date-time format. See the example for reference. Please note that this parameter can't be used with `window`. (optional)
    cursor = 'cursor_example' # str | (Optional) Opaque cursor used for pagination. Clients should use `next` value from `_links` instead of this parameter. (optional)

    try:
        # Get enterprise agent usage
        api_response = api_instance.get_enterprise_agents_units_usage(start_date=start_date, end_date=end_date, cursor=cursor)
        print("The response of UsageApi->get_enterprise_agents_units_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsageApi->get_enterprise_agents_units_usage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**| Use with the &#x60;endDate&#x60; parameter. Include the complete time (hours, minutes, and seconds) in UTC time zone, following the ISO 8601 date-time format. See the example for reference. Please note that this parameter can&#39;t be used with &#x60;window&#x60;. | [optional] 
 **end_date** | **datetime**| Defaults to current time the request is made. Use with the &#x60;startDate&#x60; parameter. Include the complete time (hours, minutes, and seconds) in UTC time zone, following the ISO 8601 date-time format. See the example for reference. Please note that this parameter can&#39;t be used with &#x60;window&#x60;. | [optional] 
 **cursor** | **str**| (Optional) Opaque cursor used for pagination. Clients should use &#x60;next&#x60; value from &#x60;_links&#x60; instead of this parameter. | [optional] 

### Return type

[**GetEnterpriseAgentsUnitsUsage200Response**](GetEnterpriseAgentsUnitsUsage200Response.md)

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

# **get_test_units_usage**
> GetTestUnitsUsage200Response get_test_units_usage(aid=aid, start_date=start_date, end_date=end_date, cursor=cursor)

Get cloud and enterprise agents units usage

This endpoint returns the cloud and enterprise agents usage for all the tests for a specific time period, or the curent billing cycle if no time period is specified. In the `/v7/usage` API, an entprise agent's usage is reported in the account group where the agent was created (i.e Primary Account Group).  However in this API, the agent's usage is distributed among all the account groups where the tests are running on the particular agent. This API is also only available to customers on usage based pricing model.

### Example

* Bearer Authentication (BearerAuth):

```python
import usage
from usage.models.get_test_units_usage200_response import GetTestUnitsUsage200Response
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
    api_instance = usage.UsageApi(api_client)
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)
    start_date = '2022-07-17T22:00:54Z' # datetime | Use with the `endDate` parameter. Include the complete time (hours, minutes, and seconds) in UTC time zone, following the ISO 8601 date-time format. See the example for reference. Please note that this parameter can't be used with `window`. (optional)
    end_date = '2022-07-18T22:00:54Z' # datetime | Defaults to current time the request is made. Use with the `startDate` parameter. Include the complete time (hours, minutes, and seconds) in UTC time zone, following the ISO 8601 date-time format. See the example for reference. Please note that this parameter can't be used with `window`. (optional)
    cursor = 'cursor_example' # str | (Optional) Opaque cursor used for pagination. Clients should use `next` value from `_links` instead of this parameter. (optional)

    try:
        # Get cloud and enterprise agents units usage
        api_response = api_instance.get_test_units_usage(aid=aid, start_date=start_date, end_date=end_date, cursor=cursor)
        print("The response of UsageApi->get_test_units_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsageApi->get_test_units_usage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 
 **start_date** | **datetime**| Use with the &#x60;endDate&#x60; parameter. Include the complete time (hours, minutes, and seconds) in UTC time zone, following the ISO 8601 date-time format. See the example for reference. Please note that this parameter can&#39;t be used with &#x60;window&#x60;. | [optional] 
 **end_date** | **datetime**| Defaults to current time the request is made. Use with the &#x60;startDate&#x60; parameter. Include the complete time (hours, minutes, and seconds) in UTC time zone, following the ISO 8601 date-time format. See the example for reference. Please note that this parameter can&#39;t be used with &#x60;window&#x60;. | [optional] 
 **cursor** | **str**| (Optional) Opaque cursor used for pagination. Clients should use &#x60;next&#x60; value from &#x60;_links&#x60; instead of this parameter. | [optional] 

### Return type

[**GetTestUnitsUsage200Response**](GetTestUnitsUsage200Response.md)

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

# **get_usage**
> GetUsage200Response get_usage(aid=aid, expand=expand)

Get usage information for the last month

This endpoint returns the organization's usage data for a specified time period. If no time period is specified, it defaults to the last month.   

### Example

* Bearer Authentication (BearerAuth):

```python
import usage
from usage.models.expand import Expand
from usage.models.get_usage200_response import GetUsage200Response
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
    api_instance = usage.UsageApi(api_client)
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)
    expand = [usage.Expand()] # List[Expand] | Expands the available resources. By default, no expansion takes place if the  `expand` query parameter is not passed. For example, to expand the \"tests\"  resource, pass the query '?expand=test'. (optional)

    try:
        # Get usage information for the last month
        api_response = api_instance.get_usage(aid=aid, expand=expand)
        print("The response of UsageApi->get_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsageApi->get_usage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 
 **expand** | [**List[Expand]**](Expand.md)| Expands the available resources. By default, no expansion takes place if the  &#x60;expand&#x60; query parameter is not passed. For example, to expand the \&quot;tests\&quot;  resource, pass the query &#39;?expand&#x3D;test&#39;. | [optional] 

### Return type

[**GetUsage200Response**](GetUsage200Response.md)

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

