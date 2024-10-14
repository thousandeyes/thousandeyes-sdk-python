# thousandeyes_sdk.endpoint_test_results.RealUserEndpointTestResultsApi

All URIs are relative to *https://api.thousandeyes.com/v7*

Method | HTTP request | Description
------------- | ------------- | -------------
[**filter_real_user_tests_network_results**](RealUserEndpointTestResultsApi.md#filter_real_user_tests_network_results) | **POST** /endpoint/test-results/real-user-tests/networks/filter | List endpoint real user tests
[**filter_real_user_tests_results**](RealUserEndpointTestResultsApi.md#filter_real_user_tests_results) | **POST** /endpoint/test-results/real-user-tests/filter | List endpoint real user tests
[**filter_real_user_tests_visited_pages_results**](RealUserEndpointTestResultsApi.md#filter_real_user_tests_visited_pages_results) | **POST** /endpoint/test-results/real-user-tests/pages/filter | List endpoint real user tests visited pages
[**get_real_user_test_page_results**](RealUserEndpointTestResultsApi.md#get_real_user_test_page_results) | **GET** /endpoint/test-results/real-user-tests/{id}/pages/{pageId} | Retrieve endpoint real user test page
[**get_real_user_test_results**](RealUserEndpointTestResultsApi.md#get_real_user_test_results) | **GET** /endpoint/test-results/real-user-tests/{id} | Retrieve endpoint real user test


# **filter_real_user_tests_network_results**
> RealUserEndpointTestNetworkResults filter_real_user_tests_network_results(aid=aid, window=window, start_date=start_date, end_date=end_date, cursor=cursor, real_user_endpoint_test_results_request=real_user_endpoint_test_results_request)

List endpoint real user tests

Returns a list of all endpoint real user tests.  Sessions from the last round are provided unless an explicit start and end is provided with `startDate`, `endDate` or `window` optional parameters.  ## Request body filters This endpoint supports complex filtering using the request body. It is important these filters remain unaltered when making use of pagination, otherwise the results will not be coherent with the original request.  ### Multiple filter fields When multiple filter fields are provided, a logical `AND` is applied between the filters.  ``` curl --location --request POST 'https://api.thousandeyes.com/v7/endpoint/test-results/real-user-tests/networks/filter' --header 'Authorization: Bearer $token' --header 'Content-Type: application/json' --data-raw '{    \"searchFilters\": {     \"platform\": [ \"mac\" ],     \"domain\": [ \"thousandeyes.com\" ]   }}' ```  ### Filter field with multiple values When a filter field contains multiple values, a logical `OR` is applied between the filter values.  ``` curl --location --request POST 'https://api.thousandeyes.com/v7/endpoint/test-results/real-user-tests/networks/filter' --header 'Authorization: Bearer $token' --header 'Content-Type: application/json' --data-raw '{   \"searchFilters\": {     \"networkId\": [ \"660b34109d12\", \"660b34109d15\" ]   }}' ```  ### Combination of request parameters and body filters ``` curl --location --request POST 'https://api.thousandeyes.com/v7/endpoint/test-results/real-user-tests/networks/filter?window=1w' --header 'Authorization: Bearer $token' --header 'Content-Type: application/json' --data-raw '{   \"searchFilters\": {     \"platform\": [ \"mac\" ],     \"domain\": [ \"thousandeyes.com\" ],     \"networkId\": [ \"660b34109d12\", \"660b34109d15\" ]   }}' ```  Returns a `results` array of endpoint real user tests.  Network sessions shown are from the latest round, or based on the time range specified. 

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.endpoint_test_results
from thousandeyes_sdk.endpoint_test_results.models.real_user_endpoint_test_network_results import RealUserEndpointTestNetworkResults
from thousandeyes_sdk.endpoint_test_results.models.real_user_endpoint_test_results_request import RealUserEndpointTestResultsRequest
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
    api_instance = thousandeyes_sdk.endpoint_test_results.RealUserEndpointTestResultsApi(api_client)
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)
    window = '12h' # str | A dynamic time interval up to the current time of the request. Specify the interval as a number followed by an optional type: `s` for seconds (default if no type is specified), `m` for minutes, `h` for hours, `d` for days, and `w` for weeks. For a precise date range, use `startDate` and `endDate`. (optional)
    start_date = '2022-07-17T22:00:54Z' # datetime | Use with the `endDate` parameter. Include the complete time (hours, minutes, and seconds) in UTC time zone, following the ISO 8601 date-time format. See the example for reference. Please note that this parameter can't be used with `window`. (optional)
    end_date = '2022-07-18T22:00:54Z' # datetime | Defaults to current time the request is made. Use with the `startDate` parameter. Include the complete time (hours, minutes, and seconds) in UTC time zone, following the ISO 8601 date-time format. See the example for reference. Please note that this parameter can't be used with `window`. (optional)
    cursor = 'cursor_example' # str | (Optional) Opaque cursor used for pagination. Clients should use `next` value from `_links` instead of this parameter. (optional)
    real_user_endpoint_test_results_request = thousandeyes_sdk.endpoint_test_results.RealUserEndpointTestResultsRequest() # RealUserEndpointTestResultsRequest |  (optional)

    try:
        # List endpoint real user tests
        api_response = api_instance.filter_real_user_tests_network_results(aid=aid, window=window, start_date=start_date, end_date=end_date, cursor=cursor, real_user_endpoint_test_results_request=real_user_endpoint_test_results_request)
        print("The response of RealUserEndpointTestResultsApi->filter_real_user_tests_network_results:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RealUserEndpointTestResultsApi->filter_real_user_tests_network_results: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 
 **window** | **str**| A dynamic time interval up to the current time of the request. Specify the interval as a number followed by an optional type: &#x60;s&#x60; for seconds (default if no type is specified), &#x60;m&#x60; for minutes, &#x60;h&#x60; for hours, &#x60;d&#x60; for days, and &#x60;w&#x60; for weeks. For a precise date range, use &#x60;startDate&#x60; and &#x60;endDate&#x60;. | [optional] 
 **start_date** | **datetime**| Use with the &#x60;endDate&#x60; parameter. Include the complete time (hours, minutes, and seconds) in UTC time zone, following the ISO 8601 date-time format. See the example for reference. Please note that this parameter can&#39;t be used with &#x60;window&#x60;. | [optional] 
 **end_date** | **datetime**| Defaults to current time the request is made. Use with the &#x60;startDate&#x60; parameter. Include the complete time (hours, minutes, and seconds) in UTC time zone, following the ISO 8601 date-time format. See the example for reference. Please note that this parameter can&#39;t be used with &#x60;window&#x60;. | [optional] 
 **cursor** | **str**| (Optional) Opaque cursor used for pagination. Clients should use &#x60;next&#x60; value from &#x60;_links&#x60; instead of this parameter. | [optional] 
 **real_user_endpoint_test_results_request** | [**RealUserEndpointTestResultsRequest**](RealUserEndpointTestResultsRequest.md)|  | [optional] 

### Return type

[**RealUserEndpointTestNetworkResults**](RealUserEndpointTestNetworkResults.md)

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

# **filter_real_user_tests_results**
> RealUserEndpointTestResults filter_real_user_tests_results(aid=aid, window=window, start_date=start_date, end_date=end_date, cursor=cursor, real_user_endpoint_test_results_request=real_user_endpoint_test_results_request)

List endpoint real user tests

Returns a list of all endpoint real user tests. Results from the last round are provided unless an explicit start and end is provided with `startDate`, `endDate` or `window` optional parameters.  ## Request body filters This endpoint supports complex filtering using the request body. It is important these filters remain unaltered when making use of pagination, otherwise the results will not be coherent with the original request.  ### Multiple filter fields When multiple filter fields are provided, a logical `AND` is applied between the filters.  ``` curl --location --request POST 'https://api.thousandeyes.com/v7/endpoint/test-results/real-user-tests/filter' --header 'Authorization: Bearer $token' --header 'Content-Type: application/json' --data-raw '{   \"searchFilters\": {     \"platform\": [ \"mac\" ],     \"domain\": [ \"thousandeyes.com\" ]   }}' ```  ### Filter field with multiple values When a filter field contains multiple values, a logical `OR` is applied between the filter values.  ``` curl --location --request POST 'https://api.thousandeyes.com/v7/endpoint/test-results/real-user-tests/filter' --header 'Authorization: Bearer $token' --header 'Content-Type: application/json' --data-raw '{     \"searchFilters\": {       \"networkId\": [ \"660b34109d12\", \"660b34109d15\" ]     }   }' ```  ### Combination of request parameters and body filters ``` curl --location --request POST 'https://api.thousandeyes.com/v7/endpoint/test-results/real-user-tests/filter?window=1w' --header 'Authorization: Bearer $token' --header 'Content-Type: application/json' --data-raw '{     \"searchFilters\": {       \"platform\": [ \"mac\" ],       \"domain\": [ \"thousandeyes.com\" ],       \"networkId\": [ \"660b34109d12\", \"660b34109d15\" ]     }   }' ```  Returns a `results` array of endpoint real user tests. Either the latest results, or based on the time range and body filters specified. 

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.endpoint_test_results
from thousandeyes_sdk.endpoint_test_results.models.real_user_endpoint_test_results import RealUserEndpointTestResults
from thousandeyes_sdk.endpoint_test_results.models.real_user_endpoint_test_results_request import RealUserEndpointTestResultsRequest
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
    api_instance = thousandeyes_sdk.endpoint_test_results.RealUserEndpointTestResultsApi(api_client)
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)
    window = '12h' # str | A dynamic time interval up to the current time of the request. Specify the interval as a number followed by an optional type: `s` for seconds (default if no type is specified), `m` for minutes, `h` for hours, `d` for days, and `w` for weeks. For a precise date range, use `startDate` and `endDate`. (optional)
    start_date = '2022-07-17T22:00:54Z' # datetime | Use with the `endDate` parameter. Include the complete time (hours, minutes, and seconds) in UTC time zone, following the ISO 8601 date-time format. See the example for reference. Please note that this parameter can't be used with `window`. (optional)
    end_date = '2022-07-18T22:00:54Z' # datetime | Defaults to current time the request is made. Use with the `startDate` parameter. Include the complete time (hours, minutes, and seconds) in UTC time zone, following the ISO 8601 date-time format. See the example for reference. Please note that this parameter can't be used with `window`. (optional)
    cursor = 'cursor_example' # str | (Optional) Opaque cursor used for pagination. Clients should use `next` value from `_links` instead of this parameter. (optional)
    real_user_endpoint_test_results_request = thousandeyes_sdk.endpoint_test_results.RealUserEndpointTestResultsRequest() # RealUserEndpointTestResultsRequest |  (optional)

    try:
        # List endpoint real user tests
        api_response = api_instance.filter_real_user_tests_results(aid=aid, window=window, start_date=start_date, end_date=end_date, cursor=cursor, real_user_endpoint_test_results_request=real_user_endpoint_test_results_request)
        print("The response of RealUserEndpointTestResultsApi->filter_real_user_tests_results:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RealUserEndpointTestResultsApi->filter_real_user_tests_results: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 
 **window** | **str**| A dynamic time interval up to the current time of the request. Specify the interval as a number followed by an optional type: &#x60;s&#x60; for seconds (default if no type is specified), &#x60;m&#x60; for minutes, &#x60;h&#x60; for hours, &#x60;d&#x60; for days, and &#x60;w&#x60; for weeks. For a precise date range, use &#x60;startDate&#x60; and &#x60;endDate&#x60;. | [optional] 
 **start_date** | **datetime**| Use with the &#x60;endDate&#x60; parameter. Include the complete time (hours, minutes, and seconds) in UTC time zone, following the ISO 8601 date-time format. See the example for reference. Please note that this parameter can&#39;t be used with &#x60;window&#x60;. | [optional] 
 **end_date** | **datetime**| Defaults to current time the request is made. Use with the &#x60;startDate&#x60; parameter. Include the complete time (hours, minutes, and seconds) in UTC time zone, following the ISO 8601 date-time format. See the example for reference. Please note that this parameter can&#39;t be used with &#x60;window&#x60;. | [optional] 
 **cursor** | **str**| (Optional) Opaque cursor used for pagination. Clients should use &#x60;next&#x60; value from &#x60;_links&#x60; instead of this parameter. | [optional] 
 **real_user_endpoint_test_results_request** | [**RealUserEndpointTestResultsRequest**](RealUserEndpointTestResultsRequest.md)|  | [optional] 

### Return type

[**RealUserEndpointTestResults**](RealUserEndpointTestResults.md)

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

# **filter_real_user_tests_visited_pages_results**
> RealUserEndpointTestPageResults filter_real_user_tests_visited_pages_results(aid=aid, window=window, start_date=start_date, end_date=end_date, cursor=cursor, real_user_endpoint_test_result_request_filter=real_user_endpoint_test_result_request_filter)

List endpoint real user tests visited pages

Returns a list of all endpoint real user tests visited pages.  Sessions from the last round are provided unless an explicit start and end is provided with `startDate`, `endDate` or `window` optional parameters.  ## Request body filters This endpoint supports complex filtering using the request body. It is important these filters remain unaltered when making use of pagination, otherwise the results will not be coherent with the original request.  ### Multiple filter fields When multiple filter fields are provided, a logical `AND` is applied between the filters.  ``` curl --location --request POST 'https://api.thousandeyes.com/v7/endpoint/test-results/real-user-tests/pages/filter' --header 'Authorization: Bearer $token' --header 'Content-Type: application/json' --data-raw '{   \"searchFilters\": {     \"platform\": [ \"mac\" ],     \"domain\": [ \"thousandeyes.com\" ]   }}' ```  ### Filter field with multiple values When a filter field contains multiple values, a logical `OR` is applied between the filter values.  ``` curl --location --request POST 'https://api.thousandeyes.com/v7/endpoint/test-results/real-user-tests/pages/filter' --header 'Authorization: Bearer $token' --header 'Content-Type: application/json' --data-raw '{   \"searchFilters\": {     \"networkId\": [ \"660b34109d12\", \"660b34109d15\" ]   }}' ```  ### Combination of request parameters and body filters ``` curl --location --request POST 'https://api.thousandeyes.com/v7/endpoint/test-results/real-user-tests/pages/filter?window=1w' --header 'Authorization: Bearer $token' --header 'Content-Type: application/json' --data-raw '{   \"searchFilters\": {     \"platform\": [ \"mac\" ],     \"domain\": [ \"thousandeyes.com\" ],     \"networkId\": [ \"660b34109d12\", \"660b34109d15\" ]   }}' ```  Returns a `results` array of user loaded pages in an endpoint real user test.  Pages shown are from the latest round, or based on the time range specified. 

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.endpoint_test_results
from thousandeyes_sdk.endpoint_test_results.models.real_user_endpoint_test_page_results import RealUserEndpointTestPageResults
from thousandeyes_sdk.endpoint_test_results.models.real_user_endpoint_test_result_request_filter import RealUserEndpointTestResultRequestFilter
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
    api_instance = thousandeyes_sdk.endpoint_test_results.RealUserEndpointTestResultsApi(api_client)
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)
    window = '12h' # str | A dynamic time interval up to the current time of the request. Specify the interval as a number followed by an optional type: `s` for seconds (default if no type is specified), `m` for minutes, `h` for hours, `d` for days, and `w` for weeks. For a precise date range, use `startDate` and `endDate`. (optional)
    start_date = '2022-07-17T22:00:54Z' # datetime | Use with the `endDate` parameter. Include the complete time (hours, minutes, and seconds) in UTC time zone, following the ISO 8601 date-time format. See the example for reference. Please note that this parameter can't be used with `window`. (optional)
    end_date = '2022-07-18T22:00:54Z' # datetime | Defaults to current time the request is made. Use with the `startDate` parameter. Include the complete time (hours, minutes, and seconds) in UTC time zone, following the ISO 8601 date-time format. See the example for reference. Please note that this parameter can't be used with `window`. (optional)
    cursor = 'cursor_example' # str | (Optional) Opaque cursor used for pagination. Clients should use `next` value from `_links` instead of this parameter. (optional)
    real_user_endpoint_test_result_request_filter = thousandeyes_sdk.endpoint_test_results.RealUserEndpointTestResultRequestFilter() # RealUserEndpointTestResultRequestFilter |  (optional)

    try:
        # List endpoint real user tests visited pages
        api_response = api_instance.filter_real_user_tests_visited_pages_results(aid=aid, window=window, start_date=start_date, end_date=end_date, cursor=cursor, real_user_endpoint_test_result_request_filter=real_user_endpoint_test_result_request_filter)
        print("The response of RealUserEndpointTestResultsApi->filter_real_user_tests_visited_pages_results:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RealUserEndpointTestResultsApi->filter_real_user_tests_visited_pages_results: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 
 **window** | **str**| A dynamic time interval up to the current time of the request. Specify the interval as a number followed by an optional type: &#x60;s&#x60; for seconds (default if no type is specified), &#x60;m&#x60; for minutes, &#x60;h&#x60; for hours, &#x60;d&#x60; for days, and &#x60;w&#x60; for weeks. For a precise date range, use &#x60;startDate&#x60; and &#x60;endDate&#x60;. | [optional] 
 **start_date** | **datetime**| Use with the &#x60;endDate&#x60; parameter. Include the complete time (hours, minutes, and seconds) in UTC time zone, following the ISO 8601 date-time format. See the example for reference. Please note that this parameter can&#39;t be used with &#x60;window&#x60;. | [optional] 
 **end_date** | **datetime**| Defaults to current time the request is made. Use with the &#x60;startDate&#x60; parameter. Include the complete time (hours, minutes, and seconds) in UTC time zone, following the ISO 8601 date-time format. See the example for reference. Please note that this parameter can&#39;t be used with &#x60;window&#x60;. | [optional] 
 **cursor** | **str**| (Optional) Opaque cursor used for pagination. Clients should use &#x60;next&#x60; value from &#x60;_links&#x60; instead of this parameter. | [optional] 
 **real_user_endpoint_test_result_request_filter** | [**RealUserEndpointTestResultRequestFilter**](RealUserEndpointTestResultRequestFilter.md)|  | [optional] 

### Return type

[**RealUserEndpointTestPageResults**](RealUserEndpointTestPageResults.md)

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

# **get_real_user_test_page_results**
> RealUserEndpointTestPageDetailResult get_real_user_test_page_results(id, page_id, aid=aid)

Retrieve endpoint real user test page

Returns details for endpoint real user test web page request.  Provides complete waterfall information with all object requests.  Sends back detailed endpoint real user test web page request.  Returned object has a single field: `har` which is an HAR object according to the HTTP Archive 1.2 specifications.  [You can read more about the specification](http://www.softwareishard.com/blog/har-12-spec/).  In addition to standard fields, the object har includes a custom property `systemMetrics` which contain metrics about CPU and physical memory usage.  Check `SystemMetrics` on schemas tab for more information. 

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.endpoint_test_results
from thousandeyes_sdk.endpoint_test_results.models.real_user_endpoint_test_page_detail_result import RealUserEndpointTestPageDetailResult
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
    api_instance = thousandeyes_sdk.endpoint_test_results.RealUserEndpointTestResultsApi(api_client)
    id = '07625:1490529480:h3qJQTpl' # str | The real user test id.
    page_id = '281474976710706' # str | Web page ID
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Retrieve endpoint real user test page
        api_response = api_instance.get_real_user_test_page_results(id, page_id, aid=aid)
        print("The response of RealUserEndpointTestResultsApi->get_real_user_test_page_results:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RealUserEndpointTestResultsApi->get_real_user_test_page_results: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The real user test id. | 
 **page_id** | **str**| Web page ID | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

[**RealUserEndpointTestPageDetailResult**](RealUserEndpointTestPageDetailResult.md)

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

# **get_real_user_test_results**
> RealUserEndpointTestDetailResults get_real_user_test_results(id, aid=aid)

Retrieve endpoint real user test

Provides details for an endpoint real user test. Returns a results array containing detailed information about endpoint real user tests.\" 

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.endpoint_test_results
from thousandeyes_sdk.endpoint_test_results.models.real_user_endpoint_test_detail_results import RealUserEndpointTestDetailResults
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
    api_instance = thousandeyes_sdk.endpoint_test_results.RealUserEndpointTestResultsApi(api_client)
    id = '07625:1490529480:h3qJQTpl' # str | The real user test id.
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Retrieve endpoint real user test
        api_response = api_instance.get_real_user_test_results(id, aid=aid)
        print("The response of RealUserEndpointTestResultsApi->get_real_user_test_results:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RealUserEndpointTestResultsApi->get_real_user_test_results: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The real user test id. | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

[**RealUserEndpointTestDetailResults**](RealUserEndpointTestDetailResults.md)

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

