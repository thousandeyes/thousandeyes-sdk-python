# EventApiAffectedAgent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_id** | **str** | The ID of the virtual agent. | [optional] [readonly] 
**type** | [**CloudEnterpriseAgentType**](CloudEnterpriseAgentType.md) |  | [optional] 
**name** | **str** | The name of the agent as defined in settings. | [optional] [readonly] 
**location** | **str** | The name of the agent&#39;s location. | [optional] [readonly] 
**country_code** | **str** | The country code of the agent&#39;s location . | [optional] [readonly] 
**affected_target_ids** | **List[str]** | An array of unique target IDs that contributed data points which generated the signal for the event. | [optional] 
**affected_test_ids** | **List[str]** | An array of unique agent IDs that contributed data points which generated the signal for the event. | [optional] 
**links** | [**AgentLinks**](AgentLinks.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.event_detection.models.event_api_affected_agent import EventApiAffectedAgent

# TODO update the JSON string below
json = "{}"
# create an instance of EventApiAffectedAgent from a JSON string
event_api_affected_agent_instance = EventApiAffectedAgent.from_json(json)
# print the JSON string representation of the object
print(EventApiAffectedAgent.to_json())

# convert the object into a dict
event_api_affected_agent_dict = event_api_affected_agent_instance.to_dict()
# create an instance of EventApiAffectedAgent from a dict
event_api_affected_agent_from_dict = EventApiAffectedAgent.from_dict(event_api_affected_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


