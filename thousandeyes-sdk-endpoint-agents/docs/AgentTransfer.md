# AgentTransfer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_id** | **str** | Unique ID of endpoint agent, from &#x60;/endpoint/agents&#x60; endpoint. | [optional] [readonly] 
**from_aid** | **str** | A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. | [optional] 
**to_aid** | **str** | A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_agents.models.agent_transfer import AgentTransfer

# TODO update the JSON string below
json = "{}"
# create an instance of AgentTransfer from a JSON string
agent_transfer_instance = AgentTransfer.from_json(json)
# print the JSON string representation of the object
print(AgentTransfer.to_json())

# convert the object into a dict
agent_transfer_dict = agent_transfer_instance.to_dict()
# create an instance of AgentTransfer from a dict
agent_transfer_from_dict = AgentTransfer.from_dict(agent_transfer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


