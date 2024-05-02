# endpoint_labels.ManageLabelsApi

All URIs are relative to *https://api.thousandeyes.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**endpoint_label_delete**](ManageLabelsApi.md#endpoint_label_delete) | **DELETE** /v7/endpoint/labels/{id} | Delete label
[**endpoint_label_get**](ManageLabelsApi.md#endpoint_label_get) | **GET** /v7/endpoint/labels/{id} | Retrieve label
[**endpoint_label_update**](ManageLabelsApi.md#endpoint_label_update) | **PATCH** /v7/endpoint/labels/{id} | Update label
[**endpoint_labels_list**](ManageLabelsApi.md#endpoint_labels_list) | **GET** /v7/endpoint/labels | List labels
[**v7_endpoint_labels_post**](ManageLabelsApi.md#v7_endpoint_labels_post) | **POST** /v7/endpoint/labels | Create label


# **endpoint_label_delete**
> endpoint_label_delete(id, aid=aid)

Delete label

Deletes the label from your account. 

### Example

* Bearer Authentication (BearerAuth):

```python
import endpoint_labels
from endpoint_labels.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.thousandeyes.com
# See configuration.py for a list of all supported configuration parameters.
configuration = endpoint_labels.Configuration(
    host = "https://api.thousandeyes.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = endpoint_labels.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with endpoint_labels.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = endpoint_labels.ManageLabelsApi(api_client)
    id = 'id_example' # str | The unique identifier of the label to operate on.
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Delete label
        api_instance.endpoint_label_delete(id, aid=aid)
    except Exception as e:
        print("Exception when calling ManageLabelsApi->endpoint_label_delete: %s\n" % e)
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
 - **Accept**: application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No content |  -  |
**401** | Unauthorized |  -  |
**403** | Insufficient permissions to query endpoint |  -  |
**404** | Not found |  -  |
**429** | Exhausted rate limit for the organization |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoint_label_get**
> V7EndpointLabelsPost201Response endpoint_label_get(id, expand=expand, aid=aid)

Retrieve label

Returns a single label using its ID.

### Example

* Bearer Authentication (BearerAuth):

```python
import endpoint_labels
from endpoint_labels.models.expand import Expand
from endpoint_labels.models.v7_endpoint_labels_post201_response import V7EndpointLabelsPost201Response
from endpoint_labels.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.thousandeyes.com
# See configuration.py for a list of all supported configuration parameters.
configuration = endpoint_labels.Configuration(
    host = "https://api.thousandeyes.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = endpoint_labels.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with endpoint_labels.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = endpoint_labels.ManageLabelsApi(api_client)
    id = 'id_example' # str | The unique identifier of the label to operate on.
    expand = [endpoint_labels.Expand()] # List[Expand] | This parameter is optional and determines whether to include additional details in the response. To specify multiple expansions, you can either separate the values with commas or specify the parameter multiple times. (optional)
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Retrieve label
        api_response = api_instance.endpoint_label_get(id, expand=expand, aid=aid)
        print("The response of ManageLabelsApi->endpoint_label_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManageLabelsApi->endpoint_label_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the label to operate on. | 
 **expand** | [**List[Expand]**](Expand.md)| This parameter is optional and determines whether to include additional details in the response. To specify multiple expansions, you can either separate the values with commas or specify the parameter multiple times. | [optional] 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

[**V7EndpointLabelsPost201Response**](V7EndpointLabelsPost201Response.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoint_label_update**
> V7EndpointLabelsPost201Response endpoint_label_update(id, aid=aid, label=label)

Update label

Updates a label using its ID.

### Example

* Bearer Authentication (BearerAuth):

```python
import endpoint_labels
from endpoint_labels.models.label import Label
from endpoint_labels.models.v7_endpoint_labels_post201_response import V7EndpointLabelsPost201Response
from endpoint_labels.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.thousandeyes.com
# See configuration.py for a list of all supported configuration parameters.
configuration = endpoint_labels.Configuration(
    host = "https://api.thousandeyes.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = endpoint_labels.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with endpoint_labels.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = endpoint_labels.ManageLabelsApi(api_client)
    id = 'id_example' # str | The unique identifier of the label to operate on.
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)
    label = endpoint_labels.Label() # Label | Fields to change on the agent (optional)

    try:
        # Update label
        api_response = api_instance.endpoint_label_update(id, aid=aid, label=label)
        print("The response of ManageLabelsApi->endpoint_label_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManageLabelsApi->endpoint_label_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the label to operate on. | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 
 **label** | [**Label**](Label.md)| Fields to change on the agent | [optional] 

### Return type

[**V7EndpointLabelsPost201Response**](V7EndpointLabelsPost201Response.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoint_labels_list**
> EndpointLabelsList200Response endpoint_labels_list(max=max, cursor=cursor, expand=expand, aid=aid)

List labels

Returns a list of labels.

### Example

* Bearer Authentication (BearerAuth):

```python
import endpoint_labels
from endpoint_labels.models.endpoint_labels_list200_response import EndpointLabelsList200Response
from endpoint_labels.models.expand import Expand
from endpoint_labels.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.thousandeyes.com
# See configuration.py for a list of all supported configuration parameters.
configuration = endpoint_labels.Configuration(
    host = "https://api.thousandeyes.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = endpoint_labels.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with endpoint_labels.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = endpoint_labels.ManageLabelsApi(api_client)
    max = 5 # float | (Optional) Maximum number of objects to return. (optional)
    cursor = 'cursor_example' # str | (Optional) Opaque cursor used for pagination. Clients should use `next` value from `_links` instead of this parameter. (optional)
    expand = [endpoint_labels.Expand()] # List[Expand] | This parameter is optional and determines whether to include additional details in the response. To specify multiple expansions, you can either separate the values with commas or specify the parameter multiple times. (optional)
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # List labels
        api_response = api_instance.endpoint_labels_list(max=max, cursor=cursor, expand=expand, aid=aid)
        print("The response of ManageLabelsApi->endpoint_labels_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManageLabelsApi->endpoint_labels_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **max** | **float**| (Optional) Maximum number of objects to return. | [optional] 
 **cursor** | **str**| (Optional) Opaque cursor used for pagination. Clients should use &#x60;next&#x60; value from &#x60;_links&#x60; instead of this parameter. | [optional] 
 **expand** | [**List[Expand]**](Expand.md)| This parameter is optional and determines whether to include additional details in the response. To specify multiple expansions, you can either separate the values with commas or specify the parameter multiple times. | [optional] 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

[**EndpointLabelsList200Response**](EndpointLabelsList200Response.md)

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
**429** | Exhausted rate limit for the organization |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v7_endpoint_labels_post**
> V7EndpointLabelsPost201Response v7_endpoint_labels_post(aid=aid, label_request=label_request)

Create label

Creates a new label.

### Example

* Bearer Authentication (BearerAuth):

```python
import endpoint_labels
from endpoint_labels.models.label_request import LabelRequest
from endpoint_labels.models.v7_endpoint_labels_post201_response import V7EndpointLabelsPost201Response
from endpoint_labels.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.thousandeyes.com
# See configuration.py for a list of all supported configuration parameters.
configuration = endpoint_labels.Configuration(
    host = "https://api.thousandeyes.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = endpoint_labels.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with endpoint_labels.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = endpoint_labels.ManageLabelsApi(api_client)
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)
    label_request = endpoint_labels.LabelRequest() # LabelRequest | Label settings (optional)

    try:
        # Create label
        api_response = api_instance.v7_endpoint_labels_post(aid=aid, label_request=label_request)
        print("The response of ManageLabelsApi->v7_endpoint_labels_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManageLabelsApi->v7_endpoint_labels_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 
 **label_request** | [**LabelRequest**](LabelRequest.md)| Label settings | [optional] 

### Return type

[**V7EndpointLabelsPost201Response**](V7EndpointLabelsPost201Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | created |  * Location -  <br>  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Insufficient permissions to query endpoint |  -  |
**429** | Exhausted rate limit for the organization |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

