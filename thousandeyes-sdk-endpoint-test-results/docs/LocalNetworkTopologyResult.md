# LocalNetworkTopologyResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_id** | **str** | Unique ID of endpoint agent, from &#x60;/endpoint/agents&#x60; endpoint. | [optional] [readonly] 
**var_date** | **datetime** | UTC date when endpoint network topology took place (ISO date-time format). | [optional] [readonly] 
**network_topology_id** | **str** | Network topology ID. Each network topology occurrence has a unique ID. | [optional] [readonly] 
**round_id** | **int** | Epoch time (seconds) indicating the start time of the round. | [optional] [readonly] 
**target** | **str** | IP of the target the network topology was performed against. This is typically a default gateway, proxy or VPN endpoint. | [optional] [readonly] 
**target_port** | **int** | Port of the target the network topology was performed against. | [optional] [readonly] 
**type** | [**NetworkTopologyType**](NetworkTopologyType.md) |  | [optional] 
**icmp_ping** | [**NetworkPing**](NetworkPing.md) |  | [optional] 
**is_icmp_blocked** | **bool** | Set to &#x60;true&#x60; if network target is blocking ICMP echo (ping) queries. | [optional] [readonly] 
**tcp_connect** | [**TcpConnect**](TcpConnect.md) |  | [optional] 
**system_metrics** | [**SystemMetrics**](SystemMetrics.md) |  | [optional] 
**system_metric_details** | [**SystemMetricDetails**](SystemMetricDetails.md) |  | [optional] 
**coordinates** | [**RealUserEndpointTestCoordinates**](RealUserEndpointTestCoordinates.md) |  | [optional] 
**network_profile** | [**NetworkProfile**](NetworkProfile.md) |  | [optional] 
**icmp_traceroute** | [**Traceroute**](Traceroute.md) |  | [optional] 
**icmp_traceroutes** | [**List[Traceroute]**](Traceroute.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_test_results.models.local_network_topology_result import LocalNetworkTopologyResult

# TODO update the JSON string below
json = "{}"
# create an instance of LocalNetworkTopologyResult from a JSON string
local_network_topology_result_instance = LocalNetworkTopologyResult.from_json(json)
# print the JSON string representation of the object
print(LocalNetworkTopologyResult.to_json())

# convert the object into a dict
local_network_topology_result_dict = local_network_topology_result_instance.to_dict()
# create an instance of LocalNetworkTopologyResult from a dict
local_network_topology_result_from_dict = LocalNetworkTopologyResult.from_dict(local_network_topology_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


