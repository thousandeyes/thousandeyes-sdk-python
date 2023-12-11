# tests_api.ScheduledTestsAgentToServerApi

All URIs are relative to *https://api.thousandeyes.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_endpoint_agent_to_server_detail**](ScheduledTestsAgentToServerApi.md#get_endpoint_agent_to_server_detail) | **GET** /v7/endpoint/tests/scheduled-tests/agent-to-server/{testId} | Retrieve agent to server endpoint scheduled test
[**get_endpoint_agent_toserver_tests_list**](ScheduledTestsAgentToServerApi.md#get_endpoint_agent_toserver_tests_list) | **GET** /v7/endpoint/tests/scheduled-tests/agent-to-server | List agent to server endpoint scheduled tests
[**post_endpoint_agent_to_server_test**](ScheduledTestsAgentToServerApi.md#post_endpoint_agent_to_server_test) | **POST** /v7/endpoint/tests/scheduled-tests/agent-to-server | Creates agent to server endpoint scheduled test


# **get_endpoint_agent_to_server_detail**
> PostEndpointAgentToServerTest201Response get_endpoint_agent_to_server_detail(test_id, aid=aid)

Retrieve agent to server endpoint scheduled test

Retrieves details of an agent to server endpoint scheduled test.

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import tests_api
from tests_api.models.post_endpoint_agent_to_server_test201_response import PostEndpointAgentToServerTest201Response
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
    api_instance = tests_api.ScheduledTestsAgentToServerApi(api_client)
    test_id = '584739201' # str | Unique ID of endpoint test.
    aid = '2067' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Retrieve agent to server endpoint scheduled test
        api_response = api_instance.get_endpoint_agent_to_server_detail(test_id, aid=aid)
        print("The response of ScheduledTestsAgentToServerApi->get_endpoint_agent_to_server_detail:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScheduledTestsAgentToServerApi->get_endpoint_agent_to_server_detail: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_id** | **str**| Unique ID of endpoint test. | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

[**PostEndpointAgentToServerTest201Response**](PostEndpointAgentToServerTest201Response.md)

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

# **get_endpoint_agent_toserver_tests_list**
> GetEndpointAgentToserverTestsList200Response get_endpoint_agent_toserver_tests_list(aid=aid)

List agent to server endpoint scheduled tests

Returns a list of all agent to server endpoint scheduled tests configured in ThousandEyes. This list does not contain saved events. 

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import tests_api
from tests_api.models.get_endpoint_agent_toserver_tests_list200_response import GetEndpointAgentToserverTestsList200Response
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
    api_instance = tests_api.ScheduledTestsAgentToServerApi(api_client)
    aid = '2067' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # List agent to server endpoint scheduled tests
        api_response = api_instance.get_endpoint_agent_toserver_tests_list(aid=aid)
        print("The response of ScheduledTestsAgentToServerApi->get_endpoint_agent_toserver_tests_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScheduledTestsAgentToServerApi->get_endpoint_agent_toserver_tests_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

[**GetEndpointAgentToserverTestsList200Response**](GetEndpointAgentToserverTestsList200Response.md)

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

# **post_endpoint_agent_to_server_test**
> PostEndpointAgentToServerTest201Response post_endpoint_agent_to_server_test(endpoint_agent_to_server_test_request, aid=aid)

Creates agent to server endpoint scheduled test

Creates a new endpoint test in ThousandEyes using properties specified in the POST data. Please note that only Account Admins have the authorization to create new tests; regular users are restricted from using POST-based methods. 

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import tests_api
from tests_api.models.endpoint_agent_to_server_test_request import EndpointAgentToServerTestRequest
from tests_api.models.post_endpoint_agent_to_server_test201_response import PostEndpointAgentToServerTest201Response
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
    api_instance = tests_api.ScheduledTestsAgentToServerApi(api_client)
    endpoint_agent_to_server_test_request = tests_api.EndpointAgentToServerTestRequest() # EndpointAgentToServerTestRequest | 
    aid = '2067' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Creates agent to server endpoint scheduled test
        api_response = api_instance.post_endpoint_agent_to_server_test(endpoint_agent_to_server_test_request, aid=aid)
        print("The response of ScheduledTestsAgentToServerApi->post_endpoint_agent_to_server_test:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScheduledTestsAgentToServerApi->post_endpoint_agent_to_server_test: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint_agent_to_server_test_request** | [**EndpointAgentToServerTestRequest**](EndpointAgentToServerTestRequest.md)|  | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

[**PostEndpointAgentToServerTest201Response**](PostEndpointAgentToServerTest201Response.md)

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

