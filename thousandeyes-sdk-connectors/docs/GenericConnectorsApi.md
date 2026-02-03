# thousandeyes_sdk.connectors.GenericConnectorsApi

All URIs are relative to *https://api.thousandeyes.com/v7*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_generic_connector**](GenericConnectorsApi.md#create_generic_connector) | **POST** /connectors/generic | Create connector
[**delete_generic_connector**](GenericConnectorsApi.md#delete_generic_connector) | **DELETE** /connectors/generic/{id} | Delete connector
[**get_generic_connector**](GenericConnectorsApi.md#get_generic_connector) | **GET** /connectors/generic/{id} | Retrieve connector
[**get_generic_connectors**](GenericConnectorsApi.md#get_generic_connectors) | **GET** /connectors/generic | List connectors
[**list_generic_connector_operations**](GenericConnectorsApi.md#list_generic_connector_operations) | **GET** /connectors/generic/{id}/operations | List operation IDs assigned to a connector
[**set_generic_connector_operations**](GenericConnectorsApi.md#set_generic_connector_operations) | **PUT** /connectors/generic/{id}/operations | Assign operations to a connector
[**update_generic_connector**](GenericConnectorsApi.md#update_generic_connector) | **PUT** /connectors/generic/{id} | Update connector


# **create_generic_connector**
> GenericConnector create_generic_connector(generic_connector, aid=aid)

Create connector

Creates a new connector.

### Example


```python
import thousandeyes_sdk.connectors
from thousandeyes_sdk.connectors.models.generic_connector import GenericConnector
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
    api_instance = thousandeyes_sdk.connectors.GenericConnectorsApi(api_client)
    generic_connector = thousandeyes_sdk.connectors.GenericConnector() # GenericConnector | 
    aid = 123456 # float | Account ID (optional)

    try:
        # Create connector
        api_response = api_instance.create_generic_connector(generic_connector, aid=aid)
        print("The response of GenericConnectorsApi->create_generic_connector:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenericConnectorsApi->create_generic_connector: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **generic_connector** | [**GenericConnector**](GenericConnector.md)|  | 
 **aid** | **float**| Account ID | [optional] 

### Return type

[**GenericConnector**](GenericConnector.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json, application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The created connector. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Insufficient permissions to query endpoint |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_generic_connector**
> delete_generic_connector(id, aid=aid)

Delete connector

Deletes the connector specified by ID.

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
    api_instance = thousandeyes_sdk.connectors.GenericConnectorsApi(api_client)
    id = 'cb1b8033-ea2d-4e9b-a920-fe87850693cf' # str | The connector ID.
    aid = 123456 # float | Account ID (optional)

    try:
        # Delete connector
        api_instance.delete_generic_connector(id, aid=aid)
    except Exception as e:
        print("Exception when calling GenericConnectorsApi->delete_generic_connector: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The connector ID. | 
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

# **get_generic_connector**
> GenericConnector get_generic_connector(id, aid=aid)

Retrieve connector

Retrieves details of a connector by its ID.

### Example


```python
import thousandeyes_sdk.connectors
from thousandeyes_sdk.connectors.models.generic_connector import GenericConnector
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
    api_instance = thousandeyes_sdk.connectors.GenericConnectorsApi(api_client)
    id = 'cb1b8033-ea2d-4e9b-a920-fe87850693cf' # str | The connector ID.
    aid = 123456 # float | Account ID (optional)

    try:
        # Retrieve connector
        api_response = api_instance.get_generic_connector(id, aid=aid)
        print("The response of GenericConnectorsApi->get_generic_connector:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenericConnectorsApi->get_generic_connector: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The connector ID. | 
 **aid** | **float**| Account ID | [optional] 

### Return type

[**GenericConnector**](GenericConnector.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json, application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Connector details. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Insufficient permissions to query endpoint |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_generic_connectors**
> GenericConnectors get_generic_connectors(aid=aid)

List connectors

Returns a list of connectors in the specified account group. If no account group is specified, the user’s default account group is used.

### Example


```python
import thousandeyes_sdk.connectors
from thousandeyes_sdk.connectors.models.generic_connectors import GenericConnectors
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
    api_instance = thousandeyes_sdk.connectors.GenericConnectorsApi(api_client)
    aid = 123456 # float | Account ID (optional)

    try:
        # List connectors
        api_response = api_instance.get_generic_connectors(aid=aid)
        print("The response of GenericConnectorsApi->get_generic_connectors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenericConnectorsApi->get_generic_connectors: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aid** | **float**| Account ID | [optional] 

### Return type

[**GenericConnectors**](GenericConnectors.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json, application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of connectors. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Insufficient permissions to query endpoint |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_generic_connector_operations**
> Assignments list_generic_connector_operations(id, aid=aid)

List operation IDs assigned to a connector

Returns a list of operation IDs assigned to a connector.

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
    api_instance = thousandeyes_sdk.connectors.GenericConnectorsApi(api_client)
    id = 'cb1b8033-ea2d-4e9b-a920-fe87850693cf' # str | The connector ID.
    aid = 123456 # float | Account ID (optional)

    try:
        # List operation IDs assigned to a connector
        api_response = api_instance.list_generic_connector_operations(id, aid=aid)
        print("The response of GenericConnectorsApi->list_generic_connector_operations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenericConnectorsApi->list_generic_connector_operations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The connector ID. | 
 **aid** | **float**| Account ID | [optional] 

### Return type

[**Assignments**](Assignments.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json, application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of assigned operation IDs. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Insufficient permissions to query endpoint |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_generic_connector_operations**
> Assignments set_generic_connector_operations(id, request_body, aid=aid)

Assign operations to a connector

Assigns operations to a connector. This replaces any existing assignments.

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
    api_instance = thousandeyes_sdk.connectors.GenericConnectorsApi(api_client)
    id = 'cb1b8033-ea2d-4e9b-a920-fe87850693cf' # str | The connector ID.
    request_body = ["ca39314d-eb4f-496f-9435-b5d20b1bfbff","a32cfbab-32f6-41d8-9027-7127cba965dd"] # List[str] | List of operation IDs to assign to the connector.
    aid = 123456 # float | Account ID (optional)

    try:
        # Assign operations to a connector
        api_response = api_instance.set_generic_connector_operations(id, request_body, aid=aid)
        print("The response of GenericConnectorsApi->set_generic_connector_operations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenericConnectorsApi->set_generic_connector_operations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The connector ID. | 
 **request_body** | [**List[str]**](str.md)| List of operation IDs to assign to the connector. | 
 **aid** | **float**| Account ID | [optional] 

### Return type

[**Assignments**](Assignments.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json, application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operations assigned successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Insufficient permissions to query endpoint |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_generic_connector**
> GenericConnector update_generic_connector(id, generic_connector, aid=aid)

Update connector

Updates the connector specified by ID.

### Example


```python
import thousandeyes_sdk.connectors
from thousandeyes_sdk.connectors.models.generic_connector import GenericConnector
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
    api_instance = thousandeyes_sdk.connectors.GenericConnectorsApi(api_client)
    id = 'cb1b8033-ea2d-4e9b-a920-fe87850693cf' # str | The connector ID.
    generic_connector = thousandeyes_sdk.connectors.GenericConnector() # GenericConnector | 
    aid = 123456 # float | Account ID (optional)

    try:
        # Update connector
        api_response = api_instance.update_generic_connector(id, generic_connector, aid=aid)
        print("The response of GenericConnectorsApi->update_generic_connector:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenericConnectorsApi->update_generic_connector: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The connector ID. | 
 **generic_connector** | [**GenericConnector**](GenericConnector.md)|  | 
 **aid** | **float**| Account ID | [optional] 

### Return type

[**GenericConnector**](GenericConnector.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json, application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated connector. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Insufficient permissions to query endpoint |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

