# thousandeyes_sdk.endpoint_test_results.LocalNetworkEndpointTestResultsApi

All URIs are relative to *https://api.thousandeyes.com/v7*

Method | HTTP request | Description
------------- | ------------- | -------------
[**filter_local_networks_test_results_topologies**](LocalNetworkEndpointTestResultsApi.md#filter_local_networks_test_results_topologies) | **POST** /endpoint/test-results/local-networks/topologies/filter | List endpoint network topologies probes
[**get_local_networks_test_results**](LocalNetworkEndpointTestResultsApi.md#get_local_networks_test_results) | **GET** /endpoint/test-results/local-networks | List local networks
[**get_local_networks_test_results_topology**](LocalNetworkEndpointTestResultsApi.md#get_local_networks_test_results_topology) | **GET** /endpoint/test-results/local-networks/topologies/{networkTopologyId} | Retrieve endpoint local network topology


# **filter_local_networks_test_results_topologies**
> LocalNetworkTopologyResults filter_local_networks_test_results_topologies(aid=aid, window=window, start_date=start_date, end_date=end_date, cursor=cursor, expand=expand, endpoint_network_topology_result_request=endpoint_network_topology_result_request)

List endpoint network topologies probes

Returns a list of all endpoint local network topologies probes.  Results from the last round are provided unless an explicit start and end is provided with `startDate`, `endDate` or `window` optional parameters.  ## Request body filters This endpoint supports complex filtering using the request body. It is important these filters remain unaltered when making use of pagination, otherwise the results will not be coherent with the original request.  ### Multiple filter fields When multiple filter fields are provided, a logical `AND` is applied between the filters.  ``` curl --location --request POST 'https://api.thousandeyes.com/v7/endpoint/test-results/local-networks/topologies/filter' --header 'Authorization: Bearer $token' --header 'Content-Type: application/json' --data-raw '{   \"searchFilters\": {     \"platform\": [ \"mac\" ],     \"domain\": [ \"thousandeyes.com\" ]   }}' ```  ### Filter field with multiple values When a filter field contains multiple values, a logical `OR` is applied between the filter values.  ``` curl --location --request POST 'https://api.thousandeyes.com/v7/endpoint/test-results/local-networks/topologies/filter' --header 'Authorization: Bearer $token' --header 'Content-Type: application/json' --data-raw '{   \"searchFilters\": {     \"networkId\": [ \"660b34109d12\", \"660b34109d15\" ]   }}' ```  ### Combination of request parameters and body filters ``` curl --location --request POST 'https://api.thousandeyes.com/v7/endpoint/test-results/local-networks/topologies/filter?window=12h' --header 'Authorization: Bearer $token' --header 'Content-Type: application/json' --data-raw '{   \"searchFilters\": {     \"platform\": [ \"mac\" ],     \"domain\": [ \"thousandeyes.com\" ],     \"networkId\": [ \"660b34109d12\", \"660b34109d15\" ]   }}' ```  ### Warning Note that a maximum of 12h worth of data can be retrieved at once.  If you need more, you need to make multiple requests.  Returns a `results` array of network topology probes.  Network topology probes shown are from the latest round, or based on the time range specified. 

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.endpoint_test_results
from thousandeyes_sdk.endpoint_test_results.models.endpoint_network_topology_result_request import EndpointNetworkTopologyResultRequest
from thousandeyes_sdk.endpoint_test_results.models.expand_local_network_topology_options import ExpandLocalNetworkTopologyOptions
from thousandeyes_sdk.endpoint_test_results.models.local_network_topology_results import LocalNetworkTopologyResults
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
    api_instance = thousandeyes_sdk.endpoint_test_results.LocalNetworkEndpointTestResultsApi(api_client)
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)
    window = '12h' # str | A dynamic time interval up to the current time of the request. Specify the interval as a number followed by an optional type: `s` for seconds (default if no type is specified), `m` for minutes, `h` for hours, `d` for days, and `w` for weeks. For a precise date range, use `startDate` and `endDate`. (optional)
    start_date = '2022-07-17T22:00:54Z' # datetime | Use with the `endDate` parameter. Include the complete time (hours, minutes, and seconds) in UTC time zone, following the ISO 8601 date-time format. See the example for reference. Please note that this parameter can't be used with `window`. (optional)
    end_date = '2022-07-18T22:00:54Z' # datetime | Defaults to current time the request is made. Use with the `startDate` parameter. Include the complete time (hours, minutes, and seconds) in UTC time zone, following the ISO 8601 date-time format. See the example for reference. Please note that this parameter can't be used with `window`. (optional)
    cursor = 'cursor_example' # str | (Optional) Opaque cursor used for pagination. Clients should use `next` value from `_links` instead of this parameter. (optional)
    expand = [thousandeyes_sdk.endpoint_test_results.ExpandLocalNetworkTopologyOptions()] # List[ExpandLocalNetworkTopologyOptions] | This parameter is optional and determines whether to expand resources related to local network topologies. By default, no expansion occurs when this query parameter is omitted. To expand a specific resource, such as `systemMetricDetails`, append  `?expand=system-metric-detail` to the query. (optional)
    endpoint_network_topology_result_request = thousandeyes_sdk.endpoint_test_results.EndpointNetworkTopologyResultRequest() # EndpointNetworkTopologyResultRequest |  (optional)

    try:
        # List endpoint network topologies probes
        api_response = api_instance.filter_local_networks_test_results_topologies(aid=aid, window=window, start_date=start_date, end_date=end_date, cursor=cursor, expand=expand, endpoint_network_topology_result_request=endpoint_network_topology_result_request)
        print("The response of LocalNetworkEndpointTestResultsApi->filter_local_networks_test_results_topologies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocalNetworkEndpointTestResultsApi->filter_local_networks_test_results_topologies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 
 **window** | **str**| A dynamic time interval up to the current time of the request. Specify the interval as a number followed by an optional type: &#x60;s&#x60; for seconds (default if no type is specified), &#x60;m&#x60; for minutes, &#x60;h&#x60; for hours, &#x60;d&#x60; for days, and &#x60;w&#x60; for weeks. For a precise date range, use &#x60;startDate&#x60; and &#x60;endDate&#x60;. | [optional] 
 **start_date** | **datetime**| Use with the &#x60;endDate&#x60; parameter. Include the complete time (hours, minutes, and seconds) in UTC time zone, following the ISO 8601 date-time format. See the example for reference. Please note that this parameter can&#39;t be used with &#x60;window&#x60;. | [optional] 
 **end_date** | **datetime**| Defaults to current time the request is made. Use with the &#x60;startDate&#x60; parameter. Include the complete time (hours, minutes, and seconds) in UTC time zone, following the ISO 8601 date-time format. See the example for reference. Please note that this parameter can&#39;t be used with &#x60;window&#x60;. | [optional] 
 **cursor** | **str**| (Optional) Opaque cursor used for pagination. Clients should use &#x60;next&#x60; value from &#x60;_links&#x60; instead of this parameter. | [optional] 
 **expand** | [**List[ExpandLocalNetworkTopologyOptions]**](ExpandLocalNetworkTopologyOptions.md)| This parameter is optional and determines whether to expand resources related to local network topologies. By default, no expansion occurs when this query parameter is omitted. To expand a specific resource, such as &#x60;systemMetricDetails&#x60;, append  &#x60;?expand&#x3D;system-metric-detail&#x60; to the query. | [optional] 
 **endpoint_network_topology_result_request** | [**EndpointNetworkTopologyResultRequest**](EndpointNetworkTopologyResultRequest.md)|  | [optional] 

### Return type

[**LocalNetworkTopologyResults**](LocalNetworkTopologyResults.md)

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

# **get_local_networks_test_results**
> LocalNetworkResults get_local_networks_test_results(aid=aid)

List local networks

Returns a list of all the networks used by endpoint agents.  Sends back a `localNetworks` array. 

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.endpoint_test_results
from thousandeyes_sdk.endpoint_test_results.models.local_network_results import LocalNetworkResults
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
    api_instance = thousandeyes_sdk.endpoint_test_results.LocalNetworkEndpointTestResultsApi(api_client)
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # List local networks
        api_response = api_instance.get_local_networks_test_results(aid=aid)
        print("The response of LocalNetworkEndpointTestResultsApi->get_local_networks_test_results:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocalNetworkEndpointTestResultsApi->get_local_networks_test_results: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

[**LocalNetworkResults**](LocalNetworkResults.md)

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

# **get_local_networks_test_results_topology**
> LocalNetworkTopologyDetailResults get_local_networks_test_results_topology(network_topology_id, aid=aid, expand=expand)

Retrieve endpoint local network topology

Returns detailed data of a local network topology. 

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.endpoint_test_results
from thousandeyes_sdk.endpoint_test_results.models.expand_local_network_topology_options import ExpandLocalNetworkTopologyOptions
from thousandeyes_sdk.endpoint_test_results.models.local_network_topology_detail_results import LocalNetworkTopologyDetailResults
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
    api_instance = thousandeyes_sdk.endpoint_test_results.LocalNetworkEndpointTestResultsApi(api_client)
    network_topology_id = '00160:39c518560de9:1491651900:236e6f18' # str | The network topology ID.
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)
    expand = [thousandeyes_sdk.endpoint_test_results.ExpandLocalNetworkTopologyOptions()] # List[ExpandLocalNetworkTopologyOptions] | This parameter is optional and determines whether to expand resources related to local network topologies. By default, no expansion occurs when this query parameter is omitted. To expand a specific resource, such as `systemMetricDetails`, append  `?expand=system-metric-detail` to the query. (optional)

    try:
        # Retrieve endpoint local network topology
        api_response = api_instance.get_local_networks_test_results_topology(network_topology_id, aid=aid, expand=expand)
        print("The response of LocalNetworkEndpointTestResultsApi->get_local_networks_test_results_topology:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocalNetworkEndpointTestResultsApi->get_local_networks_test_results_topology: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_topology_id** | **str**| The network topology ID. | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 
 **expand** | [**List[ExpandLocalNetworkTopologyOptions]**](ExpandLocalNetworkTopologyOptions.md)| This parameter is optional and determines whether to expand resources related to local network topologies. By default, no expansion occurs when this query parameter is omitted. To expand a specific resource, such as &#x60;systemMetricDetails&#x60;, append  &#x60;?expand&#x3D;system-metric-detail&#x60; to the query. | [optional] 

### Return type

[**LocalNetworkTopologyDetailResults**](LocalNetworkTopologyDetailResults.md)

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

