# thousandeyes_sdk.endpoint_tests.DynamicTestsAgentToServerApi

All URIs are relative to *https://api.thousandeyes.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_endpoint_dynamic_test**](DynamicTestsAgentToServerApi.md#delete_endpoint_dynamic_test) | **DELETE** /v7/endpoint/tests/dynamic-tests/agent-to-server/{testId} | Delete agent to server dynamic test
[**get_dynamic_test_detail**](DynamicTestsAgentToServerApi.md#get_dynamic_test_detail) | **GET** /v7/endpoint/tests/dynamic-tests/agent-to-server/{testId} | Retrieve endpoint dynamic test
[**get_dynamic_tests_list**](DynamicTestsAgentToServerApi.md#get_dynamic_tests_list) | **GET** /v7/endpoint/tests/dynamic-tests/agent-to-server | List endpoint dynamic tests
[**post_dynamic_test**](DynamicTestsAgentToServerApi.md#post_dynamic_test) | **POST** /v7/endpoint/tests/dynamic-tests/agent-to-server | Create endpoint dynamic test
[**update_endpoint_dynamic_test_detail**](DynamicTestsAgentToServerApi.md#update_endpoint_dynamic_test_detail) | **PATCH** /v7/endpoint/tests/dynamic-tests/agent-to-server/{testId} | Update agent to server dynamic test


# **delete_endpoint_dynamic_test**
> delete_endpoint_dynamic_test(test_id, aid=aid)

Delete agent to server dynamic test

Deletes an agent to server endpoint dynamic test.

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.endpoint_tests
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
    api_instance = thousandeyes_sdk.endpoint_tests.DynamicTestsAgentToServerApi(api_client)
    test_id = '584739201' # str | Unique ID of endpoint test.
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Delete agent to server dynamic test
        api_instance.delete_endpoint_dynamic_test(test_id, aid=aid)
    except Exception as e:
        print("Exception when calling DynamicTestsAgentToServerApi->delete_endpoint_dynamic_test: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_id** | **str**| Unique ID of endpoint test. | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No content |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Insufficient permissions to query endpoint |  -  |
**404** | Not found |  -  |
**429** | Exhausted rate limit for the organization |  -  |
**500** | Internal server error |  -  |
**502** | Bad Gateway |  -  |
**0** | An error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dynamic_test_detail**
> DynamicTest get_dynamic_test_detail(test_id, aid=aid)

Retrieve endpoint dynamic test

Returns details of an endpoint dynamic test, including test type, name, intervals, targets.

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.endpoint_tests
from thousandeyes_sdk.endpoint_tests.models.dynamic_test import DynamicTest
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
    api_instance = thousandeyes_sdk.endpoint_tests.DynamicTestsAgentToServerApi(api_client)
    test_id = '584739201' # str | Unique ID of endpoint test.
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

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

[**DynamicTest**](DynamicTest.md)

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
> DynamicTests get_dynamic_tests_list(aid=aid)

List endpoint dynamic tests

Returns a list of all endpoint dynamic tests configured in ThousandEyes. This list does not contain saved events.

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.endpoint_tests
from thousandeyes_sdk.endpoint_tests.models.dynamic_tests import DynamicTests
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
    api_instance = thousandeyes_sdk.endpoint_tests.DynamicTestsAgentToServerApi(api_client)
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

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

[**DynamicTests**](DynamicTests.md)

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
import thousandeyes_sdk.endpoint_tests
from thousandeyes_sdk.endpoint_tests.models.dynamic_test import DynamicTest
from thousandeyes_sdk.endpoint_tests.models.dynamic_test_request import DynamicTestRequest
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
    api_instance = thousandeyes_sdk.endpoint_tests.DynamicTestsAgentToServerApi(api_client)
    dynamic_test_request = thousandeyes_sdk.endpoint_tests.DynamicTestRequest() # DynamicTestRequest | 
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

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

# **update_endpoint_dynamic_test_detail**
> DynamicTest update_endpoint_dynamic_test_detail(test_id, endpoint_dynamic_test_update, aid=aid)

Update agent to server dynamic test

Updates an agent to server endpoint dynamic test. Includes support for  enabling and disabling the test.

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.endpoint_tests
from thousandeyes_sdk.endpoint_tests.models.dynamic_test import DynamicTest
from thousandeyes_sdk.endpoint_tests.models.endpoint_dynamic_test_update import EndpointDynamicTestUpdate
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
    api_instance = thousandeyes_sdk.endpoint_tests.DynamicTestsAgentToServerApi(api_client)
    test_id = '584739201' # str | Unique ID of endpoint test.
    endpoint_dynamic_test_update = thousandeyes_sdk.endpoint_tests.EndpointDynamicTestUpdate() # EndpointDynamicTestUpdate | 
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Update agent to server dynamic test
        api_response = api_instance.update_endpoint_dynamic_test_detail(test_id, endpoint_dynamic_test_update, aid=aid)
        print("The response of DynamicTestsAgentToServerApi->update_endpoint_dynamic_test_detail:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DynamicTestsAgentToServerApi->update_endpoint_dynamic_test_detail: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_id** | **str**| Unique ID of endpoint test. | 
 **endpoint_dynamic_test_update** | [**EndpointDynamicTestUpdate**](EndpointDynamicTestUpdate.md)|  | 
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
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Insufficient permissions to query endpoint |  -  |
**404** | Not found |  -  |
**429** | Exhausted rate limit for the organization |  -  |
**500** | Internal server error |  -  |
**502** | Bad Gateway |  -  |
**0** | An error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

