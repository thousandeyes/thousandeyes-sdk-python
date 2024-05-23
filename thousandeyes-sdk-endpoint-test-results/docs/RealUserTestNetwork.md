# RealUserTestNetwork

Contains details about network profile and conditions during session.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network_profile** | [**NetworkProfile**](NetworkProfile.md) |  | [optional] 
**system_metrics** | [**SystemMetrics**](SystemMetrics.md) |  | [optional] 
**gateway_ping** | [**GatewayNetworkPing**](GatewayNetworkPing.md) |  | [optional] 
**ping** | [**TargetNetworkPing**](TargetNetworkPing.md) |  | [optional] 
**traceroute** | [**TargetTraceroute**](TargetTraceroute.md) |  | [optional] 
**connect_rtt** | **float** | Represents the number of milliseconds required to establish TCP connectivity with the target. | [optional] [readonly] 
**is_icmp_blocked** | **bool** | Set to &#x60;true&#x60; if network target is blocking ICMP echo (ping) queries. | [optional] [readonly] 
**errors** | **List[str]** | Array of string representing possible network errors. | [optional] [readonly] 
**vpn_ping** | [**VpnNetworkPing**](VpnNetworkPing.md) |  | [optional] 
**vpn_traceroute** | [**VpnTraceroute**](VpnTraceroute.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_test_results.models.real_user_test_network import RealUserTestNetwork

# TODO update the JSON string below
json = "{}"
# create an instance of RealUserTestNetwork from a JSON string
real_user_test_network_instance = RealUserTestNetwork.from_json(json)
# print the JSON string representation of the object
print(RealUserTestNetwork.to_json())

# convert the object into a dict
real_user_test_network_dict = real_user_test_network_instance.to_dict()
# create an instance of RealUserTestNetwork from a dict
real_user_test_network_from_dict = RealUserTestNetwork.from_dict(real_user_test_network_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


