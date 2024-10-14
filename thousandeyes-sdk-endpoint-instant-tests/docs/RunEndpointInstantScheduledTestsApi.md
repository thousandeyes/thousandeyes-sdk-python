# thousandeyes_sdk.endpoint_instant_tests.RunEndpointInstantScheduledTestsApi

All URIs are relative to *https://api.thousandeyes.com/v7*

Method | HTTP request | Description
------------- | ------------- | -------------
[**run_endpoint_scheduled_instant_test**](RunEndpointInstantScheduledTestsApi.md#run_endpoint_scheduled_instant_test) | **POST** /endpoint/tests/scheduled-tests/{testId}/run | Run endpoint instant scheduled test


# **run_endpoint_scheduled_instant_test**
> EndpointRunScheduledInstantTestResult run_endpoint_scheduled_instant_test(test_id, aid=aid)

Run endpoint instant scheduled test

Runs an existing endpoint instant scheduled test in ThousandEyes.

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.endpoint_instant_tests
from thousandeyes_sdk.endpoint_instant_tests.models.endpoint_run_scheduled_instant_test_result import EndpointRunScheduledInstantTestResult
from thousandeyes_sdk.endpoint_instant_tests.rest import ApiException
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
    api_instance = thousandeyes_sdk.endpoint_instant_tests.RunEndpointInstantScheduledTestsApi(api_client)
    test_id = '765231567' # str | ID of the endpoint instant scheduled test to rerun
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Run endpoint instant scheduled test
        api_response = api_instance.run_endpoint_scheduled_instant_test(test_id, aid=aid)
        print("The response of RunEndpointInstantScheduledTestsApi->run_endpoint_scheduled_instant_test:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunEndpointInstantScheduledTestsApi->run_endpoint_scheduled_instant_test: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_id** | **str**| ID of the endpoint instant scheduled test to rerun | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

[**EndpointRunScheduledInstantTestResult**](EndpointRunScheduledInstantTestResult.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully reran the instant scheduled test. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Insufficient permissions to query endpoint |  -  |
**404** | Not found |  -  |
**429** | Exhausted rate limit for the organization |  -  |
**500** | Internal server error |  -  |
**502** | Bad Gateway |  -  |
**0** | An error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

