# AgentSearchSort


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sort** | [**AgentSearchSortKey**](AgentSearchSortKey.md) |  | [optional] 
**order** | [**SortOrder**](SortOrder.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_agents.models.agent_search_sort import AgentSearchSort

# TODO update the JSON string below
json = "{}"
# create an instance of AgentSearchSort from a JSON string
agent_search_sort_instance = AgentSearchSort.from_json(json)
# print the JSON string representation of the object
print(AgentSearchSort.to_json())

# convert the object into a dict
agent_search_sort_dict = agent_search_sort_instance.to_dict()
# create an instance of AgentSearchSort from a dict
agent_search_sort_from_dict = AgentSearchSort.from_dict(agent_search_sort_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


