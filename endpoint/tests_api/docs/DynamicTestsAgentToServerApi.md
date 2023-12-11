# tests_api.DynamicTestsAgentToServerApi

All URIs are relative to *https://api.thousandeyes.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_dynamic_test_detail**](DynamicTestsAgentToServerApi.md#get_dynamic_test_detail) | **GET** /v7/endpoint/tests/dynamic-tests/agent-to-server/{testId} | Retrieve endpoint dynamic test
[**get_dynamic_tests_list**](DynamicTestsAgentToServerApi.md#get_dynamic_tests_list) | **GET** /v7/endpoint/tests/dynamic-tests/agent-to-server | List endpoint dynamic tests
[**post_dynamic_test**](DynamicTestsAgentToServerApi.md#post_dynamic_test) | **POST** /v7/endpoint/tests/dynamic-tests/agent-to-server | Create endpoint dynamic test


# **get_dynamic_test_detail**
> GetDynamicTestDetail200Response get_dynamic_test_detail(test_id, aid=aid)

Retrieve endpoint dynamic test

Returns details of an endpoint dynamic test, including test type, name, intervals, targets.

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import tests_api
from tests_api.models.get_dynamic_test_detail200_response import GetDynamicTestDetail200Response
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
    api_instance = tests_api.DynamicTestsAgentToServerApi(api_client)
    test_id = '584739201' # str | Unique ID of endpoint test.
    aid = '2067' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Retrieve endpoint dynamic test
        api_response = api_instance.get_dynamic_test_detail(test_id, aid=aid)
        print("The response of DynamicTestsAgentToServerApi->get_dynamic_test_detail:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DynamicTestsAgentToServerApi->get_dynamic_test_detail: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_id** | **str**| Unique ID of endpoint test. | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

[**GetDynamicTestDetail200Response**](GetDynamicTestDetail200Response.md)

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

# **get_dynamic_tests_list**
> GetDynamicTestsList200Response get_dynamic_tests_list(aid=aid)

List endpoint dynamic tests

Returns a list of all endpoint dynamic tests configured in ThousandEyes. This list does not contain saved events.

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import tests_api
from tests_api.models.get_dynamic_tests_list200_response import GetDynamicTestsList200Response
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
    api_instance = tests_api.DynamicTestsAgentToServerApi(api_client)
    aid = '2067' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # List endpoint dynamic tests
        api_response = api_instance.get_dynamic_tests_list(aid=aid)
        print("The response of DynamicTestsAgentToServerApi->get_dynamic_tests_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DynamicTestsAgentToServerApi->get_dynamic_tests_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

[**GetDynamicTestsList200Response**](GetDynamicTestsList200Response.md)

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

# **post_dynamic_test**
> DynamicTest post_dynamic_test(dynamic_test_request, aid=aid)

Create endpoint dynamic test

Create a new endpoint dynamic test in ThousandEyes using properties specified in the POST data. Please note that only Account Admins have the authorization to create new tests; regular users are restricted from using POST-based methods. 

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import tests_api
from tests_api.models.dynamic_test import DynamicTest
from tests_api.models.dynamic_test_request import DynamicTestRequest
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
    api_instance = tests_api.DynamicTestsAgentToServerApi(api_client)
    dynamic_test_request = tests_api.DynamicTestRequest() # DynamicTestRequest | 
    aid = '2067' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Create endpoint dynamic test
        api_response = api_instance.post_dynamic_test(dynamic_test_request, aid=aid)
        print("The response of DynamicTestsAgentToServerApi->post_dynamic_test:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DynamicTestsAgentToServerApi->post_dynamic_test: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dynamic_test_request** | [**DynamicTestRequest**](DynamicTestRequest.md)|  | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

[**DynamicTest**](DynamicTest.md)

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

