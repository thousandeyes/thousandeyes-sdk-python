# AgentLocalEventGrouping


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_id** | **str** | Numeric Agent ID (for agent-local events). | [optional] [readonly] 

## Example

```python
from thousandeyes_sdk.event_detection.models.agent_local_event_grouping import AgentLocalEventGrouping

# TODO update the JSON string below
json = "{}"
# create an instance of AgentLocalEventGrouping from a JSON string
agent_local_event_grouping_instance = AgentLocalEventGrouping.from_json(json)
# print the JSON string representation of the object
print(AgentLocalEventGrouping.to_json())

# convert the object into a dict
agent_local_event_grouping_dict = agent_local_event_grouping_instance.to_dict()
# create an instance of AgentLocalEventGrouping from a dict
agent_local_event_grouping_from_dict = AgentLocalEventGrouping.from_dict(agent_local_event_grouping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


