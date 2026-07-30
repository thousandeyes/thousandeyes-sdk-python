# AgentEventGrouping


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_id** | **str** | Agent identifier (for agent events). Represents the machine ID for Endpoint Agents or the virtual agent ID for Cloud and Enterprise Agents&#39;. | [optional] [readonly] 

## Example

```python
from thousandeyes_sdk.event_detection.models.agent_event_grouping import AgentEventGrouping

# TODO update the JSON string below
json = "{}"
# create an instance of AgentEventGrouping from a JSON string
agent_event_grouping_instance = AgentEventGrouping.from_json(json)
# print the JSON string representation of the object
print(AgentEventGrouping.to_json())

# convert the object into a dict
agent_event_grouping_dict = agent_event_grouping_instance.to_dict()
# create an instance of AgentEventGrouping from a dict
agent_event_grouping_from_dict = AgentEventGrouping.from_dict(agent_event_grouping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


