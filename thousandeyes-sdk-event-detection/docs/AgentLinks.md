# AgentLinks

A links object containing the agent link.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent** | [**Link**](Link.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.event_detection.models.agent_links import AgentLinks

# TODO update the JSON string below
json = "{}"
# create an instance of AgentLinks from a JSON string
agent_links_instance = AgentLinks.from_json(json)
# print the JSON string representation of the object
print(AgentLinks.to_json())

# convert the object into a dict
agent_links_dict = agent_links_instance.to_dict()
# create an instance of AgentLinks from a dict
agent_links_from_dict = AgentLinks.from_dict(agent_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


