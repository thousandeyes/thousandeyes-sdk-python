# labels_api.TestApi

All URIs are relative to *https://api.thousandeyes.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_test_label**](TestApi.md#create_test_label) | **POST** /v7/labels/test | Create a Label of type &#x60;test&#x60;
[**delete_test_label**](TestApi.md#delete_test_label) | **DELETE** /v7/labels/test/{labelId} | Delete a Label object of type &#x60;test&#x60;
[**get_test_label**](TestApi.md#get_test_label) | **GET** /v7/labels/test/{labelId} | Get a Label object of type &#x60;test&#x60;
[**update_test_label**](TestApi.md#update_test_label) | **PUT** /v7/labels/test/{labelId} | Update a Label object of type &#x60;test&#x60;


# **create_test_label**
> CreateAgentLabel201Response create_test_label(aid=aid, label_request=label_request)

Create a Label of type `test`

Creates a new label (formerly called group) in ThousandEyes, based on properties provided in the POST data.  In order to create a new label, the user attempting the creation must have sufficient privileges to create labels. Regular users are blocked from using any of the POST-based methods. Note: When creating or updating a label and assigning `agent` or `test`, the user needs permission to modify the objects being added.

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import labels_api
from labels_api.models.create_agent_label201_response import CreateAgentLabel201Response
from labels_api.models.label_request import LabelRequest
from labels_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.thousandeyes.com
# See configuration.py for a list of all supported configuration parameters.
configuration = labels_api.Configuration(
    host = "https://api.thousandeyes.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = labels_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with labels_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = labels_api.TestApi(api_client)
    aid = '2067' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)
    label_request = labels_api.LabelRequest() # LabelRequest | Label resource (optional)

    try:
        # Create a Label of type `test`
        api_response = api_instance.create_test_label(aid=aid, label_request=label_request)
        print("The response of TestApi->create_test_label:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestApi->create_test_label: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 
 **label_request** | [**LabelRequest**](LabelRequest.md)| Label resource | [optional] 

### Return type

[**CreateAgentLabel201Response**](CreateAgentLabel201Response.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_test_label**
> delete_test_label(label_id, aid=aid)

Delete a Label object of type `test`

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import labels_api
from labels_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.thousandeyes.com
# See configuration.py for a list of all supported configuration parameters.
configuration = labels_api.Configuration(
    host = "https://api.thousandeyes.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = labels_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with labels_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = labels_api.TestApi(api_client)
    label_id = '961' # str | ID of the label to get
    aid = '2067' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Delete a Label object of type `test`
        api_instance.delete_test_label(label_id, aid=aid)
    except Exception as e:
        print("Exception when calling TestApi->delete_test_label: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **label_id** | **str**| ID of the label to get | 
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

# **get_test_label**
> CreateAgentLabel201Response get_test_label(label_id, aid=aid)

Get a Label object of type `test`

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import labels_api
from labels_api.models.create_agent_label201_response import CreateAgentLabel201Response
from labels_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.thousandeyes.com
# See configuration.py for a list of all supported configuration parameters.
configuration = labels_api.Configuration(
    host = "https://api.thousandeyes.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = labels_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with labels_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = labels_api.TestApi(api_client)
    label_id = '961' # str | ID of the label to get
    aid = '2067' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Get a Label object of type `test`
        api_response = api_instance.get_test_label(label_id, aid=aid)
        print("The response of TestApi->get_test_label:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestApi->get_test_label: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **label_id** | **str**| ID of the label to get | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

[**CreateAgentLabel201Response**](CreateAgentLabel201Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **update_test_label**
> CreateAgentLabel201Response update_test_label(label_id, aid=aid, label_request=label_request)

Update a Label object of type `test`

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import labels_api
from labels_api.models.create_agent_label201_response import CreateAgentLabel201Response
from labels_api.models.label_request import LabelRequest
from labels_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.thousandeyes.com
# See configuration.py for a list of all supported configuration parameters.
configuration = labels_api.Configuration(
    host = "https://api.thousandeyes.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = labels_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with labels_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = labels_api.TestApi(api_client)
    label_id = '961' # str | ID of the label to get
    aid = '2067' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)
    label_request = labels_api.LabelRequest() # LabelRequest |  (optional)

    try:
        # Update a Label object of type `test`
        api_response = api_instance.update_test_label(label_id, aid=aid, label_request=label_request)
        print("The response of TestApi->update_test_label:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestApi->update_test_label: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **label_id** | **str**| ID of the label to get | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 
 **label_request** | [**LabelRequest**](LabelRequest.md)|  | [optional] 

### Return type

[**CreateAgentLabel201Response**](CreateAgentLabel201Response.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

