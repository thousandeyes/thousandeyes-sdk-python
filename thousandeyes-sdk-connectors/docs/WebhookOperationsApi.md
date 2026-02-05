# thousandeyes_sdk.connectors.WebhookOperationsApi

All URIs are relative to *https://api.thousandeyes.com/v7*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_webhook_operation**](WebhookOperationsApi.md#create_webhook_operation) | **POST** /operations/webhooks | Create webhook operation
[**delete_webhook_operation**](WebhookOperationsApi.md#delete_webhook_operation) | **DELETE** /operations/webhooks/{id} | Delete webhook operation
[**get_webhook_operation**](WebhookOperationsApi.md#get_webhook_operation) | **GET** /operations/webhooks/{id} | Retrieve webhook operation
[**get_webhook_operations**](WebhookOperationsApi.md#get_webhook_operations) | **GET** /operations/webhooks | List webhook operations
[**update_webhook_operation**](WebhookOperationsApi.md#update_webhook_operation) | **PUT** /operations/webhooks/{id} | Update webhook operation


# **create_webhook_operation**
> WebhookOperation create_webhook_operation(webhook_operation, aid=aid)

Create webhook operation

Creates a new webhook operation.

### Example


```python
import thousandeyes_sdk.connectors
from thousandeyes_sdk.connectors.models.webhook_operation import WebhookOperation
from thousandeyes_sdk.connectors.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.thousandeyes.com/v7
# See configuration.py for a list of all supported configuration parameters.
configuration = thousandeyes_sdk.core.Configuration(
    host = "https://api.thousandeyes.com/v7"
)


# Enter a context with an instance of the API client
with thousandeyes_sdk.core.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = thousandeyes_sdk.connectors.WebhookOperationsApi(api_client)
    webhook_operation = thousandeyes_sdk.connectors.WebhookOperation() # WebhookOperation | 
    aid = 123456 # float | Account ID (optional)

    try:
        # Create webhook operation
        api_response = api_instance.create_webhook_operation(webhook_operation, aid=aid)
        print("The response of WebhookOperationsApi->create_webhook_operation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookOperationsApi->create_webhook_operation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_operation** | [**WebhookOperation**](WebhookOperation.md)|  | 
 **aid** | **float**| Account ID | [optional] 

### Return type

[**WebhookOperation**](WebhookOperation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json, application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The created webhook operation. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Insufficient permissions to query endpoint |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_webhook_operation**
> delete_webhook_operation(id, aid=aid)

Delete webhook operation

Deletes the webhook operation specified by ID.

### Example


```python
import thousandeyes_sdk.connectors
from thousandeyes_sdk.connectors.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.thousandeyes.com/v7
# See configuration.py for a list of all supported configuration parameters.
configuration = thousandeyes_sdk.core.Configuration(
    host = "https://api.thousandeyes.com/v7"
)


# Enter a context with an instance of the API client
with thousandeyes_sdk.core.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = thousandeyes_sdk.connectors.WebhookOperationsApi(api_client)
    id = 'cb1b8033-ea2d-4e9b-a920-fe87850693cf' # str | The operation ID.
    aid = 123456 # float | Account ID (optional)

    try:
        # Delete webhook operation
        api_instance.delete_webhook_operation(id, aid=aid)
    except Exception as e:
        print("Exception when calling WebhookOperationsApi->delete_webhook_operation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The operation ID. | 
 **aid** | **float**| Account ID | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Insufficient permissions to query endpoint |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_webhook_operation**
> WebhookOperation get_webhook_operation(id, aid=aid)

Retrieve webhook operation

Retrieves details of a webhook operation by its ID.

### Example


```python
import thousandeyes_sdk.connectors
from thousandeyes_sdk.connectors.models.webhook_operation import WebhookOperation
from thousandeyes_sdk.connectors.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.thousandeyes.com/v7
# See configuration.py for a list of all supported configuration parameters.
configuration = thousandeyes_sdk.core.Configuration(
    host = "https://api.thousandeyes.com/v7"
)


# Enter a context with an instance of the API client
with thousandeyes_sdk.core.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = thousandeyes_sdk.connectors.WebhookOperationsApi(api_client)
    id = 'cb1b8033-ea2d-4e9b-a920-fe87850693cf' # str | The operation ID.
    aid = 123456 # float | Account ID (optional)

    try:
        # Retrieve webhook operation
        api_response = api_instance.get_webhook_operation(id, aid=aid)
        print("The response of WebhookOperationsApi->get_webhook_operation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookOperationsApi->get_webhook_operation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The operation ID. | 
 **aid** | **float**| Account ID | [optional] 

### Return type

[**WebhookOperation**](WebhookOperation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json, application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Webhook operation with the given id. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Insufficient permissions to query endpoint |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_webhook_operations**
> WebhookOperations get_webhook_operations(aid=aid)

List webhook operations

Returns a list of webhook operations in the specified account group. If no account group is specified, the user’s default account group is used.

### Example


```python
import thousandeyes_sdk.connectors
from thousandeyes_sdk.connectors.models.webhook_operations import WebhookOperations
from thousandeyes_sdk.connectors.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.thousandeyes.com/v7
# See configuration.py for a list of all supported configuration parameters.
configuration = thousandeyes_sdk.core.Configuration(
    host = "https://api.thousandeyes.com/v7"
)


# Enter a context with an instance of the API client
with thousandeyes_sdk.core.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = thousandeyes_sdk.connectors.WebhookOperationsApi(api_client)
    aid = 123456 # float | Account ID (optional)

    try:
        # List webhook operations
        api_response = api_instance.get_webhook_operations(aid=aid)
        print("The response of WebhookOperationsApi->get_webhook_operations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookOperationsApi->get_webhook_operations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aid** | **float**| Account ID | [optional] 

### Return type

[**WebhookOperations**](WebhookOperations.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json, application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of webhook operations. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Insufficient permissions to query endpoint |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_webhook_operation**
> WebhookOperation update_webhook_operation(id, webhook_operation, aid=aid)

Update webhook operation

Updates the webhook operation specified by ID.

### Example


```python
import thousandeyes_sdk.connectors
from thousandeyes_sdk.connectors.models.webhook_operation import WebhookOperation
from thousandeyes_sdk.connectors.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.thousandeyes.com/v7
# See configuration.py for a list of all supported configuration parameters.
configuration = thousandeyes_sdk.core.Configuration(
    host = "https://api.thousandeyes.com/v7"
)


# Enter a context with an instance of the API client
with thousandeyes_sdk.core.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = thousandeyes_sdk.connectors.WebhookOperationsApi(api_client)
    id = 'cb1b8033-ea2d-4e9b-a920-fe87850693cf' # str | The operation ID.
    webhook_operation = thousandeyes_sdk.connectors.WebhookOperation() # WebhookOperation | 
    aid = 123456 # float | Account ID (optional)

    try:
        # Update webhook operation
        api_response = api_instance.update_webhook_operation(id, webhook_operation, aid=aid)
        print("The response of WebhookOperationsApi->update_webhook_operation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookOperationsApi->update_webhook_operation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The operation ID. | 
 **webhook_operation** | [**WebhookOperation**](WebhookOperation.md)|  | 
 **aid** | **float**| Account ID | [optional] 

### Return type

[**WebhookOperation**](WebhookOperation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json, application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated webhook operation. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Insufficient permissions to query endpoint |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

