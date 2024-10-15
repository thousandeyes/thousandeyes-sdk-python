# thousandeyes_sdk.tags.TagAssignmentApi

All URIs are relative to *https://api.thousandeyes.com/v7*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assign_tag**](TagAssignmentApi.md#assign_tag) | **POST** /tags/{id}/assign | Assign tag to multiple objects
[**assign_tags**](TagAssignmentApi.md#assign_tags) | **POST** /tags/assign | Assign multiple tags to multiple objects
[**unassign_tag**](TagAssignmentApi.md#unassign_tag) | **POST** /tags/{id}/unassign | Remove tag from multiple objects
[**unassign_tags**](TagAssignmentApi.md#unassign_tags) | **POST** /tags/unassign | Remove multiple tags from multiple objects


# **assign_tag**
> BulkTagAssignment assign_tag(id, tag_assignment, aid=aid)

Assign tag to multiple objects

Assigns a tag to one or more objects. This operation has cumulative behavior: The tag is assigned to the specified objects, and the previous assignments persist. No unassignment takes place.

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.tags
from thousandeyes_sdk.tags.models.bulk_tag_assignment import BulkTagAssignment
from thousandeyes_sdk.tags.models.tag_assignment import TagAssignment
from thousandeyes_sdk.tags.rest import ApiException
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
    api_instance = thousandeyes_sdk.tags.TagAssignmentApi(api_client)
    id = 'c6b78e57-81a2-4c5f-a11a-d96c3c664d55' # str | Tag ID
    tag_assignment = thousandeyes_sdk.tags.TagAssignment() # TagAssignment | 
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Assign tag to multiple objects
        api_response = api_instance.assign_tag(id, tag_assignment, aid=aid)
        print("The response of TagAssignmentApi->assign_tag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TagAssignmentApi->assign_tag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Tag ID | 
 **tag_assignment** | [**TagAssignment**](TagAssignment.md)|  | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

[**BulkTagAssignment**](BulkTagAssignment.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**207** | Assignment created |  -  |
**401** | Unauthorized |  -  |
**403** | Insufficient permissions to query endpoint |  -  |
**404** | Not found |  -  |
**429** | Exhausted rate limit for the organization |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assign_tags**
> BulkTagAssignments assign_tags(bulk_tag_assignments, aid=aid)

Assign multiple tags to multiple objects

Assigns the specified tags to the specified objects. This operation has cumulative behavior: The tags are assigned to the specified objects, and the previous assignments persist. No unassignment takes place.

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.tags
from thousandeyes_sdk.tags.models.bulk_tag_assignments import BulkTagAssignments
from thousandeyes_sdk.tags.rest import ApiException
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
    api_instance = thousandeyes_sdk.tags.TagAssignmentApi(api_client)
    bulk_tag_assignments = thousandeyes_sdk.tags.BulkTagAssignments() # BulkTagAssignments | 
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Assign multiple tags to multiple objects
        api_response = api_instance.assign_tags(bulk_tag_assignments, aid=aid)
        print("The response of TagAssignmentApi->assign_tags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TagAssignmentApi->assign_tags: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk_tag_assignments** | [**BulkTagAssignments**](BulkTagAssignments.md)|  | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

[**BulkTagAssignments**](BulkTagAssignments.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**207** | Item created |  -  |
**401** | Unauthorized |  -  |
**403** | Insufficient permissions to query endpoint |  -  |
**404** | Not found |  -  |
**429** | Exhausted rate limit for the organization |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unassign_tag**
> unassign_tag(id, tag_assignment, aid=aid)

Remove tag from multiple objects

Removes a tag from one or more objects.

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.tags
from thousandeyes_sdk.tags.models.tag_assignment import TagAssignment
from thousandeyes_sdk.tags.rest import ApiException
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
    api_instance = thousandeyes_sdk.tags.TagAssignmentApi(api_client)
    id = 'c6b78e57-81a2-4c5f-a11a-d96c3c664d55' # str | Tag ID
    tag_assignment = thousandeyes_sdk.tags.TagAssignment() # TagAssignment | 
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Remove tag from multiple objects
        api_instance.unassign_tag(id, tag_assignment, aid=aid)
    except Exception as e:
        print("Exception when calling TagAssignmentApi->unassign_tag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Tag ID | 
 **tag_assignment** | [**TagAssignment**](TagAssignment.md)|  | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No content |  -  |
**401** | Unauthorized |  -  |
**403** | Insufficient permissions to query endpoint |  -  |
**404** | Not found |  -  |
**429** | Exhausted rate limit for the organization |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unassign_tags**
> BulkTagAssignments unassign_tags(bulk_tag_assignments, aid=aid)

Remove multiple tags from multiple objects

Removes the specified tags from one or more objects.

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.tags
from thousandeyes_sdk.tags.models.bulk_tag_assignments import BulkTagAssignments
from thousandeyes_sdk.tags.rest import ApiException
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
    api_instance = thousandeyes_sdk.tags.TagAssignmentApi(api_client)
    bulk_tag_assignments = thousandeyes_sdk.tags.BulkTagAssignments() # BulkTagAssignments | 
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Remove multiple tags from multiple objects
        api_response = api_instance.unassign_tags(bulk_tag_assignments, aid=aid)
        print("The response of TagAssignmentApi->unassign_tags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TagAssignmentApi->unassign_tags: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk_tag_assignments** | [**BulkTagAssignments**](BulkTagAssignments.md)|  | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

[**BulkTagAssignments**](BulkTagAssignments.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**207** | Tag assignments created |  -  |
**401** | Unauthorized |  -  |
**403** | Insufficient permissions to query endpoint |  -  |
**404** | Not found |  -  |
**429** | Exhausted rate limit for the organization |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

