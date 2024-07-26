# AgentInterfaces


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip_address** | **str** | IP address of the agent interface. | [optional] 
**agent_id** | **str** | The agent ID of the enterprise agent for the test. | [optional] 

## Example

```python
from thousandeyes_sdk.instant_tests.models.agent_interfaces import AgentInterfaces

# TODO update the JSON string below
json = "{}"
# create an instance of AgentInterfaces from a JSON string
agent_interfaces_instance = AgentInterfaces.from_json(json)
# print the JSON string representation of the object
print(AgentInterfaces.to_json())

# convert the object into a dict
agent_interfaces_dict = agent_interfaces_instance.to_dict()
# create an instance of AgentInterfaces from a dict
agent_interfaces_from_dict = AgentInterfaces.from_dict(agent_interfaces_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


