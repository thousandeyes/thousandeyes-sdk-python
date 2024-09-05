# EndpointAgentEthernetProfile

Information about the ethernet connectivity of this device. Only present if the hardware type is `ethernet`. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link_speed** | **int** | Link speed in Mbps. | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_agents.models.endpoint_agent_ethernet_profile import EndpointAgentEthernetProfile

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointAgentEthernetProfile from a JSON string
endpoint_agent_ethernet_profile_instance = EndpointAgentEthernetProfile.from_json(json)
# print the JSON string representation of the object
print(EndpointAgentEthernetProfile.to_json())

# convert the object into a dict
endpoint_agent_ethernet_profile_dict = endpoint_agent_ethernet_profile_instance.to_dict()
# create an instance of EndpointAgentEthernetProfile from a dict
endpoint_agent_ethernet_profile_from_dict = EndpointAgentEthernetProfile.from_dict(endpoint_agent_ethernet_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


