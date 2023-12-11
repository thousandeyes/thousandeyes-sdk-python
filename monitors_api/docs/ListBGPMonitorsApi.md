# monitors_api.ListBGPMonitorsApi

All URIs are relative to *https://api.thousandeyes.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_bgp_monitors**](ListBGPMonitorsApi.md#get_bgp_monitors) | **GET** /v7/monitors | List BGP monitors


# **get_bgp_monitors**
> GetBGPMonitors200Response get_bgp_monitors(aid=aid)

List BGP monitors

Retrieves a list of BGP monitors available to your account in ThousandEyes, including public and private feeds.

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import monitors_api
from monitors_api.models.get_bgp_monitors200_response import GetBGPMonitors200Response
from monitors_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.thousandeyes.com
# See configuration.py for a list of all supported configuration parameters.
configuration = monitors_api.Configuration(
    host = "https://api.thousandeyes.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = monitors_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with monitors_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitors_api.ListBGPMonitorsApi(api_client)
    aid = '2067' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # List BGP monitors
        api_response = api_instance.get_bgp_monitors(aid=aid)
        print("The response of ListBGPMonitorsApi->get_bgp_monitors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ListBGPMonitorsApi->get_bgp_monitors: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

[**GetBGPMonitors200Response**](GetBGPMonitors200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Insufficient permissions to query endpoint |  -  |
**404** | Not found |  -  |
**429** | Exhausted rate limit for the organization |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

