# RealUserTestNetworkVpnTraceroute


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination** | **str** | The target IP address. | [optional] [readonly] 
**error** | **str** | Only present when there is an error | [optional] [readonly] 
**info_flags** | **List[str]** |  | [optional] [readonly] 
**internal_errors** | **List[str]** |  | [optional] [readonly] 
**hops** | [**List[TracerouteHop]**](TracerouteHop.md) |  | [optional] 

## Example

```python
from endpoint_test_results.models.real_user_test_network_vpn_traceroute import RealUserTestNetworkVpnTraceroute

# TODO update the JSON string below
json = "{}"
# create an instance of RealUserTestNetworkVpnTraceroute from a JSON string
real_user_test_network_vpn_traceroute_instance = RealUserTestNetworkVpnTraceroute.from_json(json)
# print the JSON string representation of the object
print(RealUserTestNetworkVpnTraceroute.to_json())

# convert the object into a dict
real_user_test_network_vpn_traceroute_dict = real_user_test_network_vpn_traceroute_instance.to_dict()
# create an instance of RealUserTestNetworkVpnTraceroute from a dict
real_user_test_network_vpn_traceroute_from_dict = RealUserTestNetworkVpnTraceroute.from_dict(real_user_test_network_vpn_traceroute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


