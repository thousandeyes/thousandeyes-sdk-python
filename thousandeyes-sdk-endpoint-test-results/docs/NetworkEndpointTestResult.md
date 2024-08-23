# NetworkEndpointTestResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aid** | **str** | A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. | [optional] 
**agent_id** | **str** | Unique ID of endpoint agent, from &#x60;/endpoint/agents&#x60; endpoint. | [optional] [readonly] 
**round_id** | **int** | Epoch time (seconds) indicating the start time of the round. | [optional] [readonly] 
**server_ip** | **str** | IP address of target server. | [optional] [readonly] 
**network_profile** | [**NetworkProfile**](NetworkProfile.md) |  | [optional] 
**system_metrics** | [**SystemMetrics**](SystemMetrics.md) |  | [optional] 
**original_target_profile** | [**TargetProfile**](TargetProfile.md) |  | [optional] 
**vpn_profile** | [**VpnProfile**](VpnProfile.md) |  | [optional] 
**avg_latency** | **float** | Average RTT for packets sent to destination. | [optional] [readonly] 
**error_details** | **str** | Error details, if an error was encountered. | [optional] [readonly] 
**jitter** | **float** | Standard deviation of latency. | [optional] [readonly] 
**is_icmp_blocked** | **bool** | Set to &#x60;true&#x60; if network target is blocking ICMP echo (ping) queries. | [optional] [readonly] 
**loss** | **float** | Percentage of packets not reaching destination. | [optional] [readonly] 
**max_latency** | **float** | Maximum RTT for packets sent to destination. | [optional] [readonly] 
**min_latency** | **float** | Minimum RTT for packets sent to destination. | [optional] [readonly] 

## Example

```python
from thousandeyes_sdk.endpoint_test_results.models.network_endpoint_test_result import NetworkEndpointTestResult

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkEndpointTestResult from a JSON string
network_endpoint_test_result_instance = NetworkEndpointTestResult.from_json(json)
# print the JSON string representation of the object
print(NetworkEndpointTestResult.to_json())

# convert the object into a dict
network_endpoint_test_result_dict = network_endpoint_test_result_instance.to_dict()
# create an instance of NetworkEndpointTestResult from a dict
network_endpoint_test_result_from_dict = NetworkEndpointTestResult.from_dict(network_endpoint_test_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

