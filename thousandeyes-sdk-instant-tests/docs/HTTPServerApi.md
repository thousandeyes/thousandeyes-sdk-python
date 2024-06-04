# thousandeyes_sdk.instant_tests.HTTPServerApi

All URIs are relative to *https://api.thousandeyes.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_http_server_instant_test**](HTTPServerApi.md#create_http_server_instant_test) | **POST** /v7/tests/http-server/instant | Create HTTP server instant test


# **create_http_server_instant_test**
> HttpServerInstantTest create_http_server_instant_test(http_server_instant_test_request, aid=aid, expand=expand)

Create HTTP server instant test

Creates and runs a new HTTP server instant test.

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.instant_tests
from thousandeyes_sdk.instant_tests.models.expand import Expand
from thousandeyes_sdk.instant_tests.models.http_server_instant_test import HttpServerInstantTest
from thousandeyes_sdk.instant_tests.models.http_server_instant_test_request import HttpServerInstantTestRequest
from thousandeyes_sdk.instant_tests.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.thousandeyes.com
# See configuration.py for a list of all supported configuration parameters.
configuration = thousandeyes_sdk.core.Configuration(
    host = "https://api.thousandeyes.com"
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
with thousandeyes_sdk.instant_tests.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = thousandeyes_sdk.instant_tests.HTTPServerApi(api_client)
    http_server_instant_test_request = thousandeyes_sdk.instant_tests.HttpServerInstantTestRequest() # HttpServerInstantTestRequest | 
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)
    expand = [thousandeyes_sdk.instant_tests.Expand()] # List[Expand] | (Optional) Indicates if the test sub-resources should be expanded. Defaults to no expansion. To expand the `agents` sub-resource, use the query `?expand=agent`. (optional)

    try:
        # Create HTTP server instant test
        api_response = api_instance.create_http_server_instant_test(http_server_instant_test_request, aid=aid, expand=expand)
        print("The response of HTTPServerApi->create_http_server_instant_test:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HTTPServerApi->create_http_server_instant_test: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **http_server_instant_test_request** | [**HttpServerInstantTestRequest**](HttpServerInstantTestRequest.md)|  | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 
 **expand** | [**List[Expand]**](Expand.md)| (Optional) Indicates if the test sub-resources should be expanded. Defaults to no expansion. To expand the &#x60;agents&#x60; sub-resource, use the query &#x60;?expand&#x3D;agent&#x60;. | [optional] 

### Return type

[**HttpServerInstantTest**](HttpServerInstantTest.md)

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
**502** | Bad Gateway |  -  |
**0** | An error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

