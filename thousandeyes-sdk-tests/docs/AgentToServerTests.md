# AgentToServerTests


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tests** | [**List[UnexpandedAgentToServerTest]**](UnexpandedAgentToServerTest.md) |  | [optional] 
**links** | [**SelfLinks**](SelfLinks.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.tests.models.agent_to_server_tests import AgentToServerTests

# TODO update the JSON string below
json = "{}"
# create an instance of AgentToServerTests from a JSON string
agent_to_server_tests_instance = AgentToServerTests.from_json(json)
# print the JSON string representation of the object
print(AgentToServerTests.to_json())

# convert the object into a dict
agent_to_server_tests_dict = agent_to_server_tests_instance.to_dict()
# create an instance of AgentToServerTests from a dict
agent_to_server_tests_from_dict = AgentToServerTests.from_dict(agent_to_server_tests_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


