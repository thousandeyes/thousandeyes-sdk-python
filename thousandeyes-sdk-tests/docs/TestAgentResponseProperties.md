# TestAgentResponseProperties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_ip_address** | **str** | IP address of the agent interface used as the source for the test. Returned when a source interface is selected. | [optional] [readonly] 

## Example

```python
from thousandeyes_sdk.tests.models.test_agent_response_properties import TestAgentResponseProperties

# TODO update the JSON string below
json = "{}"
# create an instance of TestAgentResponseProperties from a JSON string
test_agent_response_properties_instance = TestAgentResponseProperties.from_json(json)
# print the JSON string representation of the object
print(TestAgentResponseProperties.to_json())

# convert the object into a dict
test_agent_response_properties_dict = test_agent_response_properties_instance.to_dict()
# create an instance of TestAgentResponseProperties from a dict
test_agent_response_properties_from_dict = TestAgentResponseProperties.from_dict(test_agent_response_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


