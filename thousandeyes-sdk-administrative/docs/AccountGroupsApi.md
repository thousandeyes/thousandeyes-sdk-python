# thousandeyes_sdk.administrative.AccountGroupsApi

All URIs are relative to *https://api.thousandeyes.com/v7*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_account_group**](AccountGroupsApi.md#create_account_group) | **POST** /account-groups | Create account group
[**delete_account_group**](AccountGroupsApi.md#delete_account_group) | **DELETE** /account-groups/{id} | Delete account group
[**get_account_group**](AccountGroupsApi.md#get_account_group) | **GET** /account-groups/{id} | Retrieve account group
[**get_account_groups**](AccountGroupsApi.md#get_account_groups) | **GET** /account-groups | List account groups
[**update_account_group**](AccountGroupsApi.md#update_account_group) | **PUT** /account-groups/{id} | Update account group


# **create_account_group**
> CreatedAccountGroup create_account_group(account_group_request, expand=expand)

Create account group

Creates a new account group. This operation requires the `Edit all account groups` permission.  **Note:** Any user assigned to `All Account Groups` is automatically assigned to the new account group.

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.administrative
from thousandeyes_sdk.administrative.models.account_group_request import AccountGroupRequest
from thousandeyes_sdk.administrative.models.created_account_group import CreatedAccountGroup
from thousandeyes_sdk.administrative.models.expand_account_group_options import ExpandAccountGroupOptions
from thousandeyes_sdk.administrative.rest import ApiException
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
    api_instance = thousandeyes_sdk.administrative.AccountGroupsApi(api_client)
    account_group_request = thousandeyes_sdk.administrative.AccountGroupRequest() # AccountGroupRequest | 
    expand = [thousandeyes_sdk.administrative.ExpandAccountGroupOptions()] # List[ExpandAccountGroupOptions] | Optional parameter that specifies whether or not account group related resources should be expanded. By default, no expansion takes place if the query parameter is not passed. For example, to expand the `users` resource, pass the `?expand=user` query. (optional)

    try:
        # Create account group
        api_response = api_instance.create_account_group(account_group_request, expand=expand)
        print("The response of AccountGroupsApi->create_account_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountGroupsApi->create_account_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_group_request** | [**AccountGroupRequest**](AccountGroupRequest.md)|  | 
 **expand** | [**List[ExpandAccountGroupOptions]**](ExpandAccountGroupOptions.md)| Optional parameter that specifies whether or not account group related resources should be expanded. By default, no expansion takes place if the query parameter is not passed. For example, to expand the &#x60;users&#x60; resource, pass the &#x60;?expand&#x3D;user&#x60; query. | [optional] 

### Return type

[**CreatedAccountGroup**](CreatedAccountGroup.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json, application/json, application/problem+json

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

# **delete_account_group**
> delete_account_group(id)

Delete account group

Deletes an account group using its ID. This operation requires the following permissions:    * Assign management permissions   * Delete account   * Edit all account groups

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.administrative
from thousandeyes_sdk.administrative.rest import ApiException
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
    api_instance = thousandeyes_sdk.administrative.AccountGroupsApi(api_client)
    id = '1234' # str | Identifier for the account group.

    try:
        # Delete account group
        api_instance.delete_account_group(id)
    except Exception as e:
        print("Exception when calling AccountGroupsApi->delete_account_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier for the account group. | 

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
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Insufficient permissions to query endpoint |  -  |
**404** | Not found |  -  |
**429** | Exhausted rate limit for the organization |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_group**
> AccountGroupDetail get_account_group(id, expand=expand)

Retrieve account group

Retrieves detailed information about an account group using its ID.  This operation requires the `View all account groups settings` permission.

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.administrative
from thousandeyes_sdk.administrative.models.account_group_detail import AccountGroupDetail
from thousandeyes_sdk.administrative.models.expand_account_group_options import ExpandAccountGroupOptions
from thousandeyes_sdk.administrative.rest import ApiException
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
    api_instance = thousandeyes_sdk.administrative.AccountGroupsApi(api_client)
    id = '1234' # str | Identifier for the account group.
    expand = [thousandeyes_sdk.administrative.ExpandAccountGroupOptions()] # List[ExpandAccountGroupOptions] | Optional parameter that specifies whether or not account group related resources should be expanded. By default, no expansion takes place if the query parameter is not passed. For example, to expand the `users` resource, pass the `?expand=user` query. (optional)

    try:
        # Retrieve account group
        api_response = api_instance.get_account_group(id, expand=expand)
        print("The response of AccountGroupsApi->get_account_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountGroupsApi->get_account_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier for the account group. | 
 **expand** | [**List[ExpandAccountGroupOptions]**](ExpandAccountGroupOptions.md)| Optional parameter that specifies whether or not account group related resources should be expanded. By default, no expansion takes place if the query parameter is not passed. For example, to expand the &#x60;users&#x60; resource, pass the &#x60;?expand&#x3D;user&#x60; query. | [optional] 

### Return type

[**AccountGroupDetail**](AccountGroupDetail.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
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
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_groups**
> AccountGroups get_account_groups()

List account groups

Retrieves a list of account groups available to the current user.

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.administrative
from thousandeyes_sdk.administrative.models.account_groups import AccountGroups
from thousandeyes_sdk.administrative.rest import ApiException
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
    api_instance = thousandeyes_sdk.administrative.AccountGroupsApi(api_client)

    try:
        # List account groups
        api_response = api_instance.get_account_groups()
        print("The response of AccountGroupsApi->get_account_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountGroupsApi->get_account_groups: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AccountGroups**](AccountGroups.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
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
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_account_group**
> AccountGroupDetail update_account_group(id, account_group_request, expand=expand)

Update account group

Updates an account group using its ID. You can modify the account group’s name or the list of agents assigned to the account group.

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.administrative
from thousandeyes_sdk.administrative.models.account_group_detail import AccountGroupDetail
from thousandeyes_sdk.administrative.models.account_group_request import AccountGroupRequest
from thousandeyes_sdk.administrative.models.expand_account_group_options import ExpandAccountGroupOptions
from thousandeyes_sdk.administrative.rest import ApiException
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
    api_instance = thousandeyes_sdk.administrative.AccountGroupsApi(api_client)
    id = '1234' # str | Identifier for the account group.
    account_group_request = thousandeyes_sdk.administrative.AccountGroupRequest() # AccountGroupRequest | 
    expand = [thousandeyes_sdk.administrative.ExpandAccountGroupOptions()] # List[ExpandAccountGroupOptions] | Optional parameter that specifies whether or not account group related resources should be expanded. By default, no expansion takes place if the query parameter is not passed. For example, to expand the `users` resource, pass the `?expand=user` query. (optional)

    try:
        # Update account group
        api_response = api_instance.update_account_group(id, account_group_request, expand=expand)
        print("The response of AccountGroupsApi->update_account_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountGroupsApi->update_account_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier for the account group. | 
 **account_group_request** | [**AccountGroupRequest**](AccountGroupRequest.md)|  | 
 **expand** | [**List[ExpandAccountGroupOptions]**](ExpandAccountGroupOptions.md)| Optional parameter that specifies whether or not account group related resources should be expanded. By default, no expansion takes place if the query parameter is not passed. For example, to expand the &#x60;users&#x60; resource, pass the &#x60;?expand&#x3D;user&#x60; query. | [optional] 

### Return type

[**AccountGroupDetail**](AccountGroupDetail.md)

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
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

