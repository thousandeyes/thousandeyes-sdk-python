# AgentToAgentTests


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tests** | [**List[UnexpandedAgentToAgentTest]**](UnexpandedAgentToAgentTest.md) |  | [optional] 
**links** | [**SelfLinks**](SelfLinks.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.tests.models.agent_to_agent_tests import AgentToAgentTests

# TODO update the JSON string below
json = "{}"
# create an instance of AgentToAgentTests from a JSON string
agent_to_agent_tests_instance = AgentToAgentTests.from_json(json)
# print the JSON string representation of the object
print(AgentToAgentTests.to_json())

# convert the object into a dict
agent_to_agent_tests_dict = agent_to_agent_tests_instance.to_dict()
# create an instance of AgentToAgentTests from a dict
agent_to_agent_tests_from_dict = AgentToAgentTests.from_dict(agent_to_agent_tests_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


