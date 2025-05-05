# AgentTestsAssignRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**test_ids** | **List[str]** | List of test IDs to assign.   You can retrieve available &#x60;testIds&#x60; using the &#x60;/agents&#x60; endpoint with the &#x60;expand&#x3D;testIds&#x60; query parameter.  | [optional] 

## Example

```python
from thousandeyes_sdk.agents.models.agent_tests_assign_request import AgentTestsAssignRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AgentTestsAssignRequest from a JSON string
agent_tests_assign_request_instance = AgentTestsAssignRequest.from_json(json)
# print the JSON string representation of the object
print(AgentTestsAssignRequest.to_json())

# convert the object into a dict
agent_tests_assign_request_dict = agent_tests_assign_request_instance.to_dict()
# create an instance of AgentTestsAssignRequest from a dict
agent_tests_assign_request_from_dict = AgentTestsAssignRequest.from_dict(agent_tests_assign_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


