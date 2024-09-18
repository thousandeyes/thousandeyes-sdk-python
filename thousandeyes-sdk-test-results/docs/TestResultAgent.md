# TestResultAgent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_id** | **str** | Unique agent ID | [optional] [readonly] 
**agent_name** | **str** | Agent name | [optional] [readonly] 
**country_id** | **str** | 2-digit ISO country code | [optional] [readonly] 
**location** | **str** | Location of the agent. | [optional] [readonly] 

## Example

```python
from thousandeyes_sdk.test_results.models.test_result_agent import TestResultAgent

# TODO update the JSON string below
json = "{}"
# create an instance of TestResultAgent from a JSON string
test_result_agent_instance = TestResultAgent.from_json(json)
# print the JSON string representation of the object
print(TestResultAgent.to_json())

# convert the object into a dict
test_result_agent_dict = test_result_agent_instance.to_dict()
# create an instance of TestResultAgent from a dict
test_result_agent_from_dict = TestResultAgent.from_dict(test_result_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


