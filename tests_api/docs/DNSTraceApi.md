# tests_api.DNSTraceApi

All URIs are relative to *https://api.thousandeyes.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_dns_trace_test**](DNSTraceApi.md#create_dns_trace_test) | **POST** /v7/tests/dns-trace | Create DNS Trace test
[**delete_dns_trace_test**](DNSTraceApi.md#delete_dns_trace_test) | **DELETE** /v7/tests/dns-trace/{testId} | Delete DNS Trace test
[**get_dns_trace_test**](DNSTraceApi.md#get_dns_trace_test) | **GET** /v7/tests/dns-trace/{testId} | Get DNS Trace test
[**get_dns_trace_tests**](DNSTraceApi.md#get_dns_trace_tests) | **GET** /v7/tests/dns-trace | List DNS Trace tests
[**update_dns_trace_test**](DNSTraceApi.md#update_dns_trace_test) | **PUT** /v7/tests/dns-trace/{testId} | Update DNS Trace test


# **create_dns_trace_test**
> DnsTraceTest create_dns_trace_test(update_dns_trace_test, aid=aid, expand=expand)

Create DNS Trace test

Creates a new DNS Trace test. This method requires Account Admin permissions. 

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import tests_api
from tests_api.models.dns_trace_test import DnsTraceTest
from tests_api.models.expand import Expand
from tests_api.models.update_dns_trace_test import UpdateDnsTraceTest
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
    api_instance = tests_api.DNSTraceApi(api_client)
    update_dns_trace_test = tests_api.UpdateDnsTraceTest() # UpdateDnsTraceTest | 
    aid = '2067' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)
    expand = [tests_api.Expand()] # List[Expand] | Optional parameter on whether or not to expand the test sub-resources. By default no expansion is going to take place if the query parameter is not present. If the user wishes to expand the `agents` sub-resource, they need to pass the `?expand=agent` query. (optional)

    try:
        # Create DNS Trace test
        api_response = api_instance.create_dns_trace_test(update_dns_trace_test, aid=aid, expand=expand)
        print("The response of DNSTraceApi->create_dns_trace_test:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DNSTraceApi->create_dns_trace_test: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_dns_trace_test** | [**UpdateDnsTraceTest**](UpdateDnsTraceTest.md)|  | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 
 **expand** | [**List[Expand]**](Expand.md)| Optional parameter on whether or not to expand the test sub-resources. By default no expansion is going to take place if the query parameter is not present. If the user wishes to expand the &#x60;agents&#x60; sub-resource, they need to pass the &#x60;?expand&#x3D;agent&#x60; query. | [optional] 

### Return type

[**DnsTraceTest**](DnsTraceTest.md)

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

# **delete_dns_trace_test**
> delete_dns_trace_test(test_id, aid=aid)

Delete DNS Trace test

Deletes the specified DNS Trace test. This method requires Account Admin permissions. 

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import tests_api
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
    api_instance = tests_api.DNSTraceApi(api_client)
    test_id = '281474976710706' # str | ID of the test
    aid = '2067' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Delete DNS Trace test
        api_instance.delete_dns_trace_test(test_id, aid=aid)
    except Exception as e:
        print("Exception when calling DNSTraceApi->delete_dns_trace_test: %s\n" % e)
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

# **get_dns_trace_test**
> GetDnsTraceTest200Response get_dns_trace_test(test_id, aid=aid, expand=expand)

Get DNS Trace test

Returns details for a DNS Trace test, including name, intervals, targets, alert rules and agents.

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import tests_api
from tests_api.models.expand import Expand
from tests_api.models.get_dns_trace_test200_response import GetDnsTraceTest200Response
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
    api_instance = tests_api.DNSTraceApi(api_client)
    test_id = '281474976710706' # str | ID of the test
    aid = '2067' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)
    expand = [tests_api.Expand()] # List[Expand] | Optional parameter on whether or not to expand the test sub-resources. By default no expansion is going to take place if the query parameter is not present. If the user wishes to expand the `agents` sub-resource, they need to pass the `?expand=agent` query. (optional)

    try:
        # Get DNS Trace test
        api_response = api_instance.get_dns_trace_test(test_id, aid=aid, expand=expand)
        print("The response of DNSTraceApi->get_dns_trace_test:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DNSTraceApi->get_dns_trace_test: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_id** | **str**| ID of the test | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 
 **expand** | [**List[Expand]**](Expand.md)| Optional parameter on whether or not to expand the test sub-resources. By default no expansion is going to take place if the query parameter is not present. If the user wishes to expand the &#x60;agents&#x60; sub-resource, they need to pass the &#x60;?expand&#x3D;agent&#x60; query. | [optional] 

### Return type

[**GetDnsTraceTest200Response**](GetDnsTraceTest200Response.md)

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

# **get_dns_trace_tests**
> GetDnsTraceTests200Response get_dns_trace_tests(aid=aid)

List DNS Trace tests

Returns a list of all DNS Trace tests and saved events.

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import tests_api
from tests_api.models.get_dns_trace_tests200_response import GetDnsTraceTests200Response
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
    api_instance = tests_api.DNSTraceApi(api_client)
    aid = '2067' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # List DNS Trace tests
        api_response = api_instance.get_dns_trace_tests(aid=aid)
        print("The response of DNSTraceApi->get_dns_trace_tests:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DNSTraceApi->get_dns_trace_tests: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

[**GetDnsTraceTests200Response**](GetDnsTraceTests200Response.md)

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

# **update_dns_trace_test**
> GetDnsTraceTest200Response update_dns_trace_test(test_id, update_dns_trace_test, aid=aid, expand=expand)

Update DNS Trace test

Updates a DNS Trace test. The target test cannot be a live share or saved event. This method requires Account Admin permissions. 

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import tests_api
from tests_api.models.expand import Expand
from tests_api.models.get_dns_trace_test200_response import GetDnsTraceTest200Response
from tests_api.models.update_dns_trace_test import UpdateDnsTraceTest
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
    api_instance = tests_api.DNSTraceApi(api_client)
    test_id = '281474976710706' # str | ID of the test
    update_dns_trace_test = tests_api.UpdateDnsTraceTest() # UpdateDnsTraceTest | 
    aid = '2067' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)
    expand = [tests_api.Expand()] # List[Expand] | Optional parameter on whether or not to expand the test sub-resources. By default no expansion is going to take place if the query parameter is not present. If the user wishes to expand the `agents` sub-resource, they need to pass the `?expand=agent` query. (optional)

    try:
        # Update DNS Trace test
        api_response = api_instance.update_dns_trace_test(test_id, update_dns_trace_test, aid=aid, expand=expand)
        print("The response of DNSTraceApi->update_dns_trace_test:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DNSTraceApi->update_dns_trace_test: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_id** | **str**| ID of the test | 
 **update_dns_trace_test** | [**UpdateDnsTraceTest**](UpdateDnsTraceTest.md)|  | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 
 **expand** | [**List[Expand]**](Expand.md)| Optional parameter on whether or not to expand the test sub-resources. By default no expansion is going to take place if the query parameter is not present. If the user wishes to expand the &#x60;agents&#x60; sub-resource, they need to pass the &#x60;?expand&#x3D;agent&#x60; query. | [optional] 

### Return type

[**GetDnsTraceTest200Response**](GetDnsTraceTest200Response.md)

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

