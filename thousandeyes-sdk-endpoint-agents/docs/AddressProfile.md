# AddressProfile

A description of the IPs assigned to this machine.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_type** | [**AddressType**](AddressType.md) |  | [optional] 
**ip_address** | **str** | IP address of this interface in the network it&#39;s currently connected to. | [optional] 
**prefix_length** | **int** | The number of bits representing the network part of the &#x60;ipAddress&#x60;. | [optional] 
**gateway** | **str** | The default gateway for this interface. | [optional] 
**router_hardware_address** | **str** | The router&#39;s MAC address resolved from an ARP request. | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_agents.models.address_profile import AddressProfile

# TODO update the JSON string below
json = "{}"
# create an instance of AddressProfile from a JSON string
address_profile_instance = AddressProfile.from_json(json)
# print the JSON string representation of the object
print(AddressProfile.to_json())

# convert the object into a dict
address_profile_dict = address_profile_instance.to_dict()
# create an instance of AddressProfile from a dict
address_profile_from_dict = AddressProfile.from_dict(address_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


