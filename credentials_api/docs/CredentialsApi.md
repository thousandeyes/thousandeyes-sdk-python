# credentials_api.CredentialsApi

All URIs are relative to *https://api.thousandeyes.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_transaction_tests_credential**](CredentialsApi.md#create_transaction_tests_credential) | **POST** /v7/credentials | Create credential
[**delete_transaction_tests_credential**](CredentialsApi.md#delete_transaction_tests_credential) | **DELETE** /v7/credentials/{id} | Delete credential
[**get_transaction_tests_credential_details**](CredentialsApi.md#get_transaction_tests_credential_details) | **GET** /v7/credentials/{id} | Retrieve credential
[**get_transaction_tests_credentials_list**](CredentialsApi.md#get_transaction_tests_credentials_list) | **GET** /v7/credentials | List credentials
[**update_transaction_tests_credential**](CredentialsApi.md#update_transaction_tests_credential) | **PUT** /v7/credentials/{id} | Update credential


# **create_transaction_tests_credential**
> CredentialWithoutValue create_transaction_tests_credential(credential_request, aid=aid)

Create credential

Creates a new credential for ThousandEyes transaction tests, based on properties provided in the request data. To create a new credential, you must have permission to update tests.

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import credentials_api
from credentials_api.models.credential_request import CredentialRequest
from credentials_api.models.credential_without_value import CredentialWithoutValue
from credentials_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.thousandeyes.com
# See configuration.py for a list of all supported configuration parameters.
configuration = credentials_api.Configuration(
    host = "https://api.thousandeyes.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = credentials_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with credentials_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = credentials_api.CredentialsApi(api_client)
    credential_request = credentials_api.CredentialRequest() # CredentialRequest | 
    aid = '2067' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Create credential
        api_response = api_instance.create_transaction_tests_credential(credential_request, aid=aid)
        print("The response of CredentialsApi->create_transaction_tests_credential:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->create_transaction_tests_credential: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credential_request** | [**CredentialRequest**](CredentialRequest.md)|  | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

[**CredentialWithoutValue**](CredentialWithoutValue.md)

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

# **delete_transaction_tests_credential**
> delete_transaction_tests_credential(id, aid=aid)

Delete credential

Deletes a ThousandEyes transaction test credential, using the request parameters. To delete a credential, you must have permission to update tests and access to the credential based on its default or provided account ID.

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import credentials_api
from credentials_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.thousandeyes.com
# See configuration.py for a list of all supported configuration parameters.
configuration = credentials_api.Configuration(
    host = "https://api.thousandeyes.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = credentials_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with credentials_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = credentials_api.CredentialsApi(api_client)
    id = '3247' # str | The ID of the desired credential.
    aid = '2067' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Delete credential
        api_instance.delete_transaction_tests_credential(id, aid=aid)
    except Exception as e:
        print("Exception when calling CredentialsApi->delete_transaction_tests_credential: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the desired credential. | 
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
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transaction_tests_credential_details**
> Credential get_transaction_tests_credential_details(id, aid=aid)

Retrieve credential

Retrieves detailed information about a ThousandEyes transaction test credential. To access this information, you must have access to the credential based on its default or provided account ID.

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import credentials_api
from credentials_api.models.credential import Credential
from credentials_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.thousandeyes.com
# See configuration.py for a list of all supported configuration parameters.
configuration = credentials_api.Configuration(
    host = "https://api.thousandeyes.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = credentials_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with credentials_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = credentials_api.CredentialsApi(api_client)
    id = '3247' # str | The ID of the desired credential.
    aid = '2067' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Retrieve credential
        api_response = api_instance.get_transaction_tests_credential_details(id, aid=aid)
        print("The response of CredentialsApi->get_transaction_tests_credential_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->get_transaction_tests_credential_details: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the desired credential. | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

[**Credential**](Credential.md)

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

# **get_transaction_tests_credentials_list**
> GetTransactionTestsCredentialsList200Response get_transaction_tests_credentials_list(aid=aid)

List credentials

Retrieves a list of credentials configured in ThousandEyes. Users have access to the list of credentials based on the default settings or the specified account ID.

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import credentials_api
from credentials_api.models.get_transaction_tests_credentials_list200_response import GetTransactionTestsCredentialsList200Response
from credentials_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.thousandeyes.com
# See configuration.py for a list of all supported configuration parameters.
configuration = credentials_api.Configuration(
    host = "https://api.thousandeyes.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = credentials_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with credentials_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = credentials_api.CredentialsApi(api_client)
    aid = '2067' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # List credentials
        api_response = api_instance.get_transaction_tests_credentials_list(aid=aid)
        print("The response of CredentialsApi->get_transaction_tests_credentials_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->get_transaction_tests_credentials_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

[**GetTransactionTestsCredentialsList200Response**](GetTransactionTestsCredentialsList200Response.md)

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
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_transaction_tests_credential**
> CredentialWithoutValue update_transaction_tests_credential(id, credential_request, aid=aid)

Update credential

Updates the credential for ThousandEyes transaction tests, based on properties provided in the request data. To update a credential, you must have permission to update tests and access to the credential based on its default or provided account ID.

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import credentials_api
from credentials_api.models.credential_request import CredentialRequest
from credentials_api.models.credential_without_value import CredentialWithoutValue
from credentials_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.thousandeyes.com
# See configuration.py for a list of all supported configuration parameters.
configuration = credentials_api.Configuration(
    host = "https://api.thousandeyes.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = credentials_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with credentials_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = credentials_api.CredentialsApi(api_client)
    id = '3247' # str | The ID of the desired credential.
    credential_request = credentials_api.CredentialRequest() # CredentialRequest | 
    aid = '2067' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Update credential
        api_response = api_instance.update_transaction_tests_credential(id, credential_request, aid=aid)
        print("The response of CredentialsApi->update_transaction_tests_credential:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->update_transaction_tests_credential: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the desired credential. | 
 **credential_request** | [**CredentialRequest**](CredentialRequest.md)|  | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

[**CredentialWithoutValue**](CredentialWithoutValue.md)

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

