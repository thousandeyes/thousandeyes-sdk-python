# thousandeyes_sdk.tests.SIPServerApi

All URIs are relative to *https://api.thousandeyes.com/v7*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_sip_server_test**](SIPServerApi.md#create_sip_server_test) | **POST** /tests/sip-server | Create SIP Server test
[**delete_sip_server_test**](SIPServerApi.md#delete_sip_server_test) | **DELETE** /tests/sip-server/{testId} | Delete SIP Server test
[**get_sip_server_test**](SIPServerApi.md#get_sip_server_test) | **GET** /tests/sip-server/{testId} | Get SIP Server test
[**get_sip_server_tests**](SIPServerApi.md#get_sip_server_tests) | **GET** /tests/sip-server | List SIP Server tests
[**update_sip_server_test**](SIPServerApi.md#update_sip_server_test) | **PUT** /tests/sip-server/{testId} | Update SIP Server test


# **create_sip_server_test**
> SipServerTest create_sip_server_test(update_sip_server_test, aid=aid, expand=expand)

Create SIP Server test

Creates a new SIP Server test. This method requires Account Admin permissions.

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.tests
from thousandeyes_sdk.tests.models.expand import Expand
from thousandeyes_sdk.tests.models.sip_server_test import SipServerTest
from thousandeyes_sdk.tests.models.update_sip_server_test import UpdateSipServerTest
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
with thousandeyes_sdk.tests.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = thousandeyes_sdk.tests.SIPServerApi(api_client)
    update_sip_server_test = thousandeyes_sdk.tests.UpdateSipServerTest() # UpdateSipServerTest | 
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)
    expand = [thousandeyes_sdk.tests.Expand()] # List[Expand] | Optional parameter on whether or not to expand the test sub-resources. By default no expansion is going to take place if the query parameter is not present. If the user wishes to expand the `agents` sub-resource, they need to pass the `?expand=agent` query. (optional)

    try:
        # Create SIP Server test
        api_response = api_instance.create_sip_server_test(update_sip_server_test, aid=aid, expand=expand)
        print("The response of SIPServerApi->create_sip_server_test:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SIPServerApi->create_sip_server_test: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_sip_server_test** | [**UpdateSipServerTest**](UpdateSipServerTest.md)|  | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 
 **expand** | [**List[Expand]**](Expand.md)| Optional parameter on whether or not to expand the test sub-resources. By default no expansion is going to take place if the query parameter is not present. If the user wishes to expand the &#x60;agents&#x60; sub-resource, they need to pass the &#x60;?expand&#x3D;agent&#x60; query. | [optional] 

### Return type

[**SipServerTest**](SipServerTest.md)

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

# **delete_sip_server_test**
> delete_sip_server_test(test_id, aid=aid)

Delete SIP Server test

Deletes the specified SIP Server test. This method requires Account Admin permissions.

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
with thousandeyes_sdk.tests.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = thousandeyes_sdk.tests.SIPServerApi(api_client)
    test_id = '281474976710706' # str | ID of the test
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Delete SIP Server test
        api_instance.delete_sip_server_test(test_id, aid=aid)
    except Exception as e:
        print("Exception when calling SIPServerApi->delete_sip_server_test: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_id** | **str**| ID of the test | 
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sip_server_test**
> SipServerTest get_sip_server_test(test_id, aid=aid, expand=expand)

Get SIP Server test

Returns details for a SIP Server test, including name, intervals, targets, alert rules and agents.

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.tests
from thousandeyes_sdk.tests.models.expand import Expand
from thousandeyes_sdk.tests.models.sip_server_test import SipServerTest
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
with thousandeyes_sdk.tests.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = thousandeyes_sdk.tests.SIPServerApi(api_client)
    test_id = '281474976710706' # str | ID of the test
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)
    expand = [thousandeyes_sdk.tests.Expand()] # List[Expand] | Optional parameter on whether or not to expand the test sub-resources. By default no expansion is going to take place if the query parameter is not present. If the user wishes to expand the `agents` sub-resource, they need to pass the `?expand=agent` query. (optional)

    try:
        # Get SIP Server test
        api_response = api_instance.get_sip_server_test(test_id, aid=aid, expand=expand)
        print("The response of SIPServerApi->get_sip_server_test:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SIPServerApi->get_sip_server_test: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_id** | **str**| ID of the test | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 
 **expand** | [**List[Expand]**](Expand.md)| Optional parameter on whether or not to expand the test sub-resources. By default no expansion is going to take place if the query parameter is not present. If the user wishes to expand the &#x60;agents&#x60; sub-resource, they need to pass the &#x60;?expand&#x3D;agent&#x60; query. | [optional] 

### Return type

[**SipServerTest**](SipServerTest.md)

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

# **get_sip_server_tests**
> SipServerTests get_sip_server_tests(aid=aid)

List SIP Server tests

Returns a list of SIP Server tests and saved events.

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.tests
from thousandeyes_sdk.tests.models.sip_server_tests import SipServerTests
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
with thousandeyes_sdk.tests.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = thousandeyes_sdk.tests.SIPServerApi(api_client)
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # List SIP Server tests
        api_response = api_instance.get_sip_server_tests(aid=aid)
        print("The response of SIPServerApi->get_sip_server_tests:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SIPServerApi->get_sip_server_tests: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

[**SipServerTests**](SipServerTests.md)

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

# **update_sip_server_test**
> SipServerTest update_sip_server_test(test_id, update_sip_server_test, aid=aid, expand=expand)

Update SIP Server test

Updates a SIP Server test. The target test cannot be a live share or saved event. This method requires Account Admin permissions.

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.tests
from thousandeyes_sdk.tests.models.expand import Expand
from thousandeyes_sdk.tests.models.sip_server_test import SipServerTest
from thousandeyes_sdk.tests.models.update_sip_server_test import UpdateSipServerTest
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
with thousandeyes_sdk.tests.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = thousandeyes_sdk.tests.SIPServerApi(api_client)
    test_id = '281474976710706' # str | ID of the test
    update_sip_server_test = thousandeyes_sdk.tests.UpdateSipServerTest() # UpdateSipServerTest | 
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)
    expand = [thousandeyes_sdk.tests.Expand()] # List[Expand] | Optional parameter on whether or not to expand the test sub-resources. By default no expansion is going to take place if the query parameter is not present. If the user wishes to expand the `agents` sub-resource, they need to pass the `?expand=agent` query. (optional)

    try:
        # Update SIP Server test
        api_response = api_instance.update_sip_server_test(test_id, update_sip_server_test, aid=aid, expand=expand)
        print("The response of SIPServerApi->update_sip_server_test:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SIPServerApi->update_sip_server_test: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_id** | **str**| ID of the test | 
 **update_sip_server_test** | [**UpdateSipServerTest**](UpdateSipServerTest.md)|  | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 
 **expand** | [**List[Expand]**](Expand.md)| Optional parameter on whether or not to expand the test sub-resources. By default no expansion is going to take place if the query parameter is not present. If the user wishes to expand the &#x60;agents&#x60; sub-resource, they need to pass the &#x60;?expand&#x3D;agent&#x60; query. | [optional] 

### Return type

[**SipServerTest**](SipServerTest.md)

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

