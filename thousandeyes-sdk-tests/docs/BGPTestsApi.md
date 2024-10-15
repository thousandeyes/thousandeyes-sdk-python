# thousandeyes_sdk.tests.BGPTestsApi

All URIs are relative to *https://api.thousandeyes.com/v7*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_bgp_test**](BGPTestsApi.md#create_bgp_test) | **POST** /tests/bgp | Create BGP test
[**delete_bgp_test**](BGPTestsApi.md#delete_bgp_test) | **DELETE** /tests/bgp/{testId} | Delete BGP test
[**get_bgp_test**](BGPTestsApi.md#get_bgp_test) | **GET** /tests/bgp/{testId} | Get BGP test
[**get_bgp_tests**](BGPTestsApi.md#get_bgp_tests) | **GET** /tests/bgp | List BGP tests
[**update_bgp_test**](BGPTestsApi.md#update_bgp_test) | **PUT** /tests/bgp/{testId} | Update BGP test


# **create_bgp_test**
> BgpTestResponse create_bgp_test(bgp_test_request, aid=aid, expand=expand)

Create BGP test

Creates a new BGP test. This method requires Account Admin permissions.

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.tests
from thousandeyes_sdk.tests.models.bgp_test_request import BgpTestRequest
from thousandeyes_sdk.tests.models.bgp_test_response import BgpTestResponse
from thousandeyes_sdk.tests.models.expand_bgp_test_options import ExpandBgpTestOptions
from thousandeyes_sdk.tests.rest import ApiException
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
    api_instance = thousandeyes_sdk.tests.BGPTestsApi(api_client)
    bgp_test_request = thousandeyes_sdk.tests.BgpTestRequest() # BgpTestRequest | 
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)
    expand = [thousandeyes_sdk.tests.ExpandBgpTestOptions()] # List[ExpandBgpTestOptions] | Optional parameter on whether or not to expand the test sub-resources. By default no expansion takes place if the query parameter is not present. To expand the `monitors` sub-resource, pass the `?expand=monitor` query. (optional)

    try:
        # Create BGP test
        api_response = api_instance.create_bgp_test(bgp_test_request, aid=aid, expand=expand)
        print("The response of BGPTestsApi->create_bgp_test:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BGPTestsApi->create_bgp_test: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bgp_test_request** | [**BgpTestRequest**](BgpTestRequest.md)|  | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 
 **expand** | [**List[ExpandBgpTestOptions]**](ExpandBgpTestOptions.md)| Optional parameter on whether or not to expand the test sub-resources. By default no expansion takes place if the query parameter is not present. To expand the &#x60;monitors&#x60; sub-resource, pass the &#x60;?expand&#x3D;monitor&#x60; query. | [optional] 

### Return type

[**BgpTestResponse**](BgpTestResponse.md)

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

# **delete_bgp_test**
> delete_bgp_test(test_id, aid=aid)

Delete BGP test

Deletes a BGP test. This method requires Account Admin permissions.

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.tests
from thousandeyes_sdk.tests.rest import ApiException
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
    api_instance = thousandeyes_sdk.tests.BGPTestsApi(api_client)
    test_id = '202701' # str | Test ID
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Delete BGP test
        api_instance.delete_bgp_test(test_id, aid=aid)
    except Exception as e:
        print("Exception when calling BGPTestsApi->delete_bgp_test: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_id** | **str**| Test ID | 
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
**401** | Unauthorized |  -  |
**403** | Insufficient permissions to query endpoint |  -  |
**404** | Not found |  -  |
**429** | Exhausted rate limit for the organization |  -  |
**500** | Internal server error |  -  |
**502** | Bad Gateway |  -  |
**0** | An error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bgp_test**
> BgpTestResponse get_bgp_test(test_id, aid=aid, expand=expand)

Get BGP test

Returns details for a BGP test, including name, intervals, targets, alert rules and agents.

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.tests
from thousandeyes_sdk.tests.models.bgp_test_response import BgpTestResponse
from thousandeyes_sdk.tests.models.expand_bgp_test_options import ExpandBgpTestOptions
from thousandeyes_sdk.tests.rest import ApiException
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
    api_instance = thousandeyes_sdk.tests.BGPTestsApi(api_client)
    test_id = '202701' # str | Test ID
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)
    expand = [thousandeyes_sdk.tests.ExpandBgpTestOptions()] # List[ExpandBgpTestOptions] | Optional parameter on whether or not to expand the test sub-resources. By default no expansion takes place if the query parameter is not present. To expand the `monitors` sub-resource, pass the `?expand=monitor` query. (optional)

    try:
        # Get BGP test
        api_response = api_instance.get_bgp_test(test_id, aid=aid, expand=expand)
        print("The response of BGPTestsApi->get_bgp_test:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BGPTestsApi->get_bgp_test: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_id** | **str**| Test ID | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 
 **expand** | [**List[ExpandBgpTestOptions]**](ExpandBgpTestOptions.md)| Optional parameter on whether or not to expand the test sub-resources. By default no expansion takes place if the query parameter is not present. To expand the &#x60;monitors&#x60; sub-resource, pass the &#x60;?expand&#x3D;monitor&#x60; query. | [optional] 

### Return type

[**BgpTestResponse**](BgpTestResponse.md)

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

# **get_bgp_tests**
> BgpTests get_bgp_tests(aid=aid)

List BGP tests

Returns a list of BGP tests and saved events.

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.tests
from thousandeyes_sdk.tests.models.bgp_tests import BgpTests
from thousandeyes_sdk.tests.rest import ApiException
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
    api_instance = thousandeyes_sdk.tests.BGPTestsApi(api_client)
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # List BGP tests
        api_response = api_instance.get_bgp_tests(aid=aid)
        print("The response of BGPTestsApi->get_bgp_tests:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BGPTestsApi->get_bgp_tests: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

[**BgpTests**](BgpTests.md)

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

# **update_bgp_test**
> BgpTestResponse update_bgp_test(test_id, update_bgp_test_request, aid=aid, expand=expand)

Update BGP test

Updates a BGP test. This method requires Account Admin permissions. The target test cannot be a live share or saved event.

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.tests
from thousandeyes_sdk.tests.models.bgp_test_response import BgpTestResponse
from thousandeyes_sdk.tests.models.expand_bgp_test_options import ExpandBgpTestOptions
from thousandeyes_sdk.tests.models.update_bgp_test_request import UpdateBgpTestRequest
from thousandeyes_sdk.tests.rest import ApiException
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
    api_instance = thousandeyes_sdk.tests.BGPTestsApi(api_client)
    test_id = '202701' # str | Test ID
    update_bgp_test_request = thousandeyes_sdk.tests.UpdateBgpTestRequest() # UpdateBgpTestRequest | 
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)
    expand = [thousandeyes_sdk.tests.ExpandBgpTestOptions()] # List[ExpandBgpTestOptions] | Optional parameter on whether or not to expand the test sub-resources. By default no expansion takes place if the query parameter is not present. To expand the `monitors` sub-resource, pass the `?expand=monitor` query. (optional)

    try:
        # Update BGP test
        api_response = api_instance.update_bgp_test(test_id, update_bgp_test_request, aid=aid, expand=expand)
        print("The response of BGPTestsApi->update_bgp_test:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BGPTestsApi->update_bgp_test: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_id** | **str**| Test ID | 
 **update_bgp_test_request** | [**UpdateBgpTestRequest**](UpdateBgpTestRequest.md)|  | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 
 **expand** | [**List[ExpandBgpTestOptions]**](ExpandBgpTestOptions.md)| Optional parameter on whether or not to expand the test sub-resources. By default no expansion takes place if the query parameter is not present. To expand the &#x60;monitors&#x60; sub-resource, pass the &#x60;?expand&#x3D;monitor&#x60; query. | [optional] 

### Return type

[**BgpTestResponse**](BgpTestResponse.md)

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

