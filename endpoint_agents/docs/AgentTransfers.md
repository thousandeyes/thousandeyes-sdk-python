# AgentTransfers


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transfers** | [**List[AgentTransfer]**](AgentTransfer.md) |  | [optional] 

## Example

```python
from endpoint_agents.models.agent_transfers import AgentTransfers

# TODO update the JSON string below
json = "{}"
# create an instance of AgentTransfers from a JSON string
agent_transfers_instance = AgentTransfers.from_json(json)
# print the JSON string representation of the object
print(AgentTransfers.to_json())

# convert the object into a dict
agent_transfers_dict = agent_transfers_instance.to_dict()
# create an instance of AgentTransfers from a dict
agent_transfers_from_dict = AgentTransfers.from_dict(agent_transfers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


