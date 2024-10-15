# thousandeyes_sdk.endpoint_labels.EndpointAgentLabelsApi

All URIs are relative to *https://api.thousandeyes.com/v7*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_endpoint_label**](EndpointAgentLabelsApi.md#create_endpoint_label) | **POST** /endpoint/labels | Create label
[**delete_endpoint_label**](EndpointAgentLabelsApi.md#delete_endpoint_label) | **DELETE** /endpoint/labels/{id} | Delete label
[**get_endpoint_label**](EndpointAgentLabelsApi.md#get_endpoint_label) | **GET** /endpoint/labels/{id} | Retrieve label
[**get_endpoint_labels**](EndpointAgentLabelsApi.md#get_endpoint_labels) | **GET** /endpoint/labels | List labels
[**update_endpoint_label**](EndpointAgentLabelsApi.md#update_endpoint_label) | **PATCH** /endpoint/labels/{id} | Update label


# **create_endpoint_label**
> LabelResponse create_endpoint_label(aid=aid, label_request=label_request)

Create label

Creates a new label.

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.endpoint_labels
from thousandeyes_sdk.endpoint_labels.models.label_request import LabelRequest
from thousandeyes_sdk.endpoint_labels.models.label_response import LabelResponse
from thousandeyes_sdk.endpoint_labels.rest import ApiException
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
    api_instance = thousandeyes_sdk.endpoint_labels.EndpointAgentLabelsApi(api_client)
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)
    label_request = thousandeyes_sdk.endpoint_labels.LabelRequest() # LabelRequest | Label settings (optional)

    try:
        # Create label
        api_response = api_instance.create_endpoint_label(aid=aid, label_request=label_request)
        print("The response of EndpointAgentLabelsApi->create_endpoint_label:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointAgentLabelsApi->create_endpoint_label: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 
 **label_request** | [**LabelRequest**](LabelRequest.md)| Label settings | [optional] 

### Return type

[**LabelResponse**](LabelResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json, application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | created |  * Location -  <br>  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Insufficient permissions to query endpoint |  -  |
**429** | Exhausted rate limit for the organization |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_endpoint_label**
> delete_endpoint_label(id, aid=aid)

Delete label

Deletes the label from your account. 

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.endpoint_labels
from thousandeyes_sdk.endpoint_labels.rest import ApiException
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
    api_instance = thousandeyes_sdk.endpoint_labels.EndpointAgentLabelsApi(api_client)
    id = 'id_example' # str | The unique identifier of the label to operate on.
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Delete label
        api_instance.delete_endpoint_label(id, aid=aid)
    except Exception as e:
        print("Exception when calling EndpointAgentLabelsApi->delete_endpoint_label: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the label to operate on. | 
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_endpoint_label**
> LabelResponse get_endpoint_label(id, expand=expand, aid=aid)

Retrieve label

Returns a single label using its ID.

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.endpoint_labels
from thousandeyes_sdk.endpoint_labels.models.expand_label_options import ExpandLabelOptions
from thousandeyes_sdk.endpoint_labels.models.label_response import LabelResponse
from thousandeyes_sdk.endpoint_labels.rest import ApiException
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
    api_instance = thousandeyes_sdk.endpoint_labels.EndpointAgentLabelsApi(api_client)
    id = 'id_example' # str | The unique identifier of the label to operate on.
    expand = [thousandeyes_sdk.endpoint_labels.ExpandLabelOptions()] # List[ExpandLabelOptions] | This parameter is optional and determines whether to include additional details in the response. To specify multiple expansions, you can either separate the values with commas or specify the parameter multiple times. (optional)
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Retrieve label
        api_response = api_instance.get_endpoint_label(id, expand=expand, aid=aid)
        print("The response of EndpointAgentLabelsApi->get_endpoint_label:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointAgentLabelsApi->get_endpoint_label: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the label to operate on. | 
 **expand** | [**List[ExpandLabelOptions]**](ExpandLabelOptions.md)| This parameter is optional and determines whether to include additional details in the response. To specify multiple expansions, you can either separate the values with commas or specify the parameter multiple times. | [optional] 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

[**LabelResponse**](LabelResponse.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_endpoint_labels**
> Labels get_endpoint_labels(max=max, cursor=cursor, expand=expand, aid=aid)

List labels

Returns a list of labels.

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.endpoint_labels
from thousandeyes_sdk.endpoint_labels.models.expand_label_options import ExpandLabelOptions
from thousandeyes_sdk.endpoint_labels.models.labels import Labels
from thousandeyes_sdk.endpoint_labels.rest import ApiException
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
    api_instance = thousandeyes_sdk.endpoint_labels.EndpointAgentLabelsApi(api_client)
    max = 5 # int | (Optional) Maximum number of objects to return. (optional)
    cursor = 'cursor_example' # str | (Optional) Opaque cursor used for pagination. Clients should use `next` value from `_links` instead of this parameter. (optional)
    expand = [thousandeyes_sdk.endpoint_labels.ExpandLabelOptions()] # List[ExpandLabelOptions] | This parameter is optional and determines whether to include additional details in the response. To specify multiple expansions, you can either separate the values with commas or specify the parameter multiple times. (optional)
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # List labels
        api_response = api_instance.get_endpoint_labels(max=max, cursor=cursor, expand=expand, aid=aid)
        print("The response of EndpointAgentLabelsApi->get_endpoint_labels:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointAgentLabelsApi->get_endpoint_labels: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **max** | **int**| (Optional) Maximum number of objects to return. | [optional] 
 **cursor** | **str**| (Optional) Opaque cursor used for pagination. Clients should use &#x60;next&#x60; value from &#x60;_links&#x60; instead of this parameter. | [optional] 
 **expand** | [**List[ExpandLabelOptions]**](ExpandLabelOptions.md)| This parameter is optional and determines whether to include additional details in the response. To specify multiple expansions, you can either separate the values with commas or specify the parameter multiple times. | [optional] 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

[**Labels**](Labels.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_endpoint_label**
> LabelResponse update_endpoint_label(id, aid=aid, label=label)

Update label

Updates a label using its ID.

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.endpoint_labels
from thousandeyes_sdk.endpoint_labels.models.label import Label
from thousandeyes_sdk.endpoint_labels.models.label_response import LabelResponse
from thousandeyes_sdk.endpoint_labels.rest import ApiException
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
    api_instance = thousandeyes_sdk.endpoint_labels.EndpointAgentLabelsApi(api_client)
    id = 'id_example' # str | The unique identifier of the label to operate on.
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)
    label = thousandeyes_sdk.endpoint_labels.Label() # Label | Fields to change on the agent (optional)

    try:
        # Update label
        api_response = api_instance.update_endpoint_label(id, aid=aid, label=label)
        print("The response of EndpointAgentLabelsApi->update_endpoint_label:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointAgentLabelsApi->update_endpoint_label: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the label to operate on. | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 
 **label** | [**Label**](Label.md)| Fields to change on the agent | [optional] 

### Return type

[**LabelResponse**](LabelResponse.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

