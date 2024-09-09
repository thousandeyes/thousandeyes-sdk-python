# NetworkProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip_address** | **str** | Network IP address. | [optional] [readonly] 
**subnet_mask** | **str** | Network subnet mask - only for IPv4. | [optional] [readonly] 
**public_ip_address** | **str** | Network public IP address. | [optional] [readonly] 
**local_prefix** | **str** | Network local prefix. | [optional] [readonly] 
**public_ip_range** | **str** | Network public IP range. | [optional] [readonly] 
**dns_servers** | **List[str]** | Network DNS servers. | [optional] [readonly] 
**hardware_type** | [**InterfaceHardwareType**](InterfaceHardwareType.md) |  | [optional] 
**interface_name** | **str** | Network interface name. | [optional] [readonly] 
**error** | **str** | Only present when there is an error | [optional] [readonly] 
**gateway** | **str** | Network gateway address. | [optional] [readonly] 
**wireless_profile** | [**NetworkWirelessProfile**](NetworkWirelessProfile.md) |  | [optional] 
**proxy_profile** | [**NetworkProxyProfile**](NetworkProxyProfile.md) |  | [optional] 
**ethernet_profile** | [**EndpointTestEthernetProfile**](EndpointTestEthernetProfile.md) |  | [optional] 
**previous_interface** | [**NetworkInterface**](NetworkInterface.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_test_results.models.network_profile import NetworkProfile

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkProfile from a JSON string
network_profile_instance = NetworkProfile.from_json(json)
# print the JSON string representation of the object
print(NetworkProfile.to_json())

# convert the object into a dict
network_profile_dict = network_profile_instance.to_dict()
# create an instance of NetworkProfile from a dict
network_profile_from_dict = NetworkProfile.from_dict(network_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


