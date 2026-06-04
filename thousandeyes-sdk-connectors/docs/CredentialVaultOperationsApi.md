# thousandeyes_sdk.connectors.CredentialVaultOperationsApi

All URIs are relative to *https://api.thousandeyes.com/v7*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_credential_vault_operation**](CredentialVaultOperationsApi.md#create_credential_vault_operation) | **POST** /operations/credential-vault | Create Credential Vault operation
[**delete_credential_vault_operation**](CredentialVaultOperationsApi.md#delete_credential_vault_operation) | **DELETE** /operations/credential-vault/{id} | Delete Credential Vault operation
[**get_credential_vault_operation**](CredentialVaultOperationsApi.md#get_credential_vault_operation) | **GET** /operations/credential-vault/{id} | Get Credential Vault operation
[**get_credential_vault_operations**](CredentialVaultOperationsApi.md#get_credential_vault_operations) | **GET** /operations/credential-vault | List Credential Vault operations
[**update_credential_vault_operation**](CredentialVaultOperationsApi.md#update_credential_vault_operation) | **PUT** /operations/credential-vault/{id} | Update Credential Vault operation


# **create_credential_vault_operation**
> CredentialVaultOperation create_credential_vault_operation(credential_vault_operation, aid=aid)

Create Credential Vault operation

Create a new Credential Vault operation.

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.connectors
from thousandeyes_sdk.connectors.models.credential_vault_operation import CredentialVaultOperation
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
    api_instance = thousandeyes_sdk.connectors.CredentialVaultOperationsApi(api_client)
    credential_vault_operation = thousandeyes_sdk.connectors.CredentialVaultOperation() # CredentialVaultOperation | 
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Create Credential Vault operation
        api_response = api_instance.create_credential_vault_operation(credential_vault_operation, aid=aid)
        print("The response of CredentialVaultOperationsApi->create_credential_vault_operation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialVaultOperationsApi->create_credential_vault_operation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credential_vault_operation** | [**CredentialVaultOperation**](CredentialVaultOperation.md)|  | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

[**CredentialVaultOperation**](CredentialVaultOperation.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json, application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The created Credential Vault operation. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Insufficient permissions to query endpoint |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_credential_vault_operation**
> delete_credential_vault_operation(id, confirm_disabled_objects, aid=aid)

Delete Credential Vault operation

Delete a single Credential Vault operation by its ID. Note: This operation may disable affected objects (such as tests).

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
    api_instance = thousandeyes_sdk.connectors.CredentialVaultOperationsApi(api_client)
    id = 'cb1b8033-ea2d-4e9b-a920-fe87850693cf' # str | The operation ID.
    confirm_disabled_objects = False # bool | Confirmation to disable affected objects (for example, tests) for credential-vault operations. (default to False)
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Delete Credential Vault operation
        api_instance.delete_credential_vault_operation(id, confirm_disabled_objects, aid=aid)
    except Exception as e:
        print("Exception when calling CredentialVaultOperationsApi->delete_credential_vault_operation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The operation ID. | 
 **confirm_disabled_objects** | **bool**| Confirmation to disable affected objects (for example, tests) for credential-vault operations. | [default to False]
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

# **get_credential_vault_operation**
> CredentialVaultOperation get_credential_vault_operation(id, aid=aid)

Get Credential Vault operation

Retrieve a single Credential Vault operation by its ID.

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.connectors
from thousandeyes_sdk.connectors.models.credential_vault_operation import CredentialVaultOperation
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
    api_instance = thousandeyes_sdk.connectors.CredentialVaultOperationsApi(api_client)
    id = 'cb1b8033-ea2d-4e9b-a920-fe87850693cf' # str | The operation ID.
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Get Credential Vault operation
        api_response = api_instance.get_credential_vault_operation(id, aid=aid)
        print("The response of CredentialVaultOperationsApi->get_credential_vault_operation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialVaultOperationsApi->get_credential_vault_operation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The operation ID. | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

[**CredentialVaultOperation**](CredentialVaultOperation.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json, application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Credential Vault operation details. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Insufficient permissions to query endpoint |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_credential_vault_operations**
> CredentialVaultOperations get_credential_vault_operations(aid=aid)

List Credential Vault operations

Returns a list of Credential Vault operations in the specified account group. If no account group is specified, the user's default account group is used.

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.connectors
from thousandeyes_sdk.connectors.models.credential_vault_operations import CredentialVaultOperations
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
    api_instance = thousandeyes_sdk.connectors.CredentialVaultOperationsApi(api_client)
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # List Credential Vault operations
        api_response = api_instance.get_credential_vault_operations(aid=aid)
        print("The response of CredentialVaultOperationsApi->get_credential_vault_operations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialVaultOperationsApi->get_credential_vault_operations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

[**CredentialVaultOperations**](CredentialVaultOperations.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json, application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of Credential Vault operations. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Insufficient permissions to query endpoint |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_credential_vault_operation**
> CredentialVaultOperation update_credential_vault_operation(id, credential_vault_operation, aid=aid)

Update Credential Vault operation

Update a single existing Credential Vault operation.

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.connectors
from thousandeyes_sdk.connectors.models.credential_vault_operation import CredentialVaultOperation
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
    api_instance = thousandeyes_sdk.connectors.CredentialVaultOperationsApi(api_client)
    id = 'cb1b8033-ea2d-4e9b-a920-fe87850693cf' # str | The operation ID.
    credential_vault_operation = thousandeyes_sdk.connectors.CredentialVaultOperation() # CredentialVaultOperation | 
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Update Credential Vault operation
        api_response = api_instance.update_credential_vault_operation(id, credential_vault_operation, aid=aid)
        print("The response of CredentialVaultOperationsApi->update_credential_vault_operation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialVaultOperationsApi->update_credential_vault_operation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The operation ID. | 
 **credential_vault_operation** | [**CredentialVaultOperation**](CredentialVaultOperation.md)|  | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

[**CredentialVaultOperation**](CredentialVaultOperation.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json, application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated Credential Vault operation. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Insufficient permissions to query endpoint |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

