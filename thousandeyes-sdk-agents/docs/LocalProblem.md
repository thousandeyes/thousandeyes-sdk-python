# LocalProblem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent** | [**LocalProblemAgent**](LocalProblemAgent.md) |  | 
**start_date** | **datetime** | Date and time when the local problem interval started, in UTC. | [readonly] 
**end_date** | **datetime** | Date and time when the local problem interval ended, in UTC. This value is &#x60;null&#x60; when the local problem is active. | [optional] [readonly] 
**duration** | **int** | Duration of the local problem interval in seconds. | [readonly] 
**active** | **bool** | Indicates whether the local problem is active. | [readonly] 

## Example

```python
from thousandeyes_sdk.agents.models.local_problem import LocalProblem

# TODO update the JSON string below
json = "{}"
# create an instance of LocalProblem from a JSON string
local_problem_instance = LocalProblem.from_json(json)
# print the JSON string representation of the object
print(LocalProblem.to_json())

# convert the object into a dict
local_problem_dict = local_problem_instance.to_dict()
# create an instance of LocalProblem from a dict
local_problem_from_dict = LocalProblem.from_dict(local_problem_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


