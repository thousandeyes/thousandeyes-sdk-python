# thousandeyes_sdk.bgp_updates.BGPUpdatesApi

All URIs are relative to *https://api.thousandeyes.com/v7*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_bgp_updates**](BGPUpdatesApi.md#get_bgp_updates) | **GET** /bgp/updates | List BGP updates


# **get_bgp_updates**
> BgpUpdates get_bgp_updates(aid=aid, max=max, cursor=cursor, expand=expand, start_date=start_date, end_date=end_date, prefixes=prefixes, origin_ases=origin_ases, as_paths=as_paths, rpki_statuses=rpki_statuses, update_type=update_type, monitor_ids=monitor_ids, communities=communities)

List BGP updates

Retrieves a paginated list of BGP updates for prefixes tracked by the account group. When the `prefixes` filter is omitted, updates are returned for all prefixes currently tracked by the account group. Use the returned pagination links to request subsequent pages. 

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.bgp_updates
from thousandeyes_sdk.bgp_updates.models.bgp_data_expand_option import BgpDataExpandOption
from thousandeyes_sdk.bgp_updates.models.bgp_rpki_status import BgpRpkiStatus
from thousandeyes_sdk.bgp_updates.models.bgp_update_type import BgpUpdateType
from thousandeyes_sdk.bgp_updates.models.bgp_updates import BgpUpdates
from thousandeyes_sdk.bgp_updates.rest import ApiException
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
    api_instance = thousandeyes_sdk.bgp_updates.BGPUpdatesApi(api_client)
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)
    max = 20 # int | Maximum number of BGP updates to return. (optional) (default to 20)
    cursor = 'cursor_example' # str | (Optional) Opaque cursor used for pagination. Clients should use `next` value from `_links` instead of this parameter. (optional)
    expand = ["monitor"] # List[BgpDataExpandOption] | Optional expansions. Pass `expand=monitor` to replace monitor IDs with full BGP monitor objects. (optional)
    start_date = '2022-07-17T22:00:54Z' # datetime | Use with the `endDate` parameter. Include the complete time (hours, minutes, and seconds) in UTC time zone, following the ISO 8601 date-time format. See the example for reference. Please note that this parameter can't be used with `window`. (optional)
    end_date = '2022-07-18T22:00:54Z' # datetime | Defaults to current time the request is made. Use with the `startDate` parameter. Include the complete time (hours, minutes, and seconds) in UTC time zone, following the ISO 8601 date-time format. See the example for reference. Please note that this parameter can't be used with `window`. (optional)
    prefixes = ['[\"192.0.2.0/24\"]'] # List[str] | Prefix CIDR filters. Repeat the parameter to filter by multiple prefixes. (optional)
    origin_ases = [[64512]] # List[int] | Origin AS filters. Repeat the parameter to filter by multiple ASNs. (optional)
    as_paths = ['[\"64512 64513\"]'] # List[str] | AS path filters, expressed as a space-separated list of ASNs. Repeat the parameter to filter by multiple AS paths. (optional)
    rpki_statuses = [
                    'Valid'
                    ] # List[BgpRpkiStatus] | RPKI status filters. (optional)
    update_type = [
                    'announcement'
                    ] # List[BgpUpdateType] | BGP update type filters. (optional)
    monitor_ids = ['[\"101\"]'] # List[str] | BGP monitor ID filters. Repeat the parameter to filter by multiple monitors. Get `monitorId` from the `/monitors` endpoint. (optional)
    communities = ['[\"64512:100\"]'] # List[str] | BGP community filters. Repeat the parameter to filter by multiple communities. (optional)

    try:
        # List BGP updates
        api_response = api_instance.get_bgp_updates(aid=aid, max=max, cursor=cursor, expand=expand, start_date=start_date, end_date=end_date, prefixes=prefixes, origin_ases=origin_ases, as_paths=as_paths, rpki_statuses=rpki_statuses, update_type=update_type, monitor_ids=monitor_ids, communities=communities)
        print("The response of BGPUpdatesApi->get_bgp_updates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BGPUpdatesApi->get_bgp_updates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 
 **max** | **int**| Maximum number of BGP updates to return. | [optional] [default to 20]
 **cursor** | **str**| (Optional) Opaque cursor used for pagination. Clients should use &#x60;next&#x60; value from &#x60;_links&#x60; instead of this parameter. | [optional] 
 **expand** | [**List[BgpDataExpandOption]**](BgpDataExpandOption.md)| Optional expansions. Pass &#x60;expand&#x3D;monitor&#x60; to replace monitor IDs with full BGP monitor objects. | [optional] 
 **start_date** | **datetime**| Use with the &#x60;endDate&#x60; parameter. Include the complete time (hours, minutes, and seconds) in UTC time zone, following the ISO 8601 date-time format. See the example for reference. Please note that this parameter can&#39;t be used with &#x60;window&#x60;. | [optional] 
 **end_date** | **datetime**| Defaults to current time the request is made. Use with the &#x60;startDate&#x60; parameter. Include the complete time (hours, minutes, and seconds) in UTC time zone, following the ISO 8601 date-time format. See the example for reference. Please note that this parameter can&#39;t be used with &#x60;window&#x60;. | [optional] 
 **prefixes** | [**List[str]**](str.md)| Prefix CIDR filters. Repeat the parameter to filter by multiple prefixes. | [optional] 
 **origin_ases** | [**List[int]**](int.md)| Origin AS filters. Repeat the parameter to filter by multiple ASNs. | [optional] 
 **as_paths** | [**List[str]**](str.md)| AS path filters, expressed as a space-separated list of ASNs. Repeat the parameter to filter by multiple AS paths. | [optional] 
 **rpki_statuses** | [**List[BgpRpkiStatus]**](BgpRpkiStatus.md)| RPKI status filters. | [optional] 
 **update_type** | [**List[BgpUpdateType]**](BgpUpdateType.md)| BGP update type filters. | [optional] 
 **monitor_ids** | [**List[str]**](str.md)| BGP monitor ID filters. Repeat the parameter to filter by multiple monitors. Get &#x60;monitorId&#x60; from the &#x60;/monitors&#x60; endpoint. | [optional] 
 **communities** | [**List[str]**](str.md)| BGP community filters. Repeat the parameter to filter by multiple communities. | [optional] 

### Return type

[**BgpUpdates**](BgpUpdates.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json, application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of BGP updates. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Insufficient permissions to query endpoint |  -  |
**404** | Not found |  -  |
**429** | Exhausted rate limit for the organization |  -  |
**500** | Internal server error |  -  |
**502** | Bad Gateway |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

