# labels.AgentApi

All URIs are relative to *https://api.thousandeyes.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_agent_label**](AgentApi.md#create_agent_label) | **POST** /v7/labels/agent | Create a Label of type &#x60;agent&#x60;
[**delete_agent_label**](AgentApi.md#delete_agent_label) | **DELETE** /v7/labels/agent/{labelId} | Delete a Label object of type &#x60;agent&#x60;
[**get_agent_label**](AgentApi.md#get_agent_label) | **GET** /v7/labels/agent/{labelId} | Get a Label object of type &#x60;agent&#x60;
[**get_agent_labels**](AgentApi.md#get_agent_labels) | **GET** /v7/labels/agent | Get list of Labels of type &#x60;agent&#x60;
[**update_agent_label**](AgentApi.md#update_agent_label) | **PUT** /v7/labels/agent/{labelId} | Update a Label object of type &#x60;agent&#x60;


# **create_agent_label**
> CreateAgentLabel201Response create_agent_label(aid=aid, label_request=label_request)

Create a Label of type `agent`

Creates a new label (formerly called group) in ThousandEyes, based on properties provided in the POST data.  You must have sufficient permissions to create a new label. Regular users are blocked from using any of the POST-based methods. Note: When creating or updating a label and assigning `agent` or `test`, the user needs permission to modify the objects being added.

### Example

* Bearer Authentication (BearerAuth):

```python
import labels
from labels.models.create_agent_label201_response import CreateAgentLabel201Response
from labels.models.label_request import LabelRequest
from labels.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.thousandeyes.com
# See configuration.py for a list of all supported configuration parameters.
configuration = labels.Configuration(
    host = "https://api.thousandeyes.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = labels.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with labels.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = labels.AgentApi(api_client)
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)
    label_request = labels.LabelRequest() # LabelRequest | Label resource (optional)

    try:
        # Create a Label of type `agent`
        api_response = api_instance.create_agent_label(aid=aid, label_request=label_request)
        print("The response of AgentApi->create_agent_label:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentApi->create_agent_label: %s\n" % e)
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

# **delete_agent_label**
> delete_agent_label(label_id, aid=aid)

Delete a Label object of type `agent`

### Example

* Bearer Authentication (BearerAuth):

```python
import labels
from labels.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.thousandeyes.com
# See configuration.py for a list of all supported configuration parameters.
configuration = labels.Configuration(
    host = "https://api.thousandeyes.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = labels.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with labels.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = labels.AgentApi(api_client)
    label_id = '961' # str | ID of the label to get
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Delete a Label object of type `agent`
        api_instance.delete_agent_label(label_id, aid=aid)
    except Exception as e:
        print("Exception when calling AgentApi->delete_agent_label: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_agent_label**
> CreateAgentLabel201Response get_agent_label(label_id, aid=aid)

Get a Label object of type `agent`

### Example

* Bearer Authentication (BearerAuth):

```python
import labels
from labels.models.create_agent_label201_response import CreateAgentLabel201Response
from labels.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.thousandeyes.com
# See configuration.py for a list of all supported configuration parameters.
configuration = labels.Configuration(
    host = "https://api.thousandeyes.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = labels.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with labels.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = labels.AgentApi(api_client)
    label_id = '961' # str | ID of the label to get
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Get a Label object of type `agent`
        api_response = api_instance.get_agent_label(label_id, aid=aid)
        print("The response of AgentApi->get_agent_label:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentApi->get_agent_label: %s\n" % e)
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

# **get_agent_labels**
> GetLabels200Response get_agent_labels(aid=aid)

Get list of Labels of type `agent`

Returns a list of all Agent labels (formerly called groups) configured in ThousandEyes.

### Example

* Bearer Authentication (BearerAuth):

```python
import labels
from labels.models.get_labels200_response import GetLabels200Response
from labels.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.thousandeyes.com
# See configuration.py for a list of all supported configuration parameters.
configuration = labels.Configuration(
    host = "https://api.thousandeyes.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = labels.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with labels.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = labels.AgentApi(api_client)
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Get list of Labels of type `agent`
        api_response = api_instance.get_agent_labels(aid=aid)
        print("The response of AgentApi->get_agent_labels:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentApi->get_agent_labels: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

[**GetLabels200Response**](GetLabels200Response.md)

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

# **update_agent_label**
> CreateAgentLabel201Response update_agent_label(label_id, aid=aid, label_request=label_request)

Update a Label object of type `agent`

### Example

* Bearer Authentication (BearerAuth):

```python
import labels
from labels.models.create_agent_label201_response import CreateAgentLabel201Response
from labels.models.label_request import LabelRequest
from labels.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.thousandeyes.com
# See configuration.py for a list of all supported configuration parameters.
configuration = labels.Configuration(
    host = "https://api.thousandeyes.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = labels.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with labels.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = labels.AgentApi(api_client)
    label_id = '961' # str | ID of the label to get
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)
    label_request = labels.LabelRequest() # LabelRequest |  (optional)

    try:
        # Update a Label object of type `agent`
        api_response = api_instance.update_agent_label(label_id, aid=aid, label_request=label_request)
        print("The response of AgentApi->update_agent_label:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentApi->update_agent_label: %s\n" % e)
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

