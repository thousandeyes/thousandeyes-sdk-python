# TestAgent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_id** | **str** | Identifier for the agent (get &#x60;agentId&#x60; from &#x60;/agents&#x60; endpoint). | [optional] 
**source_ip_address** | **str** | IP address from the agent&#39;s &#x60;ipAddresses&#x60; field (get &#x60;ipAddresses&#x60; from &#x60;/agents&#x60; endpoint). Used for interface selection. | [optional] 

## Example

```python
from thousandeyes_sdk.instant_tests.models.test_agent import TestAgent

# TODO update the JSON string below
json = "{}"
# create an instance of TestAgent from a JSON string
test_agent_instance = TestAgent.from_json(json)
# print the JSON string representation of the object
print(TestAgent.to_json())

# convert the object into a dict
test_agent_dict = test_agent_instance.to_dict()
# create an instance of TestAgent from a dict
test_agent_from_dict = TestAgent.from_dict(test_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


