# thousandeyes_sdk.test_results.NetworkBGPTestMetricsApi

All URIs are relative to *https://api.thousandeyes.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_test_results_bgp**](NetworkBGPTestMetricsApi.md#get_test_results_bgp) | **GET** /v7/test-results/{testId}/bgp | Get BGP test results
[**get_test_results_bgp_prefix**](NetworkBGPTestMetricsApi.md#get_test_results_bgp_prefix) | **GET** /v7/test-results/{testId}/bgp/routes/prefix/{prefixId}/round/{roundId} | Get BGP route test results by prefix


# **get_test_results_bgp**
> BgpTestResults get_test_results_bgp(test_id, aid=aid, window=window, start_date=start_date, end_date=end_date, cursor=cursor)

Get BGP test results

Returns a list of BGP monitors actively monitoring the destination's target prefix. This list includes information about the prefix, its associated AS Number, and provides details regarding reachability, path updates, and any changes in the path for the target network. 

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.test_results
from thousandeyes_sdk.test_results.models.bgp_test_results import BgpTestResults
from thousandeyes_sdk.test_results.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.thousandeyes.com
# See configuration.py for a list of all supported configuration parameters.
configuration = thousandeyes_sdk.client.Configuration(
    host = "https://api.thousandeyes.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = thousandeyes_sdk.client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with thousandeyes_sdk.test_results.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = thousandeyes_sdk.test_results.NetworkBGPTestMetricsApi(api_client)
    test_id = '202701' # str | Test ID
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)
    window = '12h' # str | A dynamic time interval up to the current time of the request. Specify the interval as a number followed by an optional type: `s` for seconds (default if no type is specified), `m` for minutes, `h` for hours, `d` for days, and `w` for weeks. For a precise date range, use `startDate` and `endDate`. (optional)
    start_date = '2022-07-17T22:00:54Z' # datetime | Use with the `endDate` parameter. Include the complete time (hours, minutes, and seconds) in UTC time zone, following the ISO 8601 date-time format. See the example for reference. Please note that this parameter can't be used with `window`. (optional)
    end_date = '2022-07-18T22:00:54Z' # datetime | Defaults to current time the request is made. Use with the `startDate` parameter. Include the complete time (hours, minutes, and seconds) in UTC time zone, following the ISO 8601 date-time format. See the example for reference. Please note that this parameter can't be used with `window`. (optional)
    cursor = 'cursor_example' # str | (Optional) Opaque cursor used for pagination. Clients should use `next` value from `_links` instead of this parameter. (optional)

    try:
        # Get BGP test results
        api_response = api_instance.get_test_results_bgp(test_id, aid=aid, window=window, start_date=start_date, end_date=end_date, cursor=cursor)
        print("The response of NetworkBGPTestMetricsApi->get_test_results_bgp:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkBGPTestMetricsApi->get_test_results_bgp: %s\n" % e)
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

[**BgpTestResults**](BgpTestResults.md)

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
**0** | An error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_test_results_bgp_prefix**
> BgpTestRouteInformationResults get_test_results_bgp_prefix(test_id, prefix_id, round_id, aid=aid)

Get BGP route test results by prefix

Returns an ordered list of networks crossed by a particular network prefix, including assigned monitors for the test and the paths taken to reach the destination. This is similar to revealing ASPath details found in a BGP Routing Information Base (rib) dump. 

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.test_results
from thousandeyes_sdk.test_results.models.bgp_test_route_information_results import BgpTestRouteInformationResults
from thousandeyes_sdk.test_results.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.thousandeyes.com
# See configuration.py for a list of all supported configuration parameters.
configuration = thousandeyes_sdk.client.Configuration(
    host = "https://api.thousandeyes.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = thousandeyes_sdk.client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with thousandeyes_sdk.test_results.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = thousandeyes_sdk.test_results.NetworkBGPTestMetricsApi(api_client)
    test_id = '202701' # str | Test ID
    prefix_id = '3789376546' # str | The ID of the prefix. You can get `prefixId` from the `/test-results/{testId}/bgp` endpoint.
    round_id = '1384309800' # str | Round ID
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Get BGP route test results by prefix
        api_response = api_instance.get_test_results_bgp_prefix(test_id, prefix_id, round_id, aid=aid)
        print("The response of NetworkBGPTestMetricsApi->get_test_results_bgp_prefix:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkBGPTestMetricsApi->get_test_results_bgp_prefix: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_id** | **str**| Test ID | 
 **prefix_id** | **str**| The ID of the prefix. You can get &#x60;prefixId&#x60; from the &#x60;/test-results/{testId}/bgp&#x60; endpoint. | 
 **round_id** | **str**| Round ID | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

[**BgpTestRouteInformationResults**](BgpTestRouteInformationResults.md)

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
**0** | An error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

