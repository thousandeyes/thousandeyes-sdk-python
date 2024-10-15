# thousandeyes_sdk.dashboards.DashboardSnapshotsApi

All URIs are relative to *https://api.thousandeyes.com/v7*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_dashboard_snapshot**](DashboardSnapshotsApi.md#create_dashboard_snapshot) | **POST** /dashboard-snapshots | Create dashboard snapshot
[**delete_dashboard_snapshot**](DashboardSnapshotsApi.md#delete_dashboard_snapshot) | **DELETE** /dashboard-snapshots/{snapshotId} | Delete dashboard snapshot
[**get_dashboard_snapshot**](DashboardSnapshotsApi.md#get_dashboard_snapshot) | **GET** /dashboard-snapshots/{snapshotId} | Retrieve dashboard snapshot
[**get_dashboard_snapshot_widget_data**](DashboardSnapshotsApi.md#get_dashboard_snapshot_widget_data) | **GET** /dashboard-snapshots/{snapshotId}/widgets/{widgetId} | Retrieve dashboard snapshot data
[**get_dashboard_snapshots**](DashboardSnapshotsApi.md#get_dashboard_snapshots) | **GET** /dashboard-snapshots | List dashboard snapshots
[**update_dashboard_snapshot_expiration_date**](DashboardSnapshotsApi.md#update_dashboard_snapshot_expiration_date) | **PATCH** /dashboard-snapshots/{snapshotId} | Update snapshot expiration


# **create_dashboard_snapshot**
> DashboardSnapshotResponse create_dashboard_snapshot(generate_dashboard_snapshot_request, aid=aid)

Create dashboard snapshot

Creates a new dashboard snapshot within your account group. The `Edit Snapshots` permission is required to use this endpoint. 

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.dashboards
from thousandeyes_sdk.dashboards.models.dashboard_snapshot_response import DashboardSnapshotResponse
from thousandeyes_sdk.dashboards.models.generate_dashboard_snapshot_request import GenerateDashboardSnapshotRequest
from thousandeyes_sdk.dashboards.rest import ApiException
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
    api_instance = thousandeyes_sdk.dashboards.DashboardSnapshotsApi(api_client)
    generate_dashboard_snapshot_request = thousandeyes_sdk.dashboards.GenerateDashboardSnapshotRequest() # GenerateDashboardSnapshotRequest | Request body schema to create a dashboard snapshot.
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Create dashboard snapshot
        api_response = api_instance.create_dashboard_snapshot(generate_dashboard_snapshot_request, aid=aid)
        print("The response of DashboardSnapshotsApi->create_dashboard_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardSnapshotsApi->create_dashboard_snapshot: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **generate_dashboard_snapshot_request** | [**GenerateDashboardSnapshotRequest**](GenerateDashboardSnapshotRequest.md)| Request body schema to create a dashboard snapshot. | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

[**DashboardSnapshotResponse**](DashboardSnapshotResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json, application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  * Location -  <br>  * X-Dashboard-Snapshot-Rate-Limit-Limit -  <br>  * X-Dashboard-Snapshot-Rate-Limit-Remaining -  <br>  * X-Dashboard-Snapshot-Rate-Limit-Reset -  <br>  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Insufficient permissions to query endpoint |  -  |
**404** | Not found |  -  |
**429** | Exhausted rate limit for snapshot creation |  * X-Dashboard-Snapshot-Rate-Limit-Limit -  <br>  * X-Dashboard-Snapshot-Rate-Limit-Remaining -  <br>  * X-Dashboard-Snapshot-Rate-Limit-Reset -  <br>  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dashboard_snapshot**
> delete_dashboard_snapshot(snapshot_id, aid=aid)

Delete dashboard snapshot

Deletes a dashboard snapshot using the `snapshotId` provided in the request. Users with the `Edit reports for all users in account group` permission (Account Admin) can delete any dashboard snapshot. 

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.dashboards
from thousandeyes_sdk.dashboards.rest import ApiException
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
    api_instance = thousandeyes_sdk.dashboards.DashboardSnapshotsApi(api_client)
    snapshot_id = 'd28bb71f-5a47-4783-8f12-d4b115e61b0c' # str | A Identifier for a dashboard snapshot which can be obtained from the `/dashboards-snapshots` endpoint.
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Delete dashboard snapshot
        api_instance.delete_dashboard_snapshot(snapshot_id, aid=aid)
    except Exception as e:
        print("Exception when calling DashboardSnapshotsApi->delete_dashboard_snapshot: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshot_id** | **str**| A Identifier for a dashboard snapshot which can be obtained from the &#x60;/dashboards-snapshots&#x60; endpoint. | 
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
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Insufficient permissions to query endpoint |  -  |
**404** | Not found |  -  |
**429** | Exhausted rate limit for the organization |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dashboard_snapshot**
> ApiDashboardSnapshot get_dashboard_snapshot(snapshot_id, aid=aid)

Retrieve dashboard snapshot

This operation returns a list of widgets configured in dashboard snapshot configured in ThousandEyes. Seed this endpoint with a snapshotId found from the /dashboard-snapshots endpoint. This endpoint requires the `View Snapshots` permission be assigned to the role of the user accessing this endpoint. Returns a list of widgets configured within a dashboard snapshot. Use the `snapshotId` obtained from the `/dashboard-snapshots` endpoint. The `View Snapshots` permission is required to use this endpoint.\"

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.dashboards
from thousandeyes_sdk.dashboards.models.api_dashboard_snapshot import ApiDashboardSnapshot
from thousandeyes_sdk.dashboards.rest import ApiException
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
    api_instance = thousandeyes_sdk.dashboards.DashboardSnapshotsApi(api_client)
    snapshot_id = 'd28bb71f-5a47-4783-8f12-d4b115e61b0c' # str | A Identifier for a dashboard snapshot which can be obtained from the `/dashboards-snapshots` endpoint.
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Retrieve dashboard snapshot
        api_response = api_instance.get_dashboard_snapshot(snapshot_id, aid=aid)
        print("The response of DashboardSnapshotsApi->get_dashboard_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardSnapshotsApi->get_dashboard_snapshot: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshot_id** | **str**| A Identifier for a dashboard snapshot which can be obtained from the &#x60;/dashboards-snapshots&#x60; endpoint. | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

[**ApiDashboardSnapshot**](ApiDashboardSnapshot.md)

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

# **get_dashboard_snapshot_widget_data**
> ApiWidgetDataSnapshotResponse get_dashboard_snapshot_widget_data(snapshot_id, widget_id, aid=aid)

Retrieve dashboard snapshot data

Returns actual metrics used in the generation of a dashboard snapshot. 

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.dashboards
from thousandeyes_sdk.dashboards.models.api_widget_data_snapshot_response import ApiWidgetDataSnapshotResponse
from thousandeyes_sdk.dashboards.rest import ApiException
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
    api_instance = thousandeyes_sdk.dashboards.DashboardSnapshotsApi(api_client)
    snapshot_id = 'd28bb71f-5a47-4783-8f12-d4b115e61b0c' # str | A Identifier for a dashboard snapshot which can be obtained from the `/dashboards-snapshots` endpoint.
    widget_id = 'unpmg' # str | A Identifier for a widget.
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Retrieve dashboard snapshot data
        api_response = api_instance.get_dashboard_snapshot_widget_data(snapshot_id, widget_id, aid=aid)
        print("The response of DashboardSnapshotsApi->get_dashboard_snapshot_widget_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardSnapshotsApi->get_dashboard_snapshot_widget_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshot_id** | **str**| A Identifier for a dashboard snapshot which can be obtained from the &#x60;/dashboards-snapshots&#x60; endpoint. | 
 **widget_id** | **str**| A Identifier for a widget. | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

[**ApiWidgetDataSnapshotResponse**](ApiWidgetDataSnapshotResponse.md)

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

# **get_dashboard_snapshots**
> DashboardSnapshotsPage get_dashboard_snapshots(aid=aid, dashboard_id=dashboard_id, cursor=cursor)

List dashboard snapshots

Returns a list of dashboard snapshots within your account group. Use this data to identify a specific dashboard snapshot, which can be used in other endpoints to access aggregated data. The `View Snapshots` permission is required to use this endpoint.\" 

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.dashboards
from thousandeyes_sdk.dashboards.models.dashboard_snapshots_page import DashboardSnapshotsPage
from thousandeyes_sdk.dashboards.rest import ApiException
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
    api_instance = thousandeyes_sdk.dashboards.DashboardSnapshotsApi(api_client)
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)
    dashboard_id = '646f4d2ce3c99b0536c3821e' # str |  (optional)
    cursor = 'cursor_example' # str | (Optional) Opaque cursor used for pagination. Clients should use `next` value from `_links` instead of this parameter. (optional)

    try:
        # List dashboard snapshots
        api_response = api_instance.get_dashboard_snapshots(aid=aid, dashboard_id=dashboard_id, cursor=cursor)
        print("The response of DashboardSnapshotsApi->get_dashboard_snapshots:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardSnapshotsApi->get_dashboard_snapshots: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 
 **dashboard_id** | **str**|  | [optional] 
 **cursor** | **str**| (Optional) Opaque cursor used for pagination. Clients should use &#x60;next&#x60; value from &#x60;_links&#x60; instead of this parameter. | [optional] 

### Return type

[**DashboardSnapshotsPage**](DashboardSnapshotsPage.md)

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

# **update_dashboard_snapshot_expiration_date**
> update_dashboard_snapshot_expiration_date(snapshot_id, update_snapshot_expiration_date_api_request, aid=aid)

Update snapshot expiration

Updates the expiration date of a dashboard snapshot. The `Edit snapshots` permission is required to access this endpoint. 

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.dashboards
from thousandeyes_sdk.dashboards.models.update_snapshot_expiration_date_api_request import UpdateSnapshotExpirationDateApiRequest
from thousandeyes_sdk.dashboards.rest import ApiException
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
    api_instance = thousandeyes_sdk.dashboards.DashboardSnapshotsApi(api_client)
    snapshot_id = 'd28bb71f-5a47-4783-8f12-d4b115e61b0c' # str | A Identifier for a dashboard snapshot which can be obtained from the `/dashboards-snapshots` endpoint.
    update_snapshot_expiration_date_api_request = thousandeyes_sdk.dashboards.UpdateSnapshotExpirationDateApiRequest() # UpdateSnapshotExpirationDateApiRequest | Request body schema to update a snapshot expiration.
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Update snapshot expiration
        api_instance.update_dashboard_snapshot_expiration_date(snapshot_id, update_snapshot_expiration_date_api_request, aid=aid)
    except Exception as e:
        print("Exception when calling DashboardSnapshotsApi->update_dashboard_snapshot_expiration_date: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshot_id** | **str**| A Identifier for a dashboard snapshot which can be obtained from the &#x60;/dashboards-snapshots&#x60; endpoint. | 
 **update_snapshot_expiration_date_api_request** | [**UpdateSnapshotExpirationDateApiRequest**](UpdateSnapshotExpirationDateApiRequest.md)| Request body schema to update a snapshot expiration. | 
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
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Insufficient permissions to query endpoint |  -  |
**404** | Not found |  -  |
**429** | Exhausted rate limit for the organization |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

