# thousandeyes_sdk.endpoint_agents.EndpointAgentLogItemsApi

All URIs are relative to *https://api.thousandeyes.com/v7*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_endpoint_agent_log_items**](EndpointAgentLogItemsApi.md#get_endpoint_agent_log_items) | **GET** /endpoint/agents/{agentId}/logs | List endpoint agent log items


# **get_endpoint_agent_log_items**
> EndpointAgentLogItemsResponse get_endpoint_agent_log_items(agent_id, aid=aid, max=max, cursor=cursor, window=window, start_date=start_date, end_date=end_date)

List endpoint agent log items

Returns paginated logs for an endpoint agent within the requested time range.

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.endpoint_agents
from thousandeyes_sdk.endpoint_agents.models.endpoint_agent_log_items_response import EndpointAgentLogItemsResponse
from thousandeyes_sdk.endpoint_agents.rest import ApiException
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
    api_instance = thousandeyes_sdk.endpoint_agents.EndpointAgentLogItemsApi(api_client)
    agent_id = 'agent_id_example' # str | The identifier of the agent to operate on.
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)
    max = 1000 # int | Maximum number of log items returned per page. (optional) (default to 1000)
    cursor = 'WyIxNzA5MjQwMDAwMDAwIl0=' # str | Opaque cursor from the `_links.next.href` URL in the previous response. (optional)
    window = '12h' # str | A dynamic time interval up to the current time of the request. Specify the interval as a number followed by an optional type: `s` for seconds (default if no type is specified), `m` for minutes, `h` for hours, `d` for days, and `w` for weeks. For a precise date range, use `startDate` and `endDate`. (optional)
    start_date = '2022-07-17T22:00:54Z' # datetime | Use with the `endDate` parameter. Include the complete time (hours, minutes, and seconds) in UTC time zone, following the ISO 8601 date-time format. See the example for reference. Please note that this parameter can't be used with `window`. (optional)
    end_date = '2022-07-18T22:00:54Z' # datetime | Defaults to current time the request is made. Use with the `startDate` parameter. Include the complete time (hours, minutes, and seconds) in UTC time zone, following the ISO 8601 date-time format. See the example for reference. Please note that this parameter can't be used with `window`. (optional)

    try:
        # List endpoint agent log items
        api_response = api_instance.get_endpoint_agent_log_items(agent_id, aid=aid, max=max, cursor=cursor, window=window, start_date=start_date, end_date=end_date)
        print("The response of EndpointAgentLogItemsApi->get_endpoint_agent_log_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointAgentLogItemsApi->get_endpoint_agent_log_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **str**| The identifier of the agent to operate on. | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 
 **max** | **int**| Maximum number of log items returned per page. | [optional] [default to 1000]
 **cursor** | **str**| Opaque cursor from the &#x60;_links.next.href&#x60; URL in the previous response. | [optional] 
 **window** | **str**| A dynamic time interval up to the current time of the request. Specify the interval as a number followed by an optional type: &#x60;s&#x60; for seconds (default if no type is specified), &#x60;m&#x60; for minutes, &#x60;h&#x60; for hours, &#x60;d&#x60; for days, and &#x60;w&#x60; for weeks. For a precise date range, use &#x60;startDate&#x60; and &#x60;endDate&#x60;. | [optional] 
 **start_date** | **datetime**| Use with the &#x60;endDate&#x60; parameter. Include the complete time (hours, minutes, and seconds) in UTC time zone, following the ISO 8601 date-time format. See the example for reference. Please note that this parameter can&#39;t be used with &#x60;window&#x60;. | [optional] 
 **end_date** | **datetime**| Defaults to current time the request is made. Use with the &#x60;startDate&#x60; parameter. Include the complete time (hours, minutes, and seconds) in UTC time zone, following the ISO 8601 date-time format. See the example for reference. Please note that this parameter can&#39;t be used with &#x60;window&#x60;. | [optional] 

### Return type

[**EndpointAgentLogItemsResponse**](EndpointAgentLogItemsResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json, application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Paginated logs for the endpoint agent. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Insufficient permissions to query endpoint |  -  |
**429** | Exhausted rate limit for the organization |  -  |
**500** | Internal server error |  -  |
**502** | Bad Gateway |  -  |
**0** | An error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

