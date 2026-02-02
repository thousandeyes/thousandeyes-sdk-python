# thousandeyes_sdk.connectors.OperationConnectorsApi

All URIs are relative to *https://api.thousandeyes.com/v7*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_operation_connectors**](OperationConnectorsApi.md#get_operation_connectors) | **GET** /operations/{type}/{id}/connectors | Retrieve connectors assigned to an operation
[**set_operation_connectors**](OperationConnectorsApi.md#set_operation_connectors) | **PUT** /operations/{type}/{id}/connectors | Assign connectors to an operation


# **get_operation_connectors**
> Assignments get_operation_connectors(type, id, aid=aid)

Retrieve connectors assigned to an operation

Returns a list of connectors assigned to a specific operation.

### Example


```python
import thousandeyes_sdk.connectors
from thousandeyes_sdk.connectors.models.assignments import Assignments
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
    api_instance = thousandeyes_sdk.connectors.OperationConnectorsApi(api_client)
    type = 'webhooks' # str | The operation type.
    id = 'cb1b8033-ea2d-4e9b-a920-fe87850693cf' # str | The operation ID.
    aid = 123456 # float | Account ID (optional)

    try:
        # Retrieve connectors assigned to an operation
        api_response = api_instance.get_operation_connectors(type, id, aid=aid)
        print("The response of OperationConnectorsApi->get_operation_connectors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OperationConnectorsApi->get_operation_connectors: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The operation type. | 
 **id** | **str**| The operation ID. | 
 **aid** | **float**| Account ID | [optional] 

### Return type

[**Assignments**](Assignments.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/hal+json, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | Not found |  -  |
**200** | A list of assigned connectors. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Insufficient permissions to query endpoint |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_operation_connectors**
> Assignments set_operation_connectors(type, id, request_body, aid=aid)

Assign connectors to an operation

Assigns one or more connectors to an operation. This replaces any existing assignments.

### Example


```python
import thousandeyes_sdk.connectors
from thousandeyes_sdk.connectors.models.assignments import Assignments
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
    api_instance = thousandeyes_sdk.connectors.OperationConnectorsApi(api_client)
    type = 'webhooks' # str | The operation type.
    id = 'cb1b8033-ea2d-4e9b-a920-fe87850693cf' # str | The operation ID.
    request_body = ["ca39314d-eb4f-496f-9435-b5d20b1bfbff"] # List[str] | List of connector IDs to assign to the operation.
    aid = 123456 # float | Account ID (optional)

    try:
        # Assign connectors to an operation
        api_response = api_instance.set_operation_connectors(type, id, request_body, aid=aid)
        print("The response of OperationConnectorsApi->set_operation_connectors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OperationConnectorsApi->set_operation_connectors: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The operation type. | 
 **id** | **str**| The operation ID. | 
 **request_body** | [**List[str]**](str.md)| List of connector IDs to assign to the operation. | 
 **aid** | **float**| Account ID | [optional] 

### Return type

[**Assignments**](Assignments.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/problem+json, application/hal+json, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | Not found |  -  |
**200** | Operation Connectors updated successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Insufficient permissions to query endpoint |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

