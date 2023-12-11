# EndpointAgentUpdate

The `EndpointAgentUpdate` object contains supported fields for updates.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | New agent name. | [optional] [readonly] 
**license_type** | [**List[AgentLicenseType]**](AgentLicenseType.md) | New license type. | [optional] [readonly] 

## Example

```python
from agents_api.models.endpoint_agent_update import EndpointAgentUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointAgentUpdate from a JSON string
endpoint_agent_update_instance = EndpointAgentUpdate.from_json(json)
# print the JSON string representation of the object
print EndpointAgentUpdate.to_json()

# convert the object into a dict
endpoint_agent_update_dict = endpoint_agent_update_instance.to_dict()
# create an instance of EndpointAgentUpdate from a dict
endpoint_agent_update_form_dict = endpoint_agent_update.from_dict(endpoint_agent_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


