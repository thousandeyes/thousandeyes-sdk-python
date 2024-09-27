# PathVisDetailDynamicEndpointTestResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aid** | **str** | A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. | [optional] 
**test_id** | **str** | Unique ID of endpoint test. | [optional] [readonly] 
**agent_id** | **str** | Unique ID of endpoint agent, from &#x60;/endpoint/agents&#x60; endpoint. | [optional] [readonly] 
**round_id** | **int** | Epoch time (seconds) indicating the start time of the round. | [optional] [readonly] 
**server_ip** | **str** | IP address of target server. | [optional] [readonly] 
**network_profile** | [**NetworkProfile**](NetworkProfile.md) |  | [optional] 
**system_metrics** | [**SystemMetrics**](SystemMetrics.md) |  | [optional] 
**original_target_profile** | [**TargetProfile**](TargetProfile.md) |  | [optional] 
**vpn_profile** | [**VpnProfile**](VpnProfile.md) |  | [optional] 
**asn_details** | [**AsnDetails**](AsnDetails.md) |  | [optional] 
**server** | **str** | Target server, including port. | [optional] [readonly] 
**source_ip** | **str** | IP address of source endpoint agent. | [optional] [readonly] 
**source_prefix** | **str** | IP prefix of source endpoint agent. | [optional] [readonly] 
**path_traces** | [**List[EndpointPathVisRoute]**](EndpointPathVisRoute.md) | Shows iterations of path trace, with each iteration specified by a pathId. | [optional] 
**vpn_path_traces** | [**List[EndpointPathVisRoute]**](EndpointPathVisRoute.md) | Shows iterations of the VPN path trace, with each iteration specified by a pathId. | [optional] 
**application** | **str** | Which supported application to monitor, can be one of &#x60;webex&#x60;, &#x60;zoom&#x60;, &#x60;microsoft-teams&#x60;. | [optional] 
**protocol** | [**EndpointTestResultProtocol**](EndpointTestResultProtocol.md) |  | [optional] 
**tcp_probe_mode** | [**TestProbeModeResponse**](TestProbeModeResponse.md) |  | [optional] 
**udp_probe_mode** | [**UdpProbeModeResponse**](UdpProbeModeResponse.md) |  | [optional] 
**webex** | [**DynamicEndpointTestWebex**](DynamicEndpointTestWebex.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_test_results.models.path_vis_detail_dynamic_endpoint_test_result import PathVisDetailDynamicEndpointTestResult

# TODO update the JSON string below
json = "{}"
# create an instance of PathVisDetailDynamicEndpointTestResult from a JSON string
path_vis_detail_dynamic_endpoint_test_result_instance = PathVisDetailDynamicEndpointTestResult.from_json(json)
# print the JSON string representation of the object
print(PathVisDetailDynamicEndpointTestResult.to_json())

# convert the object into a dict
path_vis_detail_dynamic_endpoint_test_result_dict = path_vis_detail_dynamic_endpoint_test_result_instance.to_dict()
# create an instance of PathVisDetailDynamicEndpointTestResult from a dict
path_vis_detail_dynamic_endpoint_test_result_from_dict = PathVisDetailDynamicEndpointTestResult.from_dict(path_vis_detail_dynamic_endpoint_test_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


