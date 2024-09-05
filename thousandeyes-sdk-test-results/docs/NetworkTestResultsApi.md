# thousandeyes_sdk.test_results.NetworkTestResultsApi

All URIs are relative to *https://api.thousandeyes.com/v7*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_test_network_results**](NetworkTestResultsApi.md#get_test_network_results) | **GET** /test-results/{testId}/network | Get network test results
[**get_test_path_vis_agent_round_results**](NetworkTestResultsApi.md#get_test_path_vis_agent_round_results) | **GET** /test-results/{testId}/path-vis/agent/{agentId}/round/{roundId} | Get path visualization test results by agent and round
[**get_test_path_vis_results**](NetworkTestResultsApi.md#get_test_path_vis_results) | **GET** /test-results/{testId}/path-vis | Get path visualization network test results


# **get_test_network_results**
> NetworkTestResults get_test_network_results(test_id, aid=aid, window=window, start_date=start_date, end_date=end_date, cursor=cursor, direction=direction)

Get network test results

Returns network test results for every agent and round. If you do not specify a window or a start and end date, data is displayed for the most recent testing round. 

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.test_results
from thousandeyes_sdk.test_results.models.network_test_results import NetworkTestResults
from thousandeyes_sdk.test_results.models.test_direction import TestDirection
from thousandeyes_sdk.test_results.rest import ApiException
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
with thousandeyes_sdk.test_results.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = thousandeyes_sdk.test_results.NetworkTestResultsApi(api_client)
    test_id = '202701' # str | Test ID
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)
    window = '12h' # str | A dynamic time interval up to the current time of the request. Specify the interval as a number followed by an optional type: `s` for seconds (default if no type is specified), `m` for minutes, `h` for hours, `d` for days, and `w` for weeks. For a precise date range, use `startDate` and `endDate`. (optional)
    start_date = '2022-07-17T22:00:54Z' # datetime | Use with the `endDate` parameter. Include the complete time (hours, minutes, and seconds) in UTC time zone, following the ISO 8601 date-time format. See the example for reference. Please note that this parameter can't be used with `window`. (optional)
    end_date = '2022-07-18T22:00:54Z' # datetime | Defaults to current time the request is made. Use with the `startDate` parameter. Include the complete time (hours, minutes, and seconds) in UTC time zone, following the ISO 8601 date-time format. See the example for reference. Please note that this parameter can't be used with `window`. (optional)
    cursor = 'cursor_example' # str | (Optional) Opaque cursor used for pagination. Clients should use `next` value from `_links` instead of this parameter. (optional)
    direction = thousandeyes_sdk.test_results.TestDirection() # TestDirection | Choose the direction for the metrics you want: [`from-target`, `to-target`, `bidirectional`]. This applies when you're doing bidirectional Agent-to-Agent tests. For bidirectional data, you'll get combined results; otherwise, you'll get data for one direction. If you try to get unidirectional test data with an incorrect direction parameter, it will trigger an error response. (optional)

    try:
        # Get network test results
        api_response = api_instance.get_test_network_results(test_id, aid=aid, window=window, start_date=start_date, end_date=end_date, cursor=cursor, direction=direction)
        print("The response of NetworkTestResultsApi->get_test_network_results:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkTestResultsApi->get_test_network_results: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_id** | **str**| Test ID | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 
 **window** | **str**| A dynamic time interval up to the current time of the request. Specify the interval as a number followed by an optional type: &#x60;s&#x60; for seconds (default if no type is specified), &#x60;m&#x60; for minutes, &#x60;h&#x60; for hours, &#x60;d&#x60; for days, and &#x60;w&#x60; for weeks. For a precise date range, use &#x60;startDate&#x60; and &#x60;endDate&#x60;. | [optional] 
 **start_date** | **datetime**| Use with the &#x60;endDate&#x60; parameter. Include the complete time (hours, minutes, and seconds) in UTC time zone, following the ISO 8601 date-time format. See the example for reference. Please note that this parameter can&#39;t be used with &#x60;window&#x60;. | [optional] 
 **end_date** | **datetime**| Defaults to current time the request is made. Use with the &#x60;startDate&#x60; parameter. Include the complete time (hours, minutes, and seconds) in UTC time zone, following the ISO 8601 date-time format. See the example for reference. Please note that this parameter can&#39;t be used with &#x60;window&#x60;. | [optional] 
 **cursor** | **str**| (Optional) Opaque cursor used for pagination. Clients should use &#x60;next&#x60; value from &#x60;_links&#x60; instead of this parameter. | [optional] 
 **direction** | [**TestDirection**](.md)| Choose the direction for the metrics you want: [&#x60;from-target&#x60;, &#x60;to-target&#x60;, &#x60;bidirectional&#x60;]. This applies when you&#39;re doing bidirectional Agent-to-Agent tests. For bidirectional data, you&#39;ll get combined results; otherwise, you&#39;ll get data for one direction. If you try to get unidirectional test data with an incorrect direction parameter, it will trigger an error response. | [optional] 

### Return type

[**NetworkTestResults**](NetworkTestResults.md)

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
**502** | Bad Gateway |  -  |
**0** | An error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_test_path_vis_agent_round_results**
> PathVisDetailTestResults get_test_path_vis_agent_round_results(test_id, agent_id, round_id, aid=aid, direction=direction)

Get path visualization test results by agent and round

Returns a summary of the path trace data collected during path visualization for a given agent and round. With each attempt, three tries are made to reach the destination. The entire path is displayed in order.  Bidirectional agent-to-agent tests also support the `direction` parameter. For example, if agents A, B, and C are testing agent D bidirectionally, and you want results from the route from agent A to agent D, you can use the query `direction=to-target`. For results from agent D to agent A, you can use `direction=from-target`. To get both results for both routes, query without the direction parameter. The source will always be agent A and the destination will be agent D, but the direction field will indicate which trace direction you want test results from. 

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.test_results
from thousandeyes_sdk.test_results.models.path_vis_detail_test_results import PathVisDetailTestResults
from thousandeyes_sdk.test_results.models.path_vis_direction import PathVisDirection
from thousandeyes_sdk.test_results.rest import ApiException
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
with thousandeyes_sdk.test_results.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = thousandeyes_sdk.test_results.NetworkTestResultsApi(api_client)
    test_id = '202701' # str | Test ID
    agent_id = '11' # str | Agent ID
    round_id = '1384309800' # str | Round ID
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)
    direction = thousandeyes_sdk.test_results.PathVisDirection() # PathVisDirection | Choose the direction for the metrics you want: [`from-target`, `to-target`]. This applies when you're doing bidirectional Agent-to-Agent tests. Omitting the parameter will default the results to both `from-target` and `to-target` values (bidirectional); otherwise, you'll get data for one direction. If you try to get unidirectional test data with an incorrect direction parameter, it will trigger an error response. (optional)

    try:
        # Get path visualization test results by agent and round
        api_response = api_instance.get_test_path_vis_agent_round_results(test_id, agent_id, round_id, aid=aid, direction=direction)
        print("The response of NetworkTestResultsApi->get_test_path_vis_agent_round_results:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkTestResultsApi->get_test_path_vis_agent_round_results: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_id** | **str**| Test ID | 
 **agent_id** | **str**| Agent ID | 
 **round_id** | **str**| Round ID | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 
 **direction** | [**PathVisDirection**](.md)| Choose the direction for the metrics you want: [&#x60;from-target&#x60;, &#x60;to-target&#x60;]. This applies when you&#39;re doing bidirectional Agent-to-Agent tests. Omitting the parameter will default the results to both &#x60;from-target&#x60; and &#x60;to-target&#x60; values (bidirectional); otherwise, you&#39;ll get data for one direction. If you try to get unidirectional test data with an incorrect direction parameter, it will trigger an error response. | [optional] 

### Return type

[**PathVisDetailTestResults**](PathVisDetailTestResults.md)

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
**502** | Bad Gateway |  -  |
**0** | An error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_test_path_vis_results**
> PathVisTestResults get_test_path_vis_results(test_id, aid=aid, window=window, start_date=start_date, end_date=end_date, cursor=cursor, direction=direction)

Get path visualization network test results

Returns a summary of the path trace data collected during path visualization for a given time range. With each attempt, three tries are made to reach the destination. The entire path is displayed in order. If you do not specify a window or a start and end date, data is displayed for the most recent testing round.   Bidirectional agent-to-agent tests also support the `direction` parameter. For example, if agents A, B, and C are testing agent D bidirectionally, and you want results from the route from agent A to agent D, you can use the query `direction=to-target`. For results from agent D to agent A, you can use `direction=from-target`. To get both results for both routes, query without the direction parameter. The source will always be agent A and the destination will be agent D, but the direction field will indicate which trace direction you want test results from. 

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.test_results
from thousandeyes_sdk.test_results.models.path_vis_direction import PathVisDirection
from thousandeyes_sdk.test_results.models.path_vis_test_results import PathVisTestResults
from thousandeyes_sdk.test_results.rest import ApiException
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
with thousandeyes_sdk.test_results.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = thousandeyes_sdk.test_results.NetworkTestResultsApi(api_client)
    test_id = '202701' # str | Test ID
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)
    window = '12h' # str | A dynamic time interval up to the current time of the request. Specify the interval as a number followed by an optional type: `s` for seconds (default if no type is specified), `m` for minutes, `h` for hours, `d` for days, and `w` for weeks. For a precise date range, use `startDate` and `endDate`. (optional)
    start_date = '2022-07-17T22:00:54Z' # datetime | Use with the `endDate` parameter. Include the complete time (hours, minutes, and seconds) in UTC time zone, following the ISO 8601 date-time format. See the example for reference. Please note that this parameter can't be used with `window`. (optional)
    end_date = '2022-07-18T22:00:54Z' # datetime | Defaults to current time the request is made. Use with the `startDate` parameter. Include the complete time (hours, minutes, and seconds) in UTC time zone, following the ISO 8601 date-time format. See the example for reference. Please note that this parameter can't be used with `window`. (optional)
    cursor = 'cursor_example' # str | (Optional) Opaque cursor used for pagination. Clients should use `next` value from `_links` instead of this parameter. (optional)
    direction = thousandeyes_sdk.test_results.PathVisDirection() # PathVisDirection | Choose the direction for the metrics you want: [`from-target`, `to-target`]. This applies when you're doing bidirectional Agent-to-Agent tests. Omitting the parameter will default the results to both `from-target` and `to-target` values (bidirectional); otherwise, you'll get data for one direction. If you try to get unidirectional test data with an incorrect direction parameter, it will trigger an error response. (optional)

    try:
        # Get path visualization network test results
        api_response = api_instance.get_test_path_vis_results(test_id, aid=aid, window=window, start_date=start_date, end_date=end_date, cursor=cursor, direction=direction)
        print("The response of NetworkTestResultsApi->get_test_path_vis_results:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkTestResultsApi->get_test_path_vis_results: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_id** | **str**| Test ID | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 
 **window** | **str**| A dynamic time interval up to the current time of the request. Specify the interval as a number followed by an optional type: &#x60;s&#x60; for seconds (default if no type is specified), &#x60;m&#x60; for minutes, &#x60;h&#x60; for hours, &#x60;d&#x60; for days, and &#x60;w&#x60; for weeks. For a precise date range, use &#x60;startDate&#x60; and &#x60;endDate&#x60;. | [optional] 
 **start_date** | **datetime**| Use with the &#x60;endDate&#x60; parameter. Include the complete time (hours, minutes, and seconds) in UTC time zone, following the ISO 8601 date-time format. See the example for reference. Please note that this parameter can&#39;t be used with &#x60;window&#x60;. | [optional] 
 **end_date** | **datetime**| Defaults to current time the request is made. Use with the &#x60;startDate&#x60; parameter. Include the complete time (hours, minutes, and seconds) in UTC time zone, following the ISO 8601 date-time format. See the example for reference. Please note that this parameter can&#39;t be used with &#x60;window&#x60;. | [optional] 
 **cursor** | **str**| (Optional) Opaque cursor used for pagination. Clients should use &#x60;next&#x60; value from &#x60;_links&#x60; instead of this parameter. | [optional] 
 **direction** | [**PathVisDirection**](.md)| Choose the direction for the metrics you want: [&#x60;from-target&#x60;, &#x60;to-target&#x60;]. This applies when you&#39;re doing bidirectional Agent-to-Agent tests. Omitting the parameter will default the results to both &#x60;from-target&#x60; and &#x60;to-target&#x60; values (bidirectional); otherwise, you&#39;ll get data for one direction. If you try to get unidirectional test data with an incorrect direction parameter, it will trigger an error response. | [optional] 

### Return type

[**PathVisTestResults**](PathVisTestResults.md)

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
**502** | Bad Gateway |  -  |
**0** | An error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

