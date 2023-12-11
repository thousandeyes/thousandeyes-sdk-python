# alerts_api.AlertSuppressionWindowsApi

All URIs are relative to *https://api.thousandeyes.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_suppression_windows**](AlertSuppressionWindowsApi.md#create_suppression_windows) | **POST** /v7/alert-suppression-windows | Create alert suppression window
[**delete_suppression_window**](AlertSuppressionWindowsApi.md#delete_suppression_window) | **DELETE** /v7/alert-suppression-windows/{windowId} | Delete alert suppression window
[**get_suppression_window_details**](AlertSuppressionWindowsApi.md#get_suppression_window_details) | **GET** /v7/alert-suppression-windows/{windowId} | Retrieve alert suppression window
[**get_suppression_windows**](AlertSuppressionWindowsApi.md#get_suppression_windows) | **GET** /v7/alert-suppression-windows | List alert suppression windows
[**update_suppression_window**](AlertSuppressionWindowsApi.md#update_suppression_window) | **PUT** /v7/alert-suppression-windows/{windowId} | Update alert suppression window


# **create_suppression_windows**
> CreateSuppressionWindows201Response create_suppression_windows(alert_suppression_window_request, aid=aid, expand=expand)

Create alert suppression window

Creates a new alert suppression window in ThousandEyes, using the  provided POST data. Only Account Admins can create alert suppression windows.

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import alerts_api
from alerts_api.models.alert_suppression_window_request import AlertSuppressionWindowRequest
from alerts_api.models.create_suppression_windows201_response import CreateSuppressionWindows201Response
from alerts_api.models.expand import Expand
from alerts_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.thousandeyes.com
# See configuration.py for a list of all supported configuration parameters.
configuration = alerts_api.Configuration(
    host = "https://api.thousandeyes.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = alerts_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with alerts_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = alerts_api.AlertSuppressionWindowsApi(api_client)
    alert_suppression_window_request = alerts_api.AlertSuppressionWindowRequest() # AlertSuppressionWindowRequest | 
    aid = '2067' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)
    expand = [alerts_api.Expand()] # List[Expand] | Optional parameter on whether or not to expand alert related resources.  Without this parameter, there's no default expansion. For example, to expand the \"tests\" resource, use the `?expand=test` query. (optional)

    try:
        # Create alert suppression window
        api_response = api_instance.create_suppression_windows(alert_suppression_window_request, aid=aid, expand=expand)
        print("The response of AlertSuppressionWindowsApi->create_suppression_windows:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertSuppressionWindowsApi->create_suppression_windows: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_suppression_window_request** | [**AlertSuppressionWindowRequest**](AlertSuppressionWindowRequest.md)|  | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 
 **expand** | [**List[Expand]**](Expand.md)| Optional parameter on whether or not to expand alert related resources.  Without this parameter, there&#39;s no default expansion. For example, to expand the \&quot;tests\&quot; resource, use the &#x60;?expand&#x3D;test&#x60; query. | [optional] 

### Return type

[**CreateSuppressionWindows201Response**](CreateSuppressionWindows201Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/hal+json
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_suppression_window**
> delete_suppression_window(window_id, aid=aid)

Delete alert suppression window

Deletes an alert suppression window.

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import alerts_api
from alerts_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.thousandeyes.com
# See configuration.py for a list of all supported configuration parameters.
configuration = alerts_api.Configuration(
    host = "https://api.thousandeyes.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = alerts_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with alerts_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = alerts_api.AlertSuppressionWindowsApi(api_client)
    window_id = '2411' # str | Unique window ID.
    aid = '2067' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Delete alert suppression window
        api_instance.delete_suppression_window(window_id, aid=aid)
    except Exception as e:
        print("Exception when calling AlertSuppressionWindowsApi->delete_suppression_window: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **window_id** | **str**| Unique window ID. | 
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_suppression_window_details**
> CreateSuppressionWindows201Response get_suppression_window_details(window_id, aid=aid, expand=expand)

Retrieve alert suppression window

Returns detailed information about an alert suppression window configured in your account group.

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import alerts_api
from alerts_api.models.create_suppression_windows201_response import CreateSuppressionWindows201Response
from alerts_api.models.expand import Expand
from alerts_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.thousandeyes.com
# See configuration.py for a list of all supported configuration parameters.
configuration = alerts_api.Configuration(
    host = "https://api.thousandeyes.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = alerts_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with alerts_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = alerts_api.AlertSuppressionWindowsApi(api_client)
    window_id = '2411' # str | Unique window ID.
    aid = '2067' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)
    expand = [alerts_api.Expand()] # List[Expand] | Optional parameter on whether or not to expand alert related resources.  Without this parameter, there's no default expansion. For example, to expand the \"tests\" resource, use the `?expand=test` query. (optional)

    try:
        # Retrieve alert suppression window
        api_response = api_instance.get_suppression_window_details(window_id, aid=aid, expand=expand)
        print("The response of AlertSuppressionWindowsApi->get_suppression_window_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertSuppressionWindowsApi->get_suppression_window_details: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **window_id** | **str**| Unique window ID. | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 
 **expand** | [**List[Expand]**](Expand.md)| Optional parameter on whether or not to expand alert related resources.  Without this parameter, there&#39;s no default expansion. For example, to expand the \&quot;tests\&quot; resource, use the &#x60;?expand&#x3D;test&#x60; query. | [optional] 

### Return type

[**CreateSuppressionWindows201Response**](CreateSuppressionWindows201Response.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_suppression_windows**
> GetSuppressionWindows200Response get_suppression_windows(aid=aid)

List alert suppression windows

Returns a list of all alert suppression windows configured in your account group.

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import alerts_api
from alerts_api.models.get_suppression_windows200_response import GetSuppressionWindows200Response
from alerts_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.thousandeyes.com
# See configuration.py for a list of all supported configuration parameters.
configuration = alerts_api.Configuration(
    host = "https://api.thousandeyes.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = alerts_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with alerts_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = alerts_api.AlertSuppressionWindowsApi(api_client)
    aid = '2067' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # List alert suppression windows
        api_response = api_instance.get_suppression_windows(aid=aid)
        print("The response of AlertSuppressionWindowsApi->get_suppression_windows:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertSuppressionWindowsApi->get_suppression_windows: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

[**GetSuppressionWindows200Response**](GetSuppressionWindows200Response.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_suppression_window**
> CreateSuppressionWindows201Response update_suppression_window(window_id, alert_suppression_window_request, aid=aid, expand=expand)

Update alert suppression window

Updates an alert suppression window in ThousandEyes, using the  provided POST data. Only Account Admins can update alert suppression windows.

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import alerts_api
from alerts_api.models.alert_suppression_window_request import AlertSuppressionWindowRequest
from alerts_api.models.create_suppression_windows201_response import CreateSuppressionWindows201Response
from alerts_api.models.expand import Expand
from alerts_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.thousandeyes.com
# See configuration.py for a list of all supported configuration parameters.
configuration = alerts_api.Configuration(
    host = "https://api.thousandeyes.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = alerts_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with alerts_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = alerts_api.AlertSuppressionWindowsApi(api_client)
    window_id = '2411' # str | Unique window ID.
    alert_suppression_window_request = alerts_api.AlertSuppressionWindowRequest() # AlertSuppressionWindowRequest | 
    aid = '2067' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)
    expand = [alerts_api.Expand()] # List[Expand] | Optional parameter on whether or not to expand alert related resources.  Without this parameter, there's no default expansion. For example, to expand the \"tests\" resource, use the `?expand=test` query. (optional)

    try:
        # Update alert suppression window
        api_response = api_instance.update_suppression_window(window_id, alert_suppression_window_request, aid=aid, expand=expand)
        print("The response of AlertSuppressionWindowsApi->update_suppression_window:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertSuppressionWindowsApi->update_suppression_window: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **window_id** | **str**| Unique window ID. | 
 **alert_suppression_window_request** | [**AlertSuppressionWindowRequest**](AlertSuppressionWindowRequest.md)|  | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 
 **expand** | [**List[Expand]**](Expand.md)| Optional parameter on whether or not to expand alert related resources.  Without this parameter, there&#39;s no default expansion. For example, to expand the \&quot;tests\&quot; resource, use the &#x60;?expand&#x3D;test&#x60; query. | [optional] 

### Return type

[**CreateSuppressionWindows201Response**](CreateSuppressionWindows201Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/hal+json
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

