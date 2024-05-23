# NetworkInterface


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

## Example

```python
from thousandeyes_sdk.endpoint_test_results.models.network_interface import NetworkInterface

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkInterface from a JSON string
network_interface_instance = NetworkInterface.from_json(json)
# print the JSON string representation of the object
print(NetworkInterface.to_json())

# convert the object into a dict
network_interface_dict = network_interface_instance.to_dict()
# create an instance of NetworkInterface from a dict
network_interface_from_dict = NetworkInterface.from_dict(network_interface_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


