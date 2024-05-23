# EndpointVpnProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interface_name** | **str** | Interface name associated with &#x60;interfaceProfile&#x60;. | [optional] 
**vpn_type** | [**VpnType**](VpnType.md) |  | [optional] 
**vpn_gateway_address** | **str** | IP address of the VPN gateway. | [optional] 
**vpn_client_addresses** | **List[str]** | List of private IP addresses assigned to the device, by the VPN server. | 
**vpn_client_network_range** | **List[str]** | List of private networks assigned to the device, by the VPN server. | 

## Example

```python
from thousandeyes_sdk.endpoint_agents.models.endpoint_vpn_profile import EndpointVpnProfile

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointVpnProfile from a JSON string
endpoint_vpn_profile_instance = EndpointVpnProfile.from_json(json)
# print the JSON string representation of the object
print(EndpointVpnProfile.to_json())

# convert the object into a dict
endpoint_vpn_profile_dict = endpoint_vpn_profile_instance.to_dict()
# create an instance of EndpointVpnProfile from a dict
endpoint_vpn_profile_from_dict = EndpointVpnProfile.from_dict(endpoint_vpn_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


