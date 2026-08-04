# thousandeyes_sdk.connectors.PanoramaConnectorsApi

All URIs are relative to *https://api.thousandeyes.com/v7*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_panorama_connector**](PanoramaConnectorsApi.md#create_panorama_connector) | **POST** /connectors/panorama | Create Panorama connector
[**delete_panorama_connector**](PanoramaConnectorsApi.md#delete_panorama_connector) | **DELETE** /connectors/panorama/{id} | Delete Panorama connector
[**get_panorama_connector**](PanoramaConnectorsApi.md#get_panorama_connector) | **GET** /connectors/panorama/{id} | Retrieve Panorama connector
[**get_panorama_connector_operations**](PanoramaConnectorsApi.md#get_panorama_connector_operations) | **GET** /connectors/panorama/{id}/operations | List operation IDs for Panorama connector
[**get_panorama_connectors**](PanoramaConnectorsApi.md#get_panorama_connectors) | **GET** /connectors/panorama | List Panorama connectors
[**set_panorama_connector_operations**](PanoramaConnectorsApi.md#set_panorama_connector_operations) | **PUT** /connectors/panorama/{id}/operations | Assign operations to Panorama connector
[**update_panorama_connector**](PanoramaConnectorsApi.md#update_panorama_connector) | **PUT** /connectors/panorama/{id} | Update Panorama connector


# **create_panorama_connector**
> PanoramaConnector create_panorama_connector(panorama_connector, aid=aid)

Create Panorama connector

Creates a new Panorama connector.

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.connectors
from thousandeyes_sdk.connectors.models.panorama_connector import PanoramaConnector
from thousandeyes_sdk.connectors.rest import ApiException
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
    api_instance = thousandeyes_sdk.connectors.PanoramaConnectorsApi(api_client)
    panorama_connector = {"type":"panorama","name":"Branch Panorama","target":"https://panorama.example.com","authentication":{"username":"panorama-user","password":"<panorama-password>","keyTtl":40,"type":"pan-key-gen"}} # PanoramaConnector | Panorama connector configuration.
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Create Panorama connector
        api_response = api_instance.create_panorama_connector(panorama_connector, aid=aid)
        print("The response of PanoramaConnectorsApi->create_panorama_connector:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PanoramaConnectorsApi->create_panorama_connector: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **panorama_connector** | [**PanoramaConnector**](PanoramaConnector.md)| Panorama connector configuration. | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

[**PanoramaConnector**](PanoramaConnector.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json, application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The created Panorama connector. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Insufficient permissions to query endpoint |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_panorama_connector**
> delete_panorama_connector(id, aid=aid)

Delete Panorama connector

Deletes the Panorama connector specified by ID.

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.connectors
from thousandeyes_sdk.connectors.rest import ApiException
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
    api_instance = thousandeyes_sdk.connectors.PanoramaConnectorsApi(api_client)
    id = 'cb1b8033-ea2d-4e9b-a920-fe87850693cf' # str | The connector ID.
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Delete Panorama connector
        api_instance.delete_panorama_connector(id, aid=aid)
    except Exception as e:
        print("Exception when calling PanoramaConnectorsApi->delete_panorama_connector: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The connector ID. | 
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
**204** | No Content. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Insufficient permissions to query endpoint |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_panorama_connector**
> PanoramaConnector get_panorama_connector(id, aid=aid)

Retrieve Panorama connector

Retrieves details of a Panorama connector by its ID.

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.connectors
from thousandeyes_sdk.connectors.models.panorama_connector import PanoramaConnector
from thousandeyes_sdk.connectors.rest import ApiException
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
    api_instance = thousandeyes_sdk.connectors.PanoramaConnectorsApi(api_client)
    id = 'cb1b8033-ea2d-4e9b-a920-fe87850693cf' # str | The connector ID.
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Retrieve Panorama connector
        api_response = api_instance.get_panorama_connector(id, aid=aid)
        print("The response of PanoramaConnectorsApi->get_panorama_connector:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PanoramaConnectorsApi->get_panorama_connector: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The connector ID. | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

[**PanoramaConnector**](PanoramaConnector.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json, application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Panorama connector details. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Insufficient permissions to query endpoint |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_panorama_connector_operations**
> Assignments get_panorama_connector_operations(id, aid=aid)

List operation IDs for Panorama connector

Returns a list of operation IDs assigned to a Panorama connector.

### Example

* Bearer Authentication (BearerAuth):

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
    api_instance = thousandeyes_sdk.connectors.PanoramaConnectorsApi(api_client)
    id = 'cb1b8033-ea2d-4e9b-a920-fe87850693cf' # str | The connector ID.
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # List operation IDs for Panorama connector
        api_response = api_instance.get_panorama_connector_operations(id, aid=aid)
        print("The response of PanoramaConnectorsApi->get_panorama_connector_operations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PanoramaConnectorsApi->get_panorama_connector_operations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The connector ID. | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

[**Assignments**](Assignments.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json, application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation IDs assigned to the Panorama connector. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Insufficient permissions to query endpoint |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_panorama_connectors**
> PanoramaConnectors get_panorama_connectors(aid=aid)

List Panorama connectors

Returns a list of Panorama connectors in the specified account group. If no account group is specified, the user’s default account group is used.

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.connectors
from thousandeyes_sdk.connectors.models.panorama_connectors import PanoramaConnectors
from thousandeyes_sdk.connectors.rest import ApiException
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
    api_instance = thousandeyes_sdk.connectors.PanoramaConnectorsApi(api_client)
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # List Panorama connectors
        api_response = api_instance.get_panorama_connectors(aid=aid)
        print("The response of PanoramaConnectorsApi->get_panorama_connectors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PanoramaConnectorsApi->get_panorama_connectors: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

[**PanoramaConnectors**](PanoramaConnectors.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json, application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of Panorama connectors. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Insufficient permissions to query endpoint |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_panorama_connector_operations**
> Assignments set_panorama_connector_operations(id, request_body, aid=aid)

Assign operations to Panorama connector

Assigns operations to a Panorama connector. This replaces any existing assignments. Passing an empty array removes all operation assignments from the connector.

### Example

* Bearer Authentication (BearerAuth):

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
    api_instance = thousandeyes_sdk.connectors.PanoramaConnectorsApi(api_client)
    id = 'cb1b8033-ea2d-4e9b-a920-fe87850693cf' # str | The connector ID.
    request_body = ["ca39314d-eb4f-496f-9435-b5d20b1bfbff","a32cfbab-32f6-41d8-9027-7127cba965dd"] # List[str] | List of operation IDs to assign to the connector.
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Assign operations to Panorama connector
        api_response = api_instance.set_panorama_connector_operations(id, request_body, aid=aid)
        print("The response of PanoramaConnectorsApi->set_panorama_connector_operations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PanoramaConnectorsApi->set_panorama_connector_operations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The connector ID. | 
 **request_body** | [**List[str]**](str.md)| List of operation IDs to assign to the connector. | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

[**Assignments**](Assignments.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

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

# **update_panorama_connector**
> PanoramaConnector update_panorama_connector(id, panorama_connector, aid=aid)

Update Panorama connector

Replaces the Panorama connector specified by ID. The request must include the complete connector configuration, including authentication credentials; existing credentials are not retained when authentication is omitted.

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.connectors
from thousandeyes_sdk.connectors.models.panorama_connector import PanoramaConnector
from thousandeyes_sdk.connectors.rest import ApiException
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
    api_instance = thousandeyes_sdk.connectors.PanoramaConnectorsApi(api_client)
    id = 'cb1b8033-ea2d-4e9b-a920-fe87850693cf' # str | The connector ID.
    panorama_connector = {"type":"panorama","name":"Branch Panorama","target":"https://panorama.example.com","authentication":{"username":"panorama-user","password":"<panorama-password>","keyTtl":40,"type":"pan-key-gen"}} # PanoramaConnector | 
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Update Panorama connector
        api_response = api_instance.update_panorama_connector(id, panorama_connector, aid=aid)
        print("The response of PanoramaConnectorsApi->update_panorama_connector:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PanoramaConnectorsApi->update_panorama_connector: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The connector ID. | 
 **panorama_connector** | [**PanoramaConnector**](PanoramaConnector.md)|  | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

[**PanoramaConnector**](PanoramaConnector.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json, application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated Panorama connector. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Insufficient permissions to query endpoint |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

