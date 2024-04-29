# tests.AllTestTypesApi

All URIs are relative to *https://api.thousandeyes.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_tests**](AllTestTypesApi.md#get_tests) | **GET** /v7/tests | List configured tests


# **get_tests**
> GetTests200Response get_tests(aid=aid)

List configured tests

Returns configured tests and saved events.

### Example

* Bearer Authentication (BearerAuth):

```python
import tests
from tests.models.get_tests200_response import GetTests200Response
from tests.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.thousandeyes.com
# See configuration.py for a list of all supported configuration parameters.
configuration = tests.Configuration(
    host = "https://api.thousandeyes.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = tests.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tests.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tests.AllTestTypesApi(api_client)
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # List configured tests
        api_response = api_instance.get_tests(aid=aid)
        print("The response of AllTestTypesApi->get_tests:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AllTestTypesApi->get_tests: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

[**GetTests200Response**](GetTests200Response.md)

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
**502** | Bad Gateway |  -  |
**0** | An error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

