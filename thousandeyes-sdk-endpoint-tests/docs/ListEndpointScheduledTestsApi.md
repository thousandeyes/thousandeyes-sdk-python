# thousandeyes_sdk.endpoint_tests.ListEndpointScheduledTestsApi

All URIs are relative to *https://api.thousandeyes.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_endpoint_tests_list**](ListEndpointScheduledTestsApi.md#get_endpoint_tests_list) | **GET** /v7/endpoint/tests/scheduled-tests | List endpoint scheduled tests


# **get_endpoint_tests_list**
> EndpointTests get_endpoint_tests_list(aid=aid)

List endpoint scheduled tests

Returns a list of all endpoint scheduled tests configured in ThousandEyes. This list does not contain saved events.

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.endpoint_tests
from thousandeyes_sdk.endpoint_tests.models.endpoint_tests import EndpointTests
from thousandeyes_sdk.endpoint_tests.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.thousandeyes.com
# See configuration.py for a list of all supported configuration parameters.
configuration = thousandeyes_sdk.client.Configuration(
    host = "https://api.thousandeyes.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = thousandeyes_sdk.client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with thousandeyes_sdk.endpoint_tests.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = thousandeyes_sdk.endpoint_tests.ListEndpointScheduledTestsApi(api_client)
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # List endpoint scheduled tests
        api_response = api_instance.get_endpoint_tests_list(aid=aid)
        print("The response of ListEndpointScheduledTestsApi->get_endpoint_tests_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ListEndpointScheduledTestsApi->get_endpoint_tests_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

[**EndpointTests**](EndpointTests.md)

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
**429** | Exhausted rate limit for the organization |  -  |
**500** | Internal server error |  -  |
**502** | Bad Gateway |  -  |
**0** | An error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
