# thousandeyes_sdk.endpoint_test_results.HTTPServerEndpointScheduledTestResultsApi

All URIs are relative to *https://api.thousandeyes.com/v7*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_http_server_scheduled_test_results**](HTTPServerEndpointScheduledTestResultsApi.md#get_http_server_scheduled_test_results) | **GET** /endpoint/test-results/scheduled-tests/{testId}/http-server | Retrieve HTTP server scheduled test results
[**get_multi_test_filtered_http_server_scheduled_test_results**](HTTPServerEndpointScheduledTestResultsApi.md#get_multi_test_filtered_http_server_scheduled_test_results) | **POST** /endpoint/test-results/scheduled-tests/http-server/filter | Filter HTTP server scheduled test results


# **get_http_server_scheduled_test_results**
> HttpEndpointTestResults get_http_server_scheduled_test_results(test_id, aid=aid, window=window, start_date=start_date, end_date=end_date, cursor=cursor, expand=expand)

Retrieve HTTP server scheduled test results

Returns component-level (DNS, Connect, Wait and Receive) timing for the load of an object over HTTP. 

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.endpoint_test_results
from thousandeyes_sdk.endpoint_test_results.models.expand_endpoint_http_server_options import ExpandEndpointHttpServerOptions
from thousandeyes_sdk.endpoint_test_results.models.http_endpoint_test_results import HttpEndpointTestResults
from thousandeyes_sdk.endpoint_test_results.rest import ApiException
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
    api_instance = thousandeyes_sdk.endpoint_test_results.HTTPServerEndpointScheduledTestResultsApi(api_client)
    test_id = '202701' # str | Test ID
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)
    window = '12h' # str | A dynamic time interval up to the current time of the request. Specify the interval as a number followed by an optional type: `s` for seconds (default if no type is specified), `m` for minutes, `h` for hours, `d` for days, and `w` for weeks. For a precise date range, use `startDate` and `endDate`. (optional)
    start_date = '2022-07-17T22:00:54Z' # datetime | Use with the `endDate` parameter. Include the complete time (hours, minutes, and seconds) in UTC time zone, following the ISO 8601 date-time format. See the example for reference. Please note that this parameter can't be used with `window`. (optional)
    end_date = '2022-07-18T22:00:54Z' # datetime | Defaults to current time the request is made. Use with the `startDate` parameter. Include the complete time (hours, minutes, and seconds) in UTC time zone, following the ISO 8601 date-time format. See the example for reference. Please note that this parameter can't be used with `window`. (optional)
    cursor = 'cursor_example' # str | (Optional) Opaque cursor used for pagination. Clients should use `next` value from `_links` instead of this parameter. (optional)
    expand = [thousandeyes_sdk.endpoint_test_results.ExpandEndpointHttpServerOptions()] # List[ExpandEndpointHttpServerOptions] | This parameter is optional and determines whether to expand resources related to test results. By default, no expansion occurs when this query parameter is omitted. To expand a specific resource, such as \"header,\" append `?expand=header` to the query. (optional)

    try:
        # Retrieve HTTP server scheduled test results
        api_response = api_instance.get_http_server_scheduled_test_results(test_id, aid=aid, window=window, start_date=start_date, end_date=end_date, cursor=cursor, expand=expand)
        print("The response of HTTPServerEndpointScheduledTestResultsApi->get_http_server_scheduled_test_results:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HTTPServerEndpointScheduledTestResultsApi->get_http_server_scheduled_test_results: %s\n" % e)
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
 **expand** | [**List[ExpandEndpointHttpServerOptions]**](ExpandEndpointHttpServerOptions.md)| This parameter is optional and determines whether to expand resources related to test results. By default, no expansion occurs when this query parameter is omitted. To expand a specific resource, such as \&quot;header,\&quot; append &#x60;?expand&#x3D;header&#x60; to the query. | [optional] 

### Return type

