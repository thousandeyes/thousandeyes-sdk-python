# AgentLabel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label_id** | **str** | Label Id. | [optional] 
**name** | **str** | Name of the label. | [optional] 

## Example

```python
from thousandeyes_sdk.agents.models.agent_label import AgentLabel

# TODO update the JSON string below
json = "{}"
# create an instance of AgentLabel from a JSON string
agent_label_instance = AgentLabel.from_json(json)
# print the JSON string representation of the object
print(AgentLabel.to_json())

# convert the object into a dict
agent_label_dict = agent_label_instance.to_dict()
# create an instance of AgentLabel from a dict
agent_label_from_dict = AgentLabel.from_dict(agent_label_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


