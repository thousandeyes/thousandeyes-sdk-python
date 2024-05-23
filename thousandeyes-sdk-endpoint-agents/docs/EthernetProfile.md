# EthernetProfile

Information about the ethernet connectivity of this device. Only present if the hardware type is `ethernet`. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link_speed** | **int** | Link speed in Mbps. | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_agents.models.ethernet_profile import EthernetProfile

# TODO update the JSON string below
json = "{}"
# create an instance of EthernetProfile from a JSON string
ethernet_profile_instance = EthernetProfile.from_json(json)
# print the JSON string representation of the object
print(EthernetProfile.to_json())

# convert the object into a dict
ethernet_profile_dict = ethernet_profile_instance.to_dict()
# create an instance of EthernetProfile from a dict
ethernet_profile_from_dict = EthernetProfile.from_dict(ethernet_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


