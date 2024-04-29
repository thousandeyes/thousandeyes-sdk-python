# tests.FTPServerApi

All URIs are relative to *https://api.thousandeyes.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_ftp_server_test**](FTPServerApi.md#create_ftp_server_test) | **POST** /v7/tests/ftp-server | Create FTP Server test
[**delete_ftp_server_test**](FTPServerApi.md#delete_ftp_server_test) | **DELETE** /v7/tests/ftp-server/{testId} | Delete FTP Server test
[**get_ftp_server_test**](FTPServerApi.md#get_ftp_server_test) | **GET** /v7/tests/ftp-server/{testId} | Get FTP Server test
[**get_ftp_server_tests**](FTPServerApi.md#get_ftp_server_tests) | **GET** /v7/tests/ftp-server | List FTP Server tests
[**update_ftp_server_test**](FTPServerApi.md#update_ftp_server_test) | **PUT** /v7/tests/ftp-server/{testId} | Update FTP Server test


# **create_ftp_server_test**
> FtpServerTest create_ftp_server_test(update_ftp_server_test, aid=aid, expand=expand)

Create FTP Server test

Creates a new FTP Server test. This method requires Account Admin permissions.

### Example

* Bearer Authentication (BearerAuth):

```python
import tests
from tests.models.expand import Expand
from tests.models.ftp_server_test import FtpServerTest
from tests.models.update_ftp_server_test import UpdateFtpServerTest
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
    api_instance = tests.FTPServerApi(api_client)
    update_ftp_server_test = tests.UpdateFtpServerTest() # UpdateFtpServerTest | 
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)
    expand = [tests.Expand()] # List[Expand] | Optional parameter on whether or not to expand the test sub-resources. By default no expansion is going to take place if the query parameter is not present. If the user wishes to expand the `agents` sub-resource, they need to pass the `?expand=agent` query. (optional)

    try:
        # Create FTP Server test
        api_response = api_instance.create_ftp_server_test(update_ftp_server_test, aid=aid, expand=expand)
        print("The response of FTPServerApi->create_ftp_server_test:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FTPServerApi->create_ftp_server_test: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_ftp_server_test** | [**UpdateFtpServerTest**](UpdateFtpServerTest.md)|  | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 
 **expand** | [**List[Expand]**](Expand.md)| Optional parameter on whether or not to expand the test sub-resources. By default no expansion is going to take place if the query parameter is not present. If the user wishes to expand the &#x60;agents&#x60; sub-resource, they need to pass the &#x60;?expand&#x3D;agent&#x60; query. | [optional] 

### Return type

[**FtpServerTest**](FtpServerTest.md)

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

# **delete_ftp_server_test**
> delete_ftp_server_test(test_id, aid=aid)

Delete FTP Server test

Deletes the specified FTP Server test. This method requires Account Admin permissions.

### Example

* Bearer Authentication (BearerAuth):

```python
import tests
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
    api_instance = tests.FTPServerApi(api_client)
    test_id = '281474976710706' # str | ID of the test
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Delete FTP Server test
        api_instance.delete_ftp_server_test(test_id, aid=aid)
    except Exception as e:
        print("Exception when calling FTPServerApi->delete_ftp_server_test: %s\n" % e)
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
 - **Accept**: application/problem+json

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

# **get_ftp_server_test**
> FtpServerTest get_ftp_server_test(test_id, aid=aid, expand=expand)

Get FTP Server test

Returns details for a FTP Server test, including name, intervals, targets, alert rules and agents.

### Example

* Bearer Authentication (BearerAuth):

```python
import tests
from tests.models.expand import Expand
from tests.models.ftp_server_test import FtpServerTest
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
    api_instance = tests.FTPServerApi(api_client)
    test_id = '281474976710706' # str | ID of the test
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)
    expand = [tests.Expand()] # List[Expand] | Optional parameter on whether or not to expand the test sub-resources. By default no expansion is going to take place if the query parameter is not present. If the user wishes to expand the `agents` sub-resource, they need to pass the `?expand=agent` query. (optional)

    try:
        # Get FTP Server test
        api_response = api_instance.get_ftp_server_test(test_id, aid=aid, expand=expand)
        print("The response of FTPServerApi->get_ftp_server_test:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FTPServerApi->get_ftp_server_test: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_id** | **str**| ID of the test | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 
 **expand** | [**List[Expand]**](Expand.md)| Optional parameter on whether or not to expand the test sub-resources. By default no expansion is going to take place if the query parameter is not present. If the user wishes to expand the &#x60;agents&#x60; sub-resource, they need to pass the &#x60;?expand&#x3D;agent&#x60; query. | [optional] 

### Return type

[**FtpServerTest**](FtpServerTest.md)

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

# **get_ftp_server_tests**
> GetFtpServerTests200Response get_ftp_server_tests(aid=aid)

List FTP Server tests

Returns a list of FTP Server tests and saved events.

### Example

* Bearer Authentication (BearerAuth):

```python
import tests
from tests.models.get_ftp_server_tests200_response import GetFtpServerTests200Response
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
    api_instance = tests.FTPServerApi(api_client)
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # List FTP Server tests
        api_response = api_instance.get_ftp_server_tests(aid=aid)
        print("The response of FTPServerApi->get_ftp_server_tests:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FTPServerApi->get_ftp_server_tests: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

[**GetFtpServerTests200Response**](GetFtpServerTests200Response.md)

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

# **update_ftp_server_test**
> FtpServerTest update_ftp_server_test(test_id, update_ftp_server_test, aid=aid, expand=expand)

Update FTP Server test

Updates a FTP Server test. The target test cannot be a live share or saved event. This method requires Account Admin permissions.

### Example

* Bearer Authentication (BearerAuth):

```python
import tests
from tests.models.expand import Expand
from tests.models.ftp_server_test import FtpServerTest
from tests.models.update_ftp_server_test import UpdateFtpServerTest
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
    api_instance = tests.FTPServerApi(api_client)
    test_id = '281474976710706' # str | ID of the test
    update_ftp_server_test = tests.UpdateFtpServerTest() # UpdateFtpServerTest | 
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)
    expand = [tests.Expand()] # List[Expand] | Optional parameter on whether or not to expand the test sub-resources. By default no expansion is going to take place if the query parameter is not present. If the user wishes to expand the `agents` sub-resource, they need to pass the `?expand=agent` query. (optional)

    try:
        # Update FTP Server test
        api_response = api_instance.update_ftp_server_test(test_id, update_ftp_server_test, aid=aid, expand=expand)
        print("The response of FTPServerApi->update_ftp_server_test:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FTPServerApi->update_ftp_server_test: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_id** | **str**| ID of the test | 
 **update_ftp_server_test** | [**UpdateFtpServerTest**](UpdateFtpServerTest.md)|  | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 
 **expand** | [**List[Expand]**](Expand.md)| Optional parameter on whether or not to expand the test sub-resources. By default no expansion is going to take place if the query parameter is not present. If the user wishes to expand the &#x60;agents&#x60; sub-resource, they need to pass the &#x60;?expand&#x3D;agent&#x60; query. | [optional] 

### Return type

[**FtpServerTest**](FtpServerTest.md)

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
