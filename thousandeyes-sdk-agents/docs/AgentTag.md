# AgentTag


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Tag Id. | [optional] 
**key** | **str** | Tag key, for example, \&quot;Location\&quot; or \&quot;Department\&quot;. | [optional] 
**value** | **str** | Tag value, for example, \&quot;San Francisco\&quot; or \&quot;Engineering\&quot;. | [optional] 

## Example

```python
from thousandeyes_sdk.agents.models.agent_tag import AgentTag

# TODO update the JSON string below
json = "{}"
# create an instance of AgentTag from a JSON string
agent_tag_instance = AgentTag.from_json(json)
# print the JSON string representation of the object
print(AgentTag.to_json())

# convert the object into a dict
agent_tag_dict = agent_tag_instance.to_dict()
# create an instance of AgentTag from a dict
agent_tag_from_dict = AgentTag.from_dict(agent_tag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


