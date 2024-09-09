# InterfaceProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interface_name** | **str** |  | [optional] 
**address_profiles** | [**List[AddressProfile]**](AddressProfile.md) |  | [optional] 
**hardware_type** | [**InterfaceHardwareType**](InterfaceHardwareType.md) |  | [optional] 
**ethernet_profile** | [**EndpointAgentEthernetProfile**](EndpointAgentEthernetProfile.md) |  | [optional] 
**wireless_profile** | [**WirelessProfile**](WirelessProfile.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_agents.models.interface_profile import InterfaceProfile

# TODO update the JSON string below
json = "{}"
# create an instance of InterfaceProfile from a JSON string
interface_profile_instance = InterfaceProfile.from_json(json)
# print the JSON string representation of the object
print(InterfaceProfile.to_json())

# convert the object into a dict
interface_profile_dict = interface_profile_instance.to_dict()
# create an instance of InterfaceProfile from a dict
interface_profile_from_dict = InterfaceProfile.from_dict(interface_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


