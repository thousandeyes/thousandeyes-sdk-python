# endpoint_test_results.NetworkDynamicTestsResultsApi

All URIs are relative to *https://api.thousandeyes.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_dynamic_test_result_network_pathvis**](NetworkDynamicTestsResultsApi.md#get_dynamic_test_result_network_pathvis) | **GET** /v7/endpoint/test-results/dynamic-tests/{testId}/path-vis | Retrieve path visualization network dynamic test results
[**get_dynamic_test_result_pathvis_agent_round**](NetworkDynamicTestsResultsApi.md#get_dynamic_test_result_pathvis_agent_round) | **GET** /v7/endpoint/test-results/dynamic-tests/{testId}/path-vis/agent/{agentId}/round/{roundId} | Retrieve path visualization network dynamic test results details
[**post_fetch_dynamic_test_result_metrics**](NetworkDynamicTestsResultsApi.md#post_fetch_dynamic_test_result_metrics) | **POST** /v7/endpoint/test-results/dynamic-tests/{testId}/network/filter | Retrieve network dynamic test results


# **get_dynamic_test_result_network_pathvis**
> GetDynamicTestResultNetworkPathvis200Response get_dynamic_test_result_network_pathvis(test_id, aid=aid, window=window, start_date=start_date, end_date=end_date, cursor=cursor)

Retrieve path visualization network dynamic test results

Returns a summary of the path visualization data collected from each endpoint agent to the destination. In each path visualization attempt, one attempt is made to reach the destination. Each set of data is summarized, based on response time, number of hops, and response time to the target. A time frame must be specified, or the most recent round within last 2 hours will be returned. 

### Example

* Bearer Authentication (BearerAuth):

```python
import endpoint_test_results
from endpoint_test_results.models.get_dynamic_test_result_network_pathvis200_response import GetDynamicTestResultNetworkPathvis200Response
from endpoint_test_results.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.thousandeyes.com
# See configuration.py for a list of all supported configuration parameters.
configuration = endpoint_test_results.Configuration(
    host = "https://api.thousandeyes.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = endpoint_test_results.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with endpoint_test_results.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = endpoint_test_results.NetworkDynamicTestsResultsApi(api_client)
    test_id = '202701' # str | Test ID
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)
    window = '12h' # str | A dynamic time interval up to the current time of the request. Specify the interval as a number followed by an optional type: `s` for seconds (default if no type is specified), `m` for minutes, `h` for hours, `d` for days, and `w` for weeks. For a precise date range, use `startDate` and `endDate`. (optional)
    start_date = '2022-07-17T22:00:54Z' # datetime | Use with the `endDate` parameter. Include the complete time (hours, minutes, and seconds) in UTC time zone, following the ISO 8601 date-time format. See the example for reference. Please note that this parameter can't be used with `window`. (optional)
    end_date = '2022-07-18T22:00:54Z' # datetime | Defaults to current time the request is made. Use with the `startDate` parameter. Include the complete time (hours, minutes, and seconds) in UTC time zone, following the ISO 8601 date-time format. See the example for reference. Please note that this parameter can't be used with `window`. (optional)
    cursor = 'cursor_example' # str | (Optional) Opaque cursor used for pagination. Clients should use `next` value from `_links` instead of this parameter. (optional)

    try:
        # Retrieve path visualization network dynamic test results
        api_response = api_instance.get_dynamic_test_result_network_pathvis(test_id, aid=aid, window=window, start_date=start_date, end_date=end_date, cursor=cursor)
        print("The response of NetworkDynamicTestsResultsApi->get_dynamic_test_result_network_pathvis:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkDynamicTestsResultsApi->get_dynamic_test_result_network_pathvis: %s\n" % e)
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

### Return type

[**GetDynamicTestResultNetworkPathvis200Response**](GetDynamicTestResultNetworkPathvis200Response.md)

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
**502** | Bad Gateway |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dynamic_test_result_pathvis_agent_round**
> GetDynamicTestResultPathvisAgentRound200Response get_dynamic_test_result_pathvis_agent_round(test_id, agent_id, round_id, aid=aid)

Retrieve path visualization network dynamic test results details

Returns a hop-by-hop summary of the path trace data collected during path visualization. In each round, one path discovery attempt is made to reach the destination. The entire path is returned. A `roundId` must be specified. 

### Example

* Bearer Authentication (BearerAuth):

```python
import endpoint_test_results
from endpoint_test_results.models.get_dynamic_test_result_pathvis_agent_round200_response import GetDynamicTestResultPathvisAgentRound200Response
from endpoint_test_results.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.thousandeyes.com
# See configuration.py for a list of all supported configuration parameters.
configuration = endpoint_test_results.Configuration(
    host = "https://api.thousandeyes.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = endpoint_test_results.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with endpoint_test_results.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = endpoint_test_results.NetworkDynamicTestsResultsApi(api_client)
    test_id = '202701' # str | Test ID
    agent_id = '11' # str | Agent ID
    round_id = '1384309800' # str | Round ID
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Retrieve path visualization network dynamic test results details
        api_response = api_instance.get_dynamic_test_result_pathvis_agent_round(test_id, agent_id, round_id, aid=aid)
        print("The response of NetworkDynamicTestsResultsApi->get_dynamic_test_result_pathvis_agent_round:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkDynamicTestsResultsApi->get_dynamic_test_result_pathvis_agent_round: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_id** | **str**| Test ID | 
 **agent_id** | **str**| Agent ID | 
 **round_id** | **str**| Round ID | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

[**GetDynamicTestResultPathvisAgentRound200Response**](GetDynamicTestResultPathvisAgentRound200Response.md)

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
**502** | Bad Gateway |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_fetch_dynamic_test_result_metrics**
> PostFetchDynamicTestResultMetrics200Response post_fetch_dynamic_test_result_metrics(test_id, aid=aid, window=window, start_date=start_date, end_date=end_date, cursor=cursor, dynamic_tests_data_round_search=dynamic_tests_data_round_search)

Retrieve network dynamic test results

Returns network metrics (`loss`, `latency`, `jitter` and `bandwidth`) from each endpoint agent, for each `roundId` in the requested window. When Time Frame is provided the rounds specific to the time frame is returned and the order is not pre-defined unless a user specifies the sort order in filter. When no time frame is provided the latest rounds are returned. 

### Example

* Bearer Authentication (BearerAuth):

```python
import endpoint_test_results
from endpoint_test_results.models.dynamic_tests_data_round_search import DynamicTestsDataRoundSearch
from endpoint_test_results.models.post_fetch_dynamic_test_result_metrics200_response import PostFetchDynamicTestResultMetrics200Response
from endpoint_test_results.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.thousandeyes.com
# See configuration.py for a list of all supported configuration parameters.
configuration = endpoint_test_results.Configuration(
    host = "https://api.thousandeyes.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = endpoint_test_results.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with endpoint_test_results.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = endpoint_test_results.NetworkDynamicTestsResultsApi(api_client)
    test_id = '202701' # str | Test ID
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)
    window = '12h' # str | A dynamic time interval up to the current time of the request. Specify the interval as a number followed by an optional type: `s` for seconds (default if no type is specified), `m` for minutes, `h` for hours, `d` for days, and `w` for weeks. For a precise date range, use `startDate` and `endDate`. (optional)
    start_date = '2022-07-17T22:00:54Z' # datetime | Use with the `endDate` parameter. Include the complete time (hours, minutes, and seconds) in UTC time zone, following the ISO 8601 date-time format. See the example for reference. Please note that this parameter can't be used with `window`. (optional)
    end_date = '2022-07-18T22:00:54Z' # datetime | Defaults to current time the request is made. Use with the `startDate` parameter. Include the complete time (hours, minutes, and seconds) in UTC time zone, following the ISO 8601 date-time format. See the example for reference. Please note that this parameter can't be used with `window`. (optional)
    cursor = 'cursor_example' # str | (Optional) Opaque cursor used for pagination. Clients should use `next` value from `_links` instead of this parameter. (optional)
    dynamic_tests_data_round_search = endpoint_test_results.DynamicTestsDataRoundSearch() # DynamicTestsDataRoundSearch | Tests data search filters. (optional)

    try:
        # Retrieve network dynamic test results
        api_response = api_instance.post_fetch_dynamic_test_result_metrics(test_id, aid=aid, window=window, start_date=start_date, end_date=end_date, cursor=cursor, dynamic_tests_data_round_search=dynamic_tests_data_round_search)
        print("The response of NetworkDynamicTestsResultsApi->post_fetch_dynamic_test_result_metrics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkDynamicTestsResultsApi->post_fetch_dynamic_test_result_metrics: %s\n" % e)
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
 **dynamic_tests_data_round_search** | [**DynamicTestsDataRoundSearch**](DynamicTestsDataRoundSearch.md)| Tests data search filters. | [optional] 

### Return type

[**PostFetchDynamicTestResultMetrics200Response**](PostFetchDynamicTestResultMetrics200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
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
**502** | Bad Gateway |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
