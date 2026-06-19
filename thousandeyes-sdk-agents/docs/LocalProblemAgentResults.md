# LocalProblemAgentResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**local_problems** | [**List[LocalProblem]**](LocalProblem.md) |  | [optional] 
**start_date** | **datetime** | (Optional) When passing &#x60;window&#x60; or &#x60;startDate&#x60; parameter,  the client will also receive the &#x60;startDate&#x60; field indicating the UTC start date of the data&#39;s time range being retrieved  (ISO date-time format). | [optional] [readonly] 
**end_date** | **datetime** | (Optional) When passing &#x60;window&#x60; or &#x60;endDate&#x60; parameter,  the client will also receive the &#x60;endDate&#x60; field indicating the UTC end date of the data&#39;s time range being retrieved  (ISO date-time format). | [optional] [readonly] 
**links** | [**SelfLinks**](SelfLinks.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.agents.models.local_problem_agent_results import LocalProblemAgentResults

# TODO update the JSON string below
json = "{}"
# create an instance of LocalProblemAgentResults from a JSON string
local_problem_agent_results_instance = LocalProblemAgentResults.from_json(json)
# print the JSON string representation of the object
print(LocalProblemAgentResults.to_json())

# convert the object into a dict
local_problem_agent_results_dict = local_problem_agent_results_instance.to_dict()
# create an instance of LocalProblemAgentResults from a dict
local_problem_agent_results_from_dict = LocalProblemAgentResults.from_dict(local_problem_agent_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


