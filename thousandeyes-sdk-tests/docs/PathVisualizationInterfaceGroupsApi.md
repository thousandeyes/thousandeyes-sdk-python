# thousandeyes_sdk.tests.PathVisualizationInterfaceGroupsApi

All URIs are relative to *https://api.thousandeyes.com/v7*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_path_vis_interface_groups**](PathVisualizationInterfaceGroupsApi.md#create_path_vis_interface_groups) | **POST** /network/path-vis/interface-groups | Create interface group for path visualization
[**delete_path_vis_interface_group**](PathVisualizationInterfaceGroupsApi.md#delete_path_vis_interface_group) | **DELETE** /network/path-vis/interface-groups/{interfaceGroupId} | Delete interface group
[**get_path_vis_interface_groups**](PathVisualizationInterfaceGroupsApi.md#get_path_vis_interface_groups) | **GET** /network/path-vis/interface-groups | List interface groups for path visualization
[**update_path_vis_interface_group**](PathVisualizationInterfaceGroupsApi.md#update_path_vis_interface_group) | **PUT** /network/path-vis/interface-groups/{interfaceGroupId} | Update interface group


# **create_path_vis_interface_groups**
> InterfaceGroup create_path_vis_interface_groups(interface_group, aid=aid)

Create interface group for path visualization

Creates a new path visualization interface group.

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.tests
from thousandeyes_sdk.tests.models.interface_group import InterfaceGroup
from thousandeyes_sdk.tests.rest import ApiException
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
    api_instance = thousandeyes_sdk.tests.PathVisualizationInterfaceGroupsApi(api_client)
    interface_group = thousandeyes_sdk.tests.InterfaceGroup() # InterfaceGroup | 
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Create interface group for path visualization
        api_response = api_instance.create_path_vis_interface_groups(interface_group, aid=aid)
        print("The response of PathVisualizationInterfaceGroupsApi->create_path_vis_interface_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PathVisualizationInterfaceGroupsApi->create_path_vis_interface_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **interface_group** | [**InterfaceGroup**](InterfaceGroup.md)|  | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

[**InterfaceGroup**](InterfaceGroup.md)

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
**502** | Bad Gateway |  -  |
**0** | An error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_path_vis_interface_group**
> delete_path_vis_interface_group(interface_group_id, aid=aid)

Delete interface group

Deletes a path visualization interface group.

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.tests
from thousandeyes_sdk.tests.rest import ApiException
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
    api_instance = thousandeyes_sdk.tests.PathVisualizationInterfaceGroupsApi(api_client)
    interface_group_id = '281474976710706' # str | ID of the network path vis interface group
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Delete interface group
        api_instance.delete_path_vis_interface_group(interface_group_id, aid=aid)
    except Exception as e:
        print("Exception when calling PathVisualizationInterfaceGroupsApi->delete_path_vis_interface_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **interface_group_id** | **str**| ID of the network path vis interface group | 
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
**502** | Bad Gateway |  -  |
**0** | An error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_path_vis_interface_groups**
> InterfaceGroups get_path_vis_interface_groups(aid=aid)

List interface groups for path visualization

Returns a list of all path visualization interface groups. For more information about interface groups, see https://docs.thousandeyes.com/product-documentation/end-user-monitoring/viewing-data/endpoint-agent-views-reference#grouping.

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.tests
from thousandeyes_sdk.tests.models.interface_groups import InterfaceGroups
from thousandeyes_sdk.tests.rest import ApiException
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
    api_instance = thousandeyes_sdk.tests.PathVisualizationInterfaceGroupsApi(api_client)
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # List interface groups for path visualization
        api_response = api_instance.get_path_vis_interface_groups(aid=aid)
        print("The response of PathVisualizationInterfaceGroupsApi->get_path_vis_interface_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PathVisualizationInterfaceGroupsApi->get_path_vis_interface_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

[**InterfaceGroups**](InterfaceGroups.md)

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
**500** | Internal server error |  -  |
**502** | Bad Gateway |  -  |
**0** | An error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_path_vis_interface_group**
> InterfaceGroup update_path_vis_interface_group(interface_group_id, interface_group, aid=aid)

Update interface group

Updates a path visualization interface group..

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.tests
from thousandeyes_sdk.tests.models.interface_group import InterfaceGroup
from thousandeyes_sdk.tests.rest import ApiException
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
    api_instance = thousandeyes_sdk.tests.PathVisualizationInterfaceGroupsApi(api_client)
    interface_group_id = '281474976710706' # str | ID of the network path vis interface group
    interface_group = thousandeyes_sdk.tests.InterfaceGroup() # InterfaceGroup | 
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Update interface group
        api_response = api_instance.update_path_vis_interface_group(interface_group_id, interface_group, aid=aid)
        print("The response of PathVisualizationInterfaceGroupsApi->update_path_vis_interface_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PathVisualizationInterfaceGroupsApi->update_path_vis_interface_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **interface_group_id** | **str**| ID of the network path vis interface group | 
 **interface_group** | [**InterfaceGroup**](InterfaceGroup.md)|  | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

[**InterfaceGroup**](InterfaceGroup.md)

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
**502** | Bad Gateway |  -  |
**0** | An error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

