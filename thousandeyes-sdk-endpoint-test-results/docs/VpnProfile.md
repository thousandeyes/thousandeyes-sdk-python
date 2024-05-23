# VpnProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vpn_client_addresses** | **List[str]** | A list of private IP addresses assigned to the device by the VPN server. | [optional] [readonly] 
**vpn_client_network_range** | **List[str]** | A list of private networks assigned to the device by the VPN server. | [optional] [readonly] 
**vpn_gateway_address** | **str** | IP address of the VPN gateway. | [optional] [readonly] 
**vpn_type** | [**VpnType**](VpnType.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_test_results.models.vpn_profile import VpnProfile

# TODO update the JSON string below
json = "{}"
# create an instance of VpnProfile from a JSON string
vpn_profile_instance = VpnProfile.from_json(json)
# print the JSON string representation of the object
print(VpnProfile.to_json())

# convert the object into a dict
vpn_profile_dict = vpn_profile_instance.to_dict()
# create an instance of VpnProfile from a dict
vpn_profile_from_dict = VpnProfile.from_dict(vpn_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


