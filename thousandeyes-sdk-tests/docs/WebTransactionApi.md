# thousandeyes_sdk.tests.WebTransactionApi

All URIs are relative to *https://api.thousandeyes.com/v7*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_web_transactions_test**](WebTransactionApi.md#create_web_transactions_test) | **POST** /tests/web-transactions | Create Web Transactions test
[**delete_web_transactions_test**](WebTransactionApi.md#delete_web_transactions_test) | **DELETE** /tests/web-transactions/{testId} | Delete Web Transactions test
[**get_web_transactions_test**](WebTransactionApi.md#get_web_transactions_test) | **GET** /tests/web-transactions/{testId} | Get Web Transactions test
[**get_web_transactions_tests**](WebTransactionApi.md#get_web_transactions_tests) | **GET** /tests/web-transactions | List Web Transactions tests
[**update_web_transactions_test**](WebTransactionApi.md#update_web_transactions_test) | **PUT** /tests/web-transactions/{testId} | Update Web Transactions test


# **create_web_transactions_test**
> WebTransactionTest create_web_transactions_test(update_web_transaction_test, aid=aid, expand=expand)

Create Web Transactions test

Creates a new Web Transactions test. This method requires Account Admin permissions.

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.tests
from thousandeyes_sdk.tests.models.expand import Expand
from thousandeyes_sdk.tests.models.update_web_transaction_test import UpdateWebTransactionTest
from thousandeyes_sdk.tests.models.web_transaction_test import WebTransactionTest
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
    api_instance = thousandeyes_sdk.tests.WebTransactionApi(api_client)
    update_web_transaction_test = thousandeyes_sdk.tests.UpdateWebTransactionTest() # UpdateWebTransactionTest | 
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)
    expand = [thousandeyes_sdk.tests.Expand()] # List[Expand] | Optional parameter on whether or not to expand the test sub-resources. By default no expansion is going to take place if the query parameter is not present. If the user wishes to expand the `agents` sub-resource, they need to pass the `?expand=agent` query. (optional)

    try:
        # Create Web Transactions test
        api_response = api_instance.create_web_transactions_test(update_web_transaction_test, aid=aid, expand=expand)
        print("The response of WebTransactionApi->create_web_transactions_test:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebTransactionApi->create_web_transactions_test: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_web_transaction_test** | [**UpdateWebTransactionTest**](UpdateWebTransactionTest.md)|  | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 
 **expand** | [**List[Expand]**](Expand.md)| Optional parameter on whether or not to expand the test sub-resources. By default no expansion is going to take place if the query parameter is not present. If the user wishes to expand the &#x60;agents&#x60; sub-resource, they need to pass the &#x60;?expand&#x3D;agent&#x60; query. | [optional] 

### Return type

[**WebTransactionTest**](WebTransactionTest.md)

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

# **delete_web_transactions_test**
> delete_web_transactions_test(test_id, aid=aid)

Delete Web Transactions test

Deletes the specified Web Transactions test. This method requires Account Admin permissions.

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
    api_instance = thousandeyes_sdk.tests.WebTransactionApi(api_client)
    test_id = '281474976710706' # str | ID of the test
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Delete Web Transactions test
        api_instance.delete_web_transactions_test(test_id, aid=aid)
    except Exception as e:
        print("Exception when calling WebTransactionApi->delete_web_transactions_test: %s\n" % e)
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
**502** | Bad Gateway |  -  |
**0** | An error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_web_transactions_test**
> WebTransactionTest get_web_transactions_test(test_id, aid=aid, expand=expand)

Get Web Transactions test

Returns details for a Web Transactions test, including name, intervals, targets, alert rules and agents.

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.tests
from thousandeyes_sdk.tests.models.expand import Expand
from thousandeyes_sdk.tests.models.web_transaction_test import WebTransactionTest
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
    api_instance = thousandeyes_sdk.tests.WebTransactionApi(api_client)
    test_id = '281474976710706' # str | ID of the test
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)
    expand = [thousandeyes_sdk.tests.Expand()] # List[Expand] | Optional parameter on whether or not to expand the test sub-resources. By default no expansion is going to take place if the query parameter is not present. If the user wishes to expand the `agents` sub-resource, they need to pass the `?expand=agent` query. (optional)

    try:
        # Get Web Transactions test
        api_response = api_instance.get_web_transactions_test(test_id, aid=aid, expand=expand)
        print("The response of WebTransactionApi->get_web_transactions_test:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebTransactionApi->get_web_transactions_test: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_id** | **str**| ID of the test | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 
 **expand** | [**List[Expand]**](Expand.md)| Optional parameter on whether or not to expand the test sub-resources. By default no expansion is going to take place if the query parameter is not present. If the user wishes to expand the &#x60;agents&#x60; sub-resource, they need to pass the &#x60;?expand&#x3D;agent&#x60; query. | [optional] 

### Return type

[**WebTransactionTest**](WebTransactionTest.md)

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

# **get_web_transactions_tests**
> WebTransactionTests get_web_transactions_tests(aid=aid)

List Web Transactions tests

Returns a list of all Web Transactions tests and saved events.

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.tests
from thousandeyes_sdk.tests.models.web_transaction_tests import WebTransactionTests
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
    api_instance = thousandeyes_sdk.tests.WebTransactionApi(api_client)
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # List Web Transactions tests
        api_response = api_instance.get_web_transactions_tests(aid=aid)
        print("The response of WebTransactionApi->get_web_transactions_tests:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebTransactionApi->get_web_transactions_tests: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

[**WebTransactionTests**](WebTransactionTests.md)

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

# **update_web_transactions_test**
> WebTransactionTest update_web_transactions_test(test_id, update_web_transaction_test, aid=aid, expand=expand)

Update Web Transactions test

Updates a Web Transactions test. The target test cannot be a live share or saved event. This method requires Account Admin permissions.

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.tests
from thousandeyes_sdk.tests.models.expand import Expand
from thousandeyes_sdk.tests.models.update_web_transaction_test import UpdateWebTransactionTest
from thousandeyes_sdk.tests.models.web_transaction_test import WebTransactionTest
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
    api_instance = thousandeyes_sdk.tests.WebTransactionApi(api_client)
    test_id = '281474976710706' # str | ID of the test
    update_web_transaction_test = thousandeyes_sdk.tests.UpdateWebTransactionTest() # UpdateWebTransactionTest | 
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)
    expand = [thousandeyes_sdk.tests.Expand()] # List[Expand] | Optional parameter on whether or not to expand the test sub-resources. By default no expansion is going to take place if the query parameter is not present. If the user wishes to expand the `agents` sub-resource, they need to pass the `?expand=agent` query. (optional)

    try:
        # Update Web Transactions test
        api_response = api_instance.update_web_transactions_test(test_id, update_web_transaction_test, aid=aid, expand=expand)
        print("The response of WebTransactionApi->update_web_transactions_test:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebTransactionApi->update_web_transactions_test: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_id** | **str**| ID of the test | 
 **update_web_transaction_test** | [**UpdateWebTransactionTest**](UpdateWebTransactionTest.md)|  | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 
 **expand** | [**List[Expand]**](Expand.md)| Optional parameter on whether or not to expand the test sub-resources. By default no expansion is going to take place if the query parameter is not present. If the user wishes to expand the &#x60;agents&#x60; sub-resource, they need to pass the &#x60;?expand&#x3D;agent&#x60; query. | [optional] 

### Return type

[**WebTransactionTest**](WebTransactionTest.md)

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

