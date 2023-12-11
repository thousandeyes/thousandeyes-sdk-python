# tests_api.ScheduledTestsHTTPServerApi

All URIs are relative to *https://api.thousandeyes.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_endpoint_httpserver_test_detail**](ScheduledTestsHTTPServerApi.md#get_endpoint_httpserver_test_detail) | **GET** /v7/endpoint/tests/scheduled-tests/http-server/{testId} | Retrieves HTTP server endpoint scheduled test
[**get_endpoint_httpserver_tests_list**](ScheduledTestsHTTPServerApi.md#get_endpoint_httpserver_tests_list) | **GET** /v7/endpoint/tests/scheduled-tests/http-server | List HTTP server endpoint scheduled tests
[**post_endpoint_httpserver_test**](ScheduledTestsHTTPServerApi.md#post_endpoint_httpserver_test) | **POST** /v7/endpoint/tests/scheduled-tests/http-server | Create HTTP server endpoint scheduled test


# **get_endpoint_httpserver_test_detail**
> GetEndpointHttpserverTestDetail200Response get_endpoint_httpserver_test_detail(test_id, aid=aid)

Retrieves HTTP server endpoint scheduled test

Retrieves details of an HTTP Server endpoint scheduled test.

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import tests_api
from tests_api.models.get_endpoint_httpserver_test_detail200_response import GetEndpointHttpserverTestDetail200Response
from tests_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.thousandeyes.com
# See configuration.py for a list of all supported configuration parameters.
configuration = tests_api.Configuration(
    host = "https://api.thousandeyes.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = tests_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tests_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tests_api.ScheduledTestsHTTPServerApi(api_client)
    test_id = '584739201' # str | Unique ID of endpoint test.
    aid = '2067' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Retrieves HTTP server endpoint scheduled test
        api_response = api_instance.get_endpoint_httpserver_test_detail(test_id, aid=aid)
        print("The response of ScheduledTestsHTTPServerApi->get_endpoint_httpserver_test_detail:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScheduledTestsHTTPServerApi->get_endpoint_httpserver_test_detail: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_id** | **str**| Unique ID of endpoint test. | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

[**GetEndpointHttpserverTestDetail200Response**](GetEndpointHttpserverTestDetail200Response.md)

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

# **get_endpoint_httpserver_tests_list**
> GetEndpointHttpserverTestsList200Response get_endpoint_httpserver_tests_list(aid=aid)

List HTTP server endpoint scheduled tests

Returns a list of agent to server endpoint scheduled tests configured in ThousandEyes. This list does not contain saved events. 

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import tests_api
from tests_api.models.get_endpoint_httpserver_tests_list200_response import GetEndpointHttpserverTestsList200Response
from tests_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.thousandeyes.com
# See configuration.py for a list of all supported configuration parameters.
configuration = tests_api.Configuration(
    host = "https://api.thousandeyes.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = tests_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tests_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tests_api.ScheduledTestsHTTPServerApi(api_client)
    aid = '2067' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # List HTTP server endpoint scheduled tests
        api_response = api_instance.get_endpoint_httpserver_tests_list(aid=aid)
        print("The response of ScheduledTestsHTTPServerApi->get_endpoint_httpserver_tests_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScheduledTestsHTTPServerApi->get_endpoint_httpserver_tests_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

[**GetEndpointHttpserverTestsList200Response**](GetEndpointHttpserverTestsList200Response.md)

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

# **post_endpoint_httpserver_test**
> EndpointHttpServerTest post_endpoint_httpserver_test(endpoint_http_server_test_request, aid=aid)

Create HTTP server endpoint scheduled test

Creates a new HTTP server endpoint test in ThousandEyes, using properties specified in the POST data. Please note that only users with Account Admin privileges have the authorization to create new tests; regular users are restricted from using POST-based methods. 

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import tests_api
from tests_api.models.endpoint_http_server_test import EndpointHttpServerTest
from tests_api.models.endpoint_http_server_test_request import EndpointHttpServerTestRequest
from tests_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.thousandeyes.com
# See configuration.py for a list of all supported configuration parameters.
configuration = tests_api.Configuration(
    host = "https://api.thousandeyes.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = tests_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tests_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tests_api.ScheduledTestsHTTPServerApi(api_client)
    endpoint_http_server_test_request = tests_api.EndpointHttpServerTestRequest() # EndpointHttpServerTestRequest | 
    aid = '2067' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Create HTTP server endpoint scheduled test
        api_response = api_instance.post_endpoint_httpserver_test(endpoint_http_server_test_request, aid=aid)
        print("The response of ScheduledTestsHTTPServerApi->post_endpoint_httpserver_test:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScheduledTestsHTTPServerApi->post_endpoint_httpserver_test: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint_http_server_test_request** | [**EndpointHttpServerTestRequest**](EndpointHttpServerTestRequest.md)|  | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

[**EndpointHttpServerTest**](EndpointHttpServerTest.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json, application/problem+json

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

