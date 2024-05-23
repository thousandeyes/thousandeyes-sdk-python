# Agent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_id** | **str** | Unique agent ID | [optional] [readonly] 
**agent_name** | **str** | Agent name | [optional] [readonly] 
**country_id** | **str** | 2-digit ISO country code | [optional] [readonly] 
**location** | **str** | Location of the agent. | [optional] [readonly] 

## Example

```python
from thousandeyes_sdk.test_results.models.agent import Agent

# TODO update the JSON string below
json = "{}"
# create an instance of Agent from a JSON string
agent_instance = Agent.from_json(json)
# print the JSON string representation of the object
print(Agent.to_json())

# convert the object into a dict
agent_dict = agent_instance.to_dict()
# create an instance of Agent from a dict
agent_from_dict = Agent.from_dict(agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


