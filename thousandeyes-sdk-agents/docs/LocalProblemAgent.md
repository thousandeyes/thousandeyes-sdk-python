# LocalProblemAgent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_id** | **str** | Agent ID. | [optional] [readonly] 
**agent_name** | **str** | Agent name. | [optional] [readonly] 
**country_id** | **str** | Two-letter ISO country code where the agent is located. | [optional] [readonly] 
**location** | **str** | Agent location. | [optional] [readonly] 

## Example

```python
from thousandeyes_sdk.agents.models.local_problem_agent import LocalProblemAgent

# TODO update the JSON string below
json = "{}"
# create an instance of LocalProblemAgent from a JSON string
local_problem_agent_instance = LocalProblemAgent.from_json(json)
# print the JSON string representation of the object
print(LocalProblemAgent.to_json())

# convert the object into a dict
local_problem_agent_dict = local_problem_agent_instance.to_dict()
# create an instance of LocalProblemAgent from a dict
local_problem_agent_from_dict = LocalProblemAgent.from_dict(local_problem_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


