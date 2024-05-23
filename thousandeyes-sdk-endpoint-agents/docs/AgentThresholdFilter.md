# AgentThresholdFilter

The metric is filtered based on the threshold value and operator provided.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**value** | **float** | The threshold value. | [optional] 
**operator** | [**ThresholdFilterOperator**](ThresholdFilterOperator.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_agents.models.agent_threshold_filter import AgentThresholdFilter

# TODO update the JSON string below
json = "{}"
# create an instance of AgentThresholdFilter from a JSON string
agent_threshold_filter_instance = AgentThresholdFilter.from_json(json)
# print the JSON string representation of the object
print(AgentThresholdFilter.to_json())

# convert the object into a dict
agent_threshold_filter_dict = agent_threshold_filter_instance.to_dict()
# create an instance of AgentThresholdFilter from a dict
agent_threshold_filter_from_dict = AgentThresholdFilter.from_dict(agent_threshold_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


