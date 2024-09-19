# AffectedAgents


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** | The total number affected. | [optional] [readonly] 
**in_account_group** | **int** | Indicates if in the affected account group. | [optional] [readonly] 
**agents** | [**List[EventApiAffectedAgent]**](EventApiAffectedAgent.md) | List of affected agents. | [optional] 

## Example

```python
from thousandeyes_sdk.event_detection.models.affected_agents import AffectedAgents

# TODO update the JSON string below
json = "{}"
# create an instance of AffectedAgents from a JSON string
affected_agents_instance = AffectedAgents.from_json(json)
# print the JSON string representation of the object
print(AffectedAgents.to_json())

# convert the object into a dict
affected_agents_dict = affected_agents_instance.to_dict()
# create an instance of AffectedAgents from a dict
affected_agents_from_dict = AffectedAgents.from_dict(affected_agents_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


