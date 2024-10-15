# thousandeyes_sdk.dashboards.DashboardsApi

All URIs are relative to *https://api.thousandeyes.com/v7*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_dashboard**](DashboardsApi.md#create_dashboard) | **POST** /dashboards | Create dashboard
[**delete_dashboard**](DashboardsApi.md#delete_dashboard) | **DELETE** /dashboards/{dashboardId} | Delete dashboard
[**get_dashboard**](DashboardsApi.md#get_dashboard) | **GET** /dashboards/{dashboardId} | Retrieve dashboard
[**get_dashboard_widget_data**](DashboardsApi.md#get_dashboard_widget_data) | **GET** /dashboards/{dashboardId}/widgets/{widgetId} | Retrieve dashboard widget data
[**get_dashboards**](DashboardsApi.md#get_dashboards) | **GET** /dashboards | List dashboards
[**update_dashboard**](DashboardsApi.md#update_dashboard) | **PUT** /dashboards/{dashboardId} | Update dashboard


# **create_dashboard**
> Dashboard create_dashboard(dashboard, aid=aid)

Create dashboard

Creates a new dashboard in your account group. To create a dashboard,  you must have one of the following permissions: * `Edit dashboard templates for all users in account group` permission (Account Admin).  * `Edit own dashboard templates` permission (Regular User). 

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.dashboards
from thousandeyes_sdk.dashboards.models.dashboard import Dashboard
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
    api_instance = thousandeyes_sdk.dashboards.DashboardsApi(api_client)
    dashboard = thousandeyes_sdk.dashboards.Dashboard() # Dashboard | Request body schema to create a dashboard.
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Create dashboard
        api_response = api_instance.create_dashboard(dashboard, aid=aid)
        print("The response of DashboardsApi->create_dashboard:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardsApi->create_dashboard: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard** | [**Dashboard**](Dashboard.md)| Request body schema to create a dashboard. | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

[**Dashboard**](Dashboard.md)

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

# **delete_dashboard**
> delete_dashboard(dashboard_id, aid=aid)

Delete dashboard

Deletes a dashboard using the `dashboardId` provided in the request.  **Note**: * Users with the `Edit dashboard templates for all users in account group` permission (Account Admin) can delete any dashboard. * Users with the `Edit own dashboard templates` permission (Regular User) can only delete the dashboards they have created themselves. 

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
    api_instance = thousandeyes_sdk.dashboards.DashboardsApi(api_client)
    dashboard_id = '646f4d2ce3c99b0536c3821e' # str | A Identifier for a dashboard which can be obtained from the `/dashboards` endpoint.
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Delete dashboard
        api_instance.delete_dashboard(dashboard_id, aid=aid)
    except Exception as e:
        print("Exception when calling DashboardsApi->delete_dashboard: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_id** | **str**| A Identifier for a dashboard which can be obtained from the &#x60;/dashboards&#x60; endpoint. | 
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

# **get_dashboard**
> ApiDashboard get_dashboard(dashboard_id, aid=aid)

Retrieve dashboard

Returns a list of widgets within a dashboard, along with the dashboard's metadata. 

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.dashboards
from thousandeyes_sdk.dashboards.models.api_dashboard import ApiDashboard
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
    api_instance = thousandeyes_sdk.dashboards.DashboardsApi(api_client)
    dashboard_id = '646f4d2ce3c99b0536c3821e' # str | A Identifier for a dashboard which can be obtained from the `/dashboards` endpoint.
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Retrieve dashboard
        api_response = api_instance.get_dashboard(dashboard_id, aid=aid)
        print("The response of DashboardsApi->get_dashboard:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardsApi->get_dashboard: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_id** | **str**| A Identifier for a dashboard which can be obtained from the &#x60;/dashboards&#x60; endpoint. | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

[**ApiDashboard**](ApiDashboard.md)

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

# **get_dashboard_widget_data**
> ApiWidgetDataResponse get_dashboard_widget_data(dashboard_id, widget_id, aid=aid, window=window, start_date=start_date, end_date=end_date, max=max, cursor=cursor, sort=sort, order=order)

Retrieve dashboard widget data

Returns the raw data displayed within a widget in the dashboard. 

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.dashboards
from thousandeyes_sdk.dashboards.models.api_widget_data_response import ApiWidgetDataResponse
from thousandeyes_sdk.dashboards.models.dashboard_order import DashboardOrder
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
    api_instance = thousandeyes_sdk.dashboards.DashboardsApi(api_client)
    dashboard_id = '646f4d2ce3c99b0536c3821e' # str | A Identifier for a dashboard which can be obtained from the `/dashboards` endpoint.
    widget_id = 'unpmg' # str | A Identifier for a widget.
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)
    window = '12h' # str | A dynamic time interval up to the current time of the request. Specify the interval as a number followed by an optional type: `s` for seconds (default if no type is specified), `m` for minutes, `h` for hours, `d` for days, and `w` for weeks. For a precise date range, use `startDate` and `endDate`. (optional)
    start_date = '2022-07-17T22:00:54Z' # datetime | Use with the `endDate` parameter. Include the complete time (hours, minutes, and seconds) in UTC time zone, following the ISO 8601 date-time format. See the example for reference. Please note that this parameter can't be used with `window`. (optional)
    end_date = '2022-07-18T22:00:54Z' # datetime | Defaults to current time the request is made. Use with the `startDate` parameter. Include the complete time (hours, minutes, and seconds) in UTC time zone, following the ISO 8601 date-time format. See the example for reference. Please note that this parameter can't be used with `window`. (optional)
    max = 10 # float | Optionally specify the maximum number of objects to retrieve. This only applies to the **Alert List** and **Test Table** Widgets. * The default for the **Alert List** widget is set by its limitBy configuration. * The default value for the **Test Table** widget is 10. (optional)
    cursor = 'bGFzdFJvdW5kSWQ9MTY4MTQxMDQ4MA' # str | An optional pagination cursor. This parameter should not not be used directly. Instead, use the `_links` returned by the API. This feature is only available in the **Test Table** widget. (optional)
    sort = 'alertStatus' # str | Optional sorting parameter with attributes listed comma-separated. This only applies to the **Alert List** and **Test Table** Widgets. * For the **Alert List** widget, you can sort by `alertStatus` or `startTime`. The default is `alertStatus`. * For the **Test Table** widget, you can sort by `alertStatus`, `testName`, or `testType`. The sequence might vary from the web application. The default sort attribute is `alertStatus`. (optional)
    order = thousandeyes_sdk.dashboards.DashboardOrder() # DashboardOrder | Optional sorting order parameter that accepts either `asc` (ascending) or `desc` (descending) values. This only applies to the **Alert List** and **Test Table** Widgets. (optional)

    try:
        # Retrieve dashboard widget data
        api_response = api_instance.get_dashboard_widget_data(dashboard_id, widget_id, aid=aid, window=window, start_date=start_date, end_date=end_date, max=max, cursor=cursor, sort=sort, order=order)
        print("The response of DashboardsApi->get_dashboard_widget_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardsApi->get_dashboard_widget_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_id** | **str**| A Identifier for a dashboard which can be obtained from the &#x60;/dashboards&#x60; endpoint. | 
 **widget_id** | **str**| A Identifier for a widget. | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 
 **window** | **str**| A dynamic time interval up to the current time of the request. Specify the interval as a number followed by an optional type: &#x60;s&#x60; for seconds (default if no type is specified), &#x60;m&#x60; for minutes, &#x60;h&#x60; for hours, &#x60;d&#x60; for days, and &#x60;w&#x60; for weeks. For a precise date range, use &#x60;startDate&#x60; and &#x60;endDate&#x60;. | [optional] 
 **start_date** | **datetime**| Use with the &#x60;endDate&#x60; parameter. Include the complete time (hours, minutes, and seconds) in UTC time zone, following the ISO 8601 date-time format. See the example for reference. Please note that this parameter can&#39;t be used with &#x60;window&#x60;. | [optional] 
 **end_date** | **datetime**| Defaults to current time the request is made. Use with the &#x60;startDate&#x60; parameter. Include the complete time (hours, minutes, and seconds) in UTC time zone, following the ISO 8601 date-time format. See the example for reference. Please note that this parameter can&#39;t be used with &#x60;window&#x60;. | [optional] 
 **max** | **float**| Optionally specify the maximum number of objects to retrieve. This only applies to the **Alert List** and **Test Table** Widgets. * The default for the **Alert List** widget is set by its limitBy configuration. * The default value for the **Test Table** widget is 10. | [optional] 
 **cursor** | **str**| An optional pagination cursor. This parameter should not not be used directly. Instead, use the &#x60;_links&#x60; returned by the API. This feature is only available in the **Test Table** widget. | [optional] 
 **sort** | **str**| Optional sorting parameter with attributes listed comma-separated. This only applies to the **Alert List** and **Test Table** Widgets. * For the **Alert List** widget, you can sort by &#x60;alertStatus&#x60; or &#x60;startTime&#x60;. The default is &#x60;alertStatus&#x60;. * For the **Test Table** widget, you can sort by &#x60;alertStatus&#x60;, &#x60;testName&#x60;, or &#x60;testType&#x60;. The sequence might vary from the web application. The default sort attribute is &#x60;alertStatus&#x60;. | [optional] 
 **order** | [**DashboardOrder**](.md)| Optional sorting order parameter that accepts either &#x60;asc&#x60; (ascending) or &#x60;desc&#x60; (descending) values. This only applies to the **Alert List** and **Test Table** Widgets. | [optional] 

### Return type

[**ApiWidgetDataResponse**](ApiWidgetDataResponse.md)

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

# **get_dashboards**
> List[ApiDashboard] get_dashboards(aid=aid)

List dashboards

Returns a list of dashboards and their settings within your account group. 

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.dashboards
from thousandeyes_sdk.dashboards.models.api_dashboard import ApiDashboard
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
    api_instance = thousandeyes_sdk.dashboards.DashboardsApi(api_client)
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # List dashboards
        api_response = api_instance.get_dashboards(aid=aid)
        print("The response of DashboardsApi->get_dashboards:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardsApi->get_dashboards: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

[**List[ApiDashboard]**](ApiDashboard.md)

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

# **update_dashboard**
> Dashboard update_dashboard(dashboard_id, dashboard, aid=aid)

Update dashboard

Updates an existing dashboard in your account group.   **Note**:  * Users with the `Edit dashboard templates for all users in account group` permission (Account Admin) can update any dashboard. * Users with the `Edit own dashboard templates` permission (Regular User) can only update the dashboards they have created themselves. 

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.dashboards
from thousandeyes_sdk.dashboards.models.dashboard import Dashboard
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
    api_instance = thousandeyes_sdk.dashboards.DashboardsApi(api_client)
    dashboard_id = '646f4d2ce3c99b0536c3821e' # str | A Identifier for a dashboard which can be obtained from the `/dashboards` endpoint.
    dashboard = thousandeyes_sdk.dashboards.Dashboard() # Dashboard | Request body schema to update a dashboard.
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Update dashboard
        api_response = api_instance.update_dashboard(dashboard_id, dashboard, aid=aid)
        print("The response of DashboardsApi->update_dashboard:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardsApi->update_dashboard: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_id** | **str**| A Identifier for a dashboard which can be obtained from the &#x60;/dashboards&#x60; endpoint. | 
 **dashboard** | [**Dashboard**](Dashboard.md)| Request body schema to update a dashboard. | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

[**Dashboard**](Dashboard.md)

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

