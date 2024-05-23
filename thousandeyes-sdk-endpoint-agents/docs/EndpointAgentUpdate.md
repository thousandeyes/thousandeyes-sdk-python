# EndpointAgentUpdate

The `EndpointAgentUpdate` object contains supported fields for updates.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | New agent name. | [optional] 
**license_type** | [**AgentLicenseType**](AgentLicenseType.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_agents.models.endpoint_agent_update import EndpointAgentUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointAgentUpdate from a JSON string
endpoint_agent_update_instance = EndpointAgentUpdate.from_json(json)
# print the JSON string representation of the object
print(EndpointAgentUpdate.to_json())

# convert the object into a dict
endpoint_agent_update_dict = endpoint_agent_update_instance.to_dict()
# create an instance of EndpointAgentUpdate from a dict
endpoint_agent_update_from_dict = EndpointAgentUpdate.from_dict(endpoint_agent_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


