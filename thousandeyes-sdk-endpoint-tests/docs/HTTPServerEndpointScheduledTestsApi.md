# thousandeyes_sdk.endpoint_tests.HTTPServerEndpointScheduledTestsApi

All URIs are relative to *https://api.thousandeyes.com/v7*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_delete_http_server_endpoint_scheduled_tests**](HTTPServerEndpointScheduledTestsApi.md#bulk_delete_http_server_endpoint_scheduled_tests) | **DELETE** /endpoint/tests/scheduled-tests/http-server | Bulk delete HTTP server endpoint scheduled tests
[**create_http_server_endpoint_scheduled_test**](HTTPServerEndpointScheduledTestsApi.md#create_http_server_endpoint_scheduled_test) | **POST** /endpoint/tests/scheduled-tests/http-server | Create HTTP server endpoint scheduled test
[**delete_http_server_endpoint_scheduled_test**](HTTPServerEndpointScheduledTestsApi.md#delete_http_server_endpoint_scheduled_test) | **DELETE** /endpoint/tests/scheduled-tests/http-server/{testId} | Delete HTTP server scheduled test
[**get_http_server_endpoint_scheduled_test**](HTTPServerEndpointScheduledTestsApi.md#get_http_server_endpoint_scheduled_test) | **GET** /endpoint/tests/scheduled-tests/http-server/{testId} | Retrieves HTTP server endpoint scheduled test
[**get_http_server_endpoint_scheduled_tests**](HTTPServerEndpointScheduledTestsApi.md#get_http_server_endpoint_scheduled_tests) | **GET** /endpoint/tests/scheduled-tests/http-server | List HTTP server endpoint scheduled tests
[**update_http_server_endpoint_scheduled_test**](HTTPServerEndpointScheduledTestsApi.md#update_http_server_endpoint_scheduled_test) | **PATCH** /endpoint/tests/scheduled-tests/http-server/{testId} | Update HTTP server endpoint scheduled test


# **bulk_delete_http_server_endpoint_scheduled_tests**
> EndpointTestBulkDeleteResult bulk_delete_http_server_endpoint_scheduled_tests(test_id, aid=aid)

Bulk delete HTTP server endpoint scheduled tests

Deletes multiple HTTP server endpoint scheduled tests in one all-or-nothing operation. Missing test IDs are ignored.  Before any tests are deleted, all found tests are validated to ensure they belong to this test family and can be deleted by the caller or, for partner-owned tests, by the owning partner. If any validation check fails, no tests are deleted. 

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.endpoint_tests
from thousandeyes_sdk.endpoint_tests.models.endpoint_test_bulk_delete_result import EndpointTestBulkDeleteResult
from thousandeyes_sdk.endpoint_tests.rest import ApiException
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
    api_instance = thousandeyes_sdk.endpoint_tests.HTTPServerEndpointScheduledTestsApi(api_client)
    test_id = ["4503599627370497","4503599627370498"] # List[str] | Endpoint test IDs to delete. Specify this parameter once for each test ID. The request must not contain more than the maximum number of tests supported by the operation. If the limit is exceeded, the `400 Bad Request` response includes the supported maximum in `maximumTestsSupported`.
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Bulk delete HTTP server endpoint scheduled tests
        api_response = api_instance.bulk_delete_http_server_endpoint_scheduled_tests(test_id, aid=aid)
        print("The response of HTTPServerEndpointScheduledTestsApi->bulk_delete_http_server_endpoint_scheduled_tests:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HTTPServerEndpointScheduledTestsApi->bulk_delete_http_server_endpoint_scheduled_tests: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_id** | [**List[str]**](str.md)| Endpoint test IDs to delete. Specify this parameter once for each test ID. The request must not contain more than the maximum number of tests supported by the operation. If the limit is exceeded, the &#x60;400 Bad Request&#x60; response includes the supported maximum in &#x60;maximumTestsSupported&#x60;. | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

[**EndpointTestBulkDeleteResult**](EndpointTestBulkDeleteResult.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The IDs of tests successfully deleted. |  -  |
**400** | The request is invalid. Missing test IDs are ignored. Each test that is found must belong to the endpoint test family addressed by the operation and must be deletable by the caller or owning partner. If any validation check fails, no tests are deleted. When the request exceeds the bulk-delete limit, the response includes the maximum number of tests supported by the operation. |  -  |
**401** | Unauthorized |  -  |
**403** | Insufficient permissions to query endpoint |  -  |
**429** | Exhausted rate limit for the organization |  -  |
**500** | Internal server error |  -  |
**502** | Bad Gateway |  -  |
**0** | An error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_http_server_endpoint_scheduled_test**
> EndpointHttpServerTest create_http_server_endpoint_scheduled_test(endpoint_http_server_test_request, aid=aid)

Create HTTP server endpoint scheduled test

Creates a new HTTP server endpoint test in ThousandEyes, using properties specified in the POST data. Please note that only users with Account Admin privileges have the authorization to create new tests; regular users are restricted from using POST-based methods. 

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.endpoint_tests
from thousandeyes_sdk.endpoint_tests.models.endpoint_http_server_test import EndpointHttpServerTest
from thousandeyes_sdk.endpoint_tests.models.endpoint_http_server_test_request import EndpointHttpServerTestRequest
from thousandeyes_sdk.endpoint_tests.rest import ApiException
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
    api_instance = thousandeyes_sdk.endpoint_tests.HTTPServerEndpointScheduledTestsApi(api_client)
    endpoint_http_server_test_request = thousandeyes_sdk.endpoint_tests.EndpointHttpServerTestRequest() # EndpointHttpServerTestRequest | 
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Create HTTP server endpoint scheduled test
        api_response = api_instance.create_http_server_endpoint_scheduled_test(endpoint_http_server_test_request, aid=aid)
        print("The response of HTTPServerEndpointScheduledTestsApi->create_http_server_endpoint_scheduled_test:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HTTPServerEndpointScheduledTestsApi->create_http_server_endpoint_scheduled_test: %s\n" % e)
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

# **delete_http_server_endpoint_scheduled_test**
> delete_http_server_endpoint_scheduled_test(test_id, aid=aid)

Delete HTTP server scheduled test

Deletes an HTTP server endpoint scheduled test.

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.endpoint_tests
from thousandeyes_sdk.endpoint_tests.rest import ApiException
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
    api_instance = thousandeyes_sdk.endpoint_tests.HTTPServerEndpointScheduledTestsApi(api_client)
    test_id = '584739201' # str | Unique ID of endpoint test.
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Delete HTTP server scheduled test
        api_instance.delete_http_server_endpoint_scheduled_test(test_id, aid=aid)
    except Exception as e:
        print("Exception when calling HTTPServerEndpointScheduledTestsApi->delete_http_server_endpoint_scheduled_test: %s\n" % e)
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
 - **Accept**: application/json, application/problem+json

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

# **get_http_server_endpoint_scheduled_test**
> EndpointHttpServerTest get_http_server_endpoint_scheduled_test(test_id, aid=aid)

Retrieves HTTP server endpoint scheduled test

Retrieves details of an HTTP Server endpoint scheduled test.

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.endpoint_tests
from thousandeyes_sdk.endpoint_tests.models.endpoint_http_server_test import EndpointHttpServerTest
from thousandeyes_sdk.endpoint_tests.rest import ApiException
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
    api_instance = thousandeyes_sdk.endpoint_tests.HTTPServerEndpointScheduledTestsApi(api_client)
    test_id = '584739201' # str | Unique ID of endpoint test.
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Retrieves HTTP server endpoint scheduled test
        api_response = api_instance.get_http_server_endpoint_scheduled_test(test_id, aid=aid)
        print("The response of HTTPServerEndpointScheduledTestsApi->get_http_server_endpoint_scheduled_test:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HTTPServerEndpointScheduledTestsApi->get_http_server_endpoint_scheduled_test: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_id** | **str**| Unique ID of endpoint test. | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

[**EndpointHttpServerTest**](EndpointHttpServerTest.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json, application/json, application/problem+json

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

# **get_http_server_endpoint_scheduled_tests**
> EndpointHttpServerTests get_http_server_endpoint_scheduled_tests(aid=aid)

List HTTP server endpoint scheduled tests

Returns a list of agent to server endpoint scheduled tests configured in ThousandEyes. This list does not contain saved events.  **Note**: **Saved Events** are now called **Private Snapshots** in the user interface. This change does not affect API. 

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.endpoint_tests
from thousandeyes_sdk.endpoint_tests.models.endpoint_http_server_tests import EndpointHttpServerTests
from thousandeyes_sdk.endpoint_tests.rest import ApiException
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
    api_instance = thousandeyes_sdk.endpoint_tests.HTTPServerEndpointScheduledTestsApi(api_client)
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # List HTTP server endpoint scheduled tests
        api_response = api_instance.get_http_server_endpoint_scheduled_tests(aid=aid)
        print("The response of HTTPServerEndpointScheduledTestsApi->get_http_server_endpoint_scheduled_tests:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HTTPServerEndpointScheduledTestsApi->get_http_server_endpoint_scheduled_tests: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

[**EndpointHttpServerTests**](EndpointHttpServerTests.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json, application/json, application/problem+json

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

# **update_http_server_endpoint_scheduled_test**
> EndpointHttpServerTest update_http_server_endpoint_scheduled_test(test_id, endpoint_http_test_update, aid=aid)

Update HTTP server endpoint scheduled test

Updates an HTTP server scheduled test. Includes support for  enabling and disabling the test.

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.endpoint_tests
from thousandeyes_sdk.endpoint_tests.models.endpoint_http_server_test import EndpointHttpServerTest
from thousandeyes_sdk.endpoint_tests.models.endpoint_http_test_update import EndpointHttpTestUpdate
from thousandeyes_sdk.endpoint_tests.rest import ApiException
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
    api_instance = thousandeyes_sdk.endpoint_tests.HTTPServerEndpointScheduledTestsApi(api_client)
    test_id = '584739201' # str | Unique ID of endpoint test.
    endpoint_http_test_update = thousandeyes_sdk.endpoint_tests.EndpointHttpTestUpdate() # EndpointHttpTestUpdate | 
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Update HTTP server endpoint scheduled test
        api_response = api_instance.update_http_server_endpoint_scheduled_test(test_id, endpoint_http_test_update, aid=aid)
        print("The response of HTTPServerEndpointScheduledTestsApi->update_http_server_endpoint_scheduled_test:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HTTPServerEndpointScheduledTestsApi->update_http_server_endpoint_scheduled_test: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_id** | **str**| Unique ID of endpoint test. | 
 **endpoint_http_test_update** | [**EndpointHttpTestUpdate**](EndpointHttpTestUpdate.md)|  | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

[**EndpointHttpServerTest**](EndpointHttpServerTest.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json, application/json, application/problem+json

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

