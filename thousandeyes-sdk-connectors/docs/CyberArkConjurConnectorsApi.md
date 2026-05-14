# thousandeyes_sdk.connectors.CyberArkConjurConnectorsApi

All URIs are relative to *https://api.thousandeyes.com/v7*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_conjur_connector**](CyberArkConjurConnectorsApi.md#create_conjur_connector) | **POST** /connectors/conjur | Create Conjur connector
[**delete_conjur_connector**](CyberArkConjurConnectorsApi.md#delete_conjur_connector) | **DELETE** /connectors/conjur/{id} | Delete a Conjur connector
[**get_conjur_connector**](CyberArkConjurConnectorsApi.md#get_conjur_connector) | **GET** /connectors/conjur/{id} | Retrieve a Conjur connector
[**get_conjur_connector_operations**](CyberArkConjurConnectorsApi.md#get_conjur_connector_operations) | **GET** /connectors/conjur/{id}/operations | List operation IDs for a Conjur connector
[**get_conjur_connectors**](CyberArkConjurConnectorsApi.md#get_conjur_connectors) | **GET** /connectors/conjur | List Conjur connectors
[**set_conjur_connector_operations**](CyberArkConjurConnectorsApi.md#set_conjur_connector_operations) | **PUT** /connectors/conjur/{id}/operations | Assign operations to a Conjur connector
[**update_conjur_connector**](CyberArkConjurConnectorsApi.md#update_conjur_connector) | **PUT** /connectors/conjur/{id} | Update a Conjur connector


# **create_conjur_connector**
> ConjurConnector create_conjur_connector(conjur_connector, aid=aid)

Create Conjur connector

Creates a new CyberArk Conjur connector.

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.connectors
from thousandeyes_sdk.connectors.models.conjur_connector import ConjurConnector
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
    api_instance = thousandeyes_sdk.connectors.CyberArkConjurConnectorsApi(api_client)
    conjur_connector = thousandeyes_sdk.connectors.ConjurConnector() # ConjurConnector | 
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Create Conjur connector
        api_response = api_instance.create_conjur_connector(conjur_connector, aid=aid)
        print("The response of CyberArkConjurConnectorsApi->create_conjur_connector:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CyberArkConjurConnectorsApi->create_conjur_connector: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conjur_connector** | [**ConjurConnector**](ConjurConnector.md)|  | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

[**ConjurConnector**](ConjurConnector.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json, application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The created Conjur connector. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Insufficient permissions to query endpoint |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_conjur_connector**
> delete_conjur_connector(id, confirm_disabled_objects, aid=aid)

Delete a Conjur connector

Deleted the CyberArk Conjur connector specified by ID. Note: This operation may disable affected objects (such as tests).

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
    api_instance = thousandeyes_sdk.connectors.CyberArkConjurConnectorsApi(api_client)
    id = 'cb1b8033-ea2d-4e9b-a920-fe87850693cf' # str | The connector ID.
    confirm_disabled_objects = False # bool | Confirmation to disable affected objects (for example, tests) for Conjur connectors. (default to False)
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Delete a Conjur connector
        api_instance.delete_conjur_connector(id, confirm_disabled_objects, aid=aid)
    except Exception as e:
        print("Exception when calling CyberArkConjurConnectorsApi->delete_conjur_connector: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The connector ID. | 
 **confirm_disabled_objects** | **bool**| Confirmation to disable affected objects (for example, tests) for Conjur connectors. | [default to False]
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

# **get_conjur_connector**
> ConjurConnector get_conjur_connector(id, aid=aid)

Retrieve a Conjur connector

Retrieves details of a CyberArk Conjur connector by its ID.

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.connectors
from thousandeyes_sdk.connectors.models.conjur_connector import ConjurConnector
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
    api_instance = thousandeyes_sdk.connectors.CyberArkConjurConnectorsApi(api_client)
    id = 'cb1b8033-ea2d-4e9b-a920-fe87850693cf' # str | The connector ID.
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Retrieve a Conjur connector
        api_response = api_instance.get_conjur_connector(id, aid=aid)
        print("The response of CyberArkConjurConnectorsApi->get_conjur_connector:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CyberArkConjurConnectorsApi->get_conjur_connector: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The connector ID. | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

[**ConjurConnector**](ConjurConnector.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json, application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CyberArk Conjur Connector details. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Insufficient permissions to query endpoint |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_conjur_connector_operations**
> Assignments get_conjur_connector_operations(id, aid=aid)

List operation IDs for a Conjur connector

Returns a list of operation IDs assigned to a CyberArk Conjur connector.

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
    api_instance = thousandeyes_sdk.connectors.CyberArkConjurConnectorsApi(api_client)
    id = 'cb1b8033-ea2d-4e9b-a920-fe87850693cf' # str | The connector ID.
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # List operation IDs for a Conjur connector
        api_response = api_instance.get_conjur_connector_operations(id, aid=aid)
        print("The response of CyberArkConjurConnectorsApi->get_conjur_connector_operations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CyberArkConjurConnectorsApi->get_conjur_connector_operations: %s\n" % e)
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
**200** | A list of assigned operation IDs. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Insufficient permissions to query endpoint |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_conjur_connectors**
> ConjurConnectors get_conjur_connectors(aid=aid)

List Conjur connectors

Returns a list of CyberArk Conjur connectors in the specified account group. If no account group is specified, the user’s default account group is used.

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.connectors
from thousandeyes_sdk.connectors.models.conjur_connectors import ConjurConnectors
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
    api_instance = thousandeyes_sdk.connectors.CyberArkConjurConnectorsApi(api_client)
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # List Conjur connectors
        api_response = api_instance.get_conjur_connectors(aid=aid)
        print("The response of CyberArkConjurConnectorsApi->get_conjur_connectors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CyberArkConjurConnectorsApi->get_conjur_connectors: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

[**ConjurConnectors**](ConjurConnectors.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json, application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of Conjur connectors. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Insufficient permissions to query endpoint |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_conjur_connector_operations**
> Assignments set_conjur_connector_operations(id, confirm_disabled_objects, request_body, aid=aid)

Assign operations to a Conjur connector

Assigns operations to a CyberArk Conjur connector. This replaces any existing assignments. Note: This operation may disable affected objects (such as tests) if operations are changed.

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
    api_instance = thousandeyes_sdk.connectors.CyberArkConjurConnectorsApi(api_client)
    id = 'cb1b8033-ea2d-4e9b-a920-fe87850693cf' # str | The connector ID.
    confirm_disabled_objects = False # bool | Confirmation to disable affected objects (for example, tests) for Conjur connectors. (default to False)
    request_body = ["ca39314d-eb4f-496f-9435-b5d20b1bfbff","a32cfbab-32f6-41d8-9027-7127cba965dd"] # List[str] | List of operation IDs to assign to the connector.
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Assign operations to a Conjur connector
        api_response = api_instance.set_conjur_connector_operations(id, confirm_disabled_objects, request_body, aid=aid)
        print("The response of CyberArkConjurConnectorsApi->set_conjur_connector_operations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CyberArkConjurConnectorsApi->set_conjur_connector_operations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The connector ID. | 
 **confirm_disabled_objects** | **bool**| Confirmation to disable affected objects (for example, tests) for Conjur connectors. | [default to False]
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

# **update_conjur_connector**
> ConjurConnector update_conjur_connector(id, conjur_connector, aid=aid)

Update a Conjur connector

Updates the CyberArk Conjur connector specified by ID.

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.connectors
from thousandeyes_sdk.connectors.models.conjur_connector import ConjurConnector
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
    api_instance = thousandeyes_sdk.connectors.CyberArkConjurConnectorsApi(api_client)
    id = 'cb1b8033-ea2d-4e9b-a920-fe87850693cf' # str | The connector ID.
    conjur_connector = thousandeyes_sdk.connectors.ConjurConnector() # ConjurConnector | 
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Update a Conjur connector
        api_response = api_instance.update_conjur_connector(id, conjur_connector, aid=aid)
        print("The response of CyberArkConjurConnectorsApi->update_conjur_connector:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CyberArkConjurConnectorsApi->update_conjur_connector: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The connector ID. | 
 **conjur_connector** | [**ConjurConnector**](ConjurConnector.md)|  | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

[**ConjurConnector**](ConjurConnector.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

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