[**HttpEndpointTestResults**](HttpEndpointTestResults.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_multi_test_filtered_http_server_scheduled_test_results**
> HttpMultiEndpointTestResults get_multi_test_filtered_http_server_scheduled_test_results(aid=aid, window=window, start_date=start_date, end_date=end_date, cursor=cursor, expand=expand, http_endpoint_tests_data_rounds_search=http_endpoint_tests_data_rounds_search)

Filter HTTP server scheduled test results

Returns component-level (DNS, Connect, Wait and Receive) timing for the load of an object over HTTP. 

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.endpoint_test_results
from thousandeyes_sdk.endpoint_test_results.models.expand_endpoint_http_server_options import ExpandEndpointHttpServerOptions
from thousandeyes_sdk.endpoint_test_results.models.http_endpoint_tests_data_rounds_search import HttpEndpointTestsDataRoundsSearch
from thousandeyes_sdk.endpoint_test_results.models.http_multi_endpoint_test_results import HttpMultiEndpointTestResults
from thousandeyes_sdk.endpoint_test_results.rest import ApiException
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
    api_instance = thousandeyes_sdk.endpoint_test_results.HTTPServerEndpointScheduledTestResultsApi(api_client)
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)
    window = '12h' # str | A dynamic time interval up to the current time of the request. Specify the interval as a number followed by an optional type: `s` for seconds (default if no type is specified), `m` for minutes, `h` for hours, `d` for days, and `w` for weeks. For a precise date range, use `startDate` and `endDate`. (optional)
    start_date = '2022-07-17T22:00:54Z' # datetime | Use with the `endDate` parameter. Include the complete time (hours, minutes, and seconds) in UTC time zone, following the ISO 8601 date-time format. See the example for reference. Please note that this parameter can't be used with `window`. (optional)
    end_date = '2022-07-18T22:00:54Z' # datetime | Defaults to current time the request is made. Use with the `startDate` parameter. Include the complete time (hours, minutes, and seconds) in UTC time zone, following the ISO 8601 date-time format. See the example for reference. Please note that this parameter can't be used with `window`. (optional)
    cursor = 'cursor_example' # str | (Optional) Opaque cursor used for pagination. Clients should use `next` value from `_links` instead of this parameter. (optional)
    expand = [thousandeyes_sdk.endpoint_test_results.ExpandEndpointHttpServerOptions()] # List[ExpandEndpointHttpServerOptions] | This parameter is optional and determines whether to expand resources related to test results. By default, no expansion occurs when this query parameter is omitted. To expand a specific resource, such as \"header,\" append `?expand=header` to the query. (optional)
    http_endpoint_tests_data_rounds_search = thousandeyes_sdk.endpoint_test_results.HttpEndpointTestsDataRoundsSearch() # HttpEndpointTestsDataRoundsSearch | Test data search filters. (optional)

    try:
        # Filter HTTP server scheduled test results
        api_response = api_instance.get_multi_test_filtered_http_server_scheduled_test_results(aid=aid, window=window, start_date=start_date, end_date=end_date, cursor=cursor, expand=expand, http_endpoint_tests_data_rounds_search=http_endpoint_tests_data_rounds_search)
        print("The response of HTTPServerEndpointScheduledTestResultsApi->get_multi_test_filtered_http_server_scheduled_test_results:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HTTPServerEndpointScheduledTestResultsApi->get_multi_test_filtered_http_server_scheduled_test_results: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 
 **window** | **str**| A dynamic time interval up to the current time of the request. Specify the interval as a number followed by an optional type: &#x60;s&#x60; for seconds (default if no type is specified), &#x60;m&#x60; for minutes, &#x60;h&#x60; for hours, &#x60;d&#x60; for days, and &#x60;w&#x60; for weeks. For a precise date range, use &#x60;startDate&#x60; and &#x60;endDate&#x60;. | [optional] 
 **start_date** | **datetime**| Use with the &#x60;endDate&#x60; parameter. Include the complete time (hours, minutes, and seconds) in UTC time zone, following the ISO 8601 date-time format. See the example for reference. Please note that this parameter can&#39;t be used with &#x60;window&#x60;. | [optional] 
 **end_date** | **datetime**| Defaults to current time the request is made. Use with the &#x60;startDate&#x60; parameter. Include the complete time (hours, minutes, and seconds) in UTC time zone, following the ISO 8601 date-time format. See the example for reference. Please note that this parameter can&#39;t be used with &#x60;window&#x60;. | [optional] 
 **cursor** | **str**| (Optional) Opaque cursor used for pagination. Clients should use &#x60;next&#x60; value from &#x60;_links&#x60; instead of this parameter. | [optional] 
 **expand** | [**List[ExpandEndpointHttpServerOptions]**](ExpandEndpointHttpServerOptions.md)| This parameter is optional and determines whether to expand resources related to test results. By default, no expansion occurs when this query parameter is omitted. To expand a specific resource, such as \&quot;header,\&quot; append &#x60;?expand&#x3D;header&#x60; to the query. | [optional] 
 **http_endpoint_tests_data_rounds_search** | [**HttpEndpointTestsDataRoundsSearch**](HttpEndpointTestsDataRoundsSearch.md)| Test data search filters. | [optional] 

### Return type

[**HttpMultiEndpointTestResults**](HttpMultiEndpointTestResults.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

