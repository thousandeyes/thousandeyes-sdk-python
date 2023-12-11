# usage_api.UsageApi

All URIs are relative to *https://api.thousandeyes.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_usage**](UsageApi.md#get_usage) | **GET** /v7/usage | Get usage information for the last month


# **get_usage**
> GetUsage200Response get_usage(aid=aid, expand=expand)

Get usage information for the last month

This endpoint returns the organization's usage data for a specified time period. If no time period is specified, it defaults to the last month.   

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import usage_api
from usage_api.models.expand import Expand
from usage_api.models.get_usage200_response import GetUsage200Response
from usage_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.thousandeyes.com
# See configuration.py for a list of all supported configuration parameters.
configuration = usage_api.Configuration(
    host = "https://api.thousandeyes.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = usage_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with usage_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = usage_api.UsageApi(api_client)
    aid = '2067' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)
    expand = [usage_api.Expand()] # List[Expand] | Expands the available resources. By default, no expansion takes place if the  `expand` query parameter is not passed. For example, to expand the \"tests\"  resource, pass the query '?expand=test'. (optional)

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

