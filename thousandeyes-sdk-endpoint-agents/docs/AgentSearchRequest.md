# AgentSearchRequest

Parameters for filtering a list of agents.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**search_filters** | [**AgentSearchFilters**](AgentSearchFilters.md) |  | [optional] 
**threshold_filter** | [**AgentThresholdFilters**](AgentThresholdFilters.md) |  | [optional] 
**search_sort** | [**List[AgentSearchSort]**](AgentSearchSort.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_agents.models.agent_search_request import AgentSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AgentSearchRequest from a JSON string
agent_search_request_instance = AgentSearchRequest.from_json(json)
# print the JSON string representation of the object
print(AgentSearchRequest.to_json())

# convert the object into a dict
agent_search_request_dict = agent_search_request_instance.to_dict()
# create an instance of AgentSearchRequest from a dict
agent_search_request_from_dict = AgentSearchRequest.from_dict(agent_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


