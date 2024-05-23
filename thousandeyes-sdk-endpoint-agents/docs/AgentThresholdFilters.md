# AgentThresholdFilters

All filters are applied based on the conditional operator (and/or).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | [**List[AgentThresholdFilter]**](AgentThresholdFilter.md) |  | [optional] 
**conditional_operator** | [**ConditionalOperator**](ConditionalOperator.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_agents.models.agent_threshold_filters import AgentThresholdFilters

# TODO update the JSON string below
json = "{}"
# create an instance of AgentThresholdFilters from a JSON string
agent_threshold_filters_instance = AgentThresholdFilters.from_json(json)
# print the JSON string representation of the object
print(AgentThresholdFilters.to_json())

# convert the object into a dict
agent_threshold_filters_dict = agent_threshold_filters_instance.to_dict()
# create an instance of AgentThresholdFilters from a dict
agent_threshold_filters_from_dict = AgentThresholdFilters.from_dict(agent_threshold_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


