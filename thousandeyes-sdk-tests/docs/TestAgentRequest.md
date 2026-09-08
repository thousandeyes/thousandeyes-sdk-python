# TestAgentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_id** | **str** | The agent ID. Get &#x60;agentId&#x60; from &#x60;/agents&#x60; endpoint. | 

## Example

```python
from thousandeyes_sdk.tests.models.test_agent_request import TestAgentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TestAgentRequest from a JSON string
test_agent_request_instance = TestAgentRequest.from_json(json)
# print the JSON string representation of the object
print(TestAgentRequest.to_json())

# convert the object into a dict
test_agent_request_dict = test_agent_request_instance.to_dict()
# create an instance of TestAgentRequest from a dict
test_agent_request_from_dict = TestAgentRequest.from_dict(test_agent_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


