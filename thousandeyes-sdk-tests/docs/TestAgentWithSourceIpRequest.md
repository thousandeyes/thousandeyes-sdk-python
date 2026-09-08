# TestAgentWithSourceIpRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_id** | **str** | The agent ID. Get &#x60;agentId&#x60; from &#x60;/agents&#x60; endpoint. | 
**source_ip_address** | **str** | The Enterprise Agent interface IP address to use as the source for the test. The address must be listed in the agent&#39;s &#x60;ipAddresses&#x60; field, available from the &#x60;/agents&#x60; endpoint. It is not supported for Cloud Agents or Enterprise Agent clusters. | [optional] 

## Example

```python
from thousandeyes_sdk.tests.models.test_agent_with_source_ip_request import TestAgentWithSourceIpRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TestAgentWithSourceIpRequest from a JSON string
test_agent_with_source_ip_request_instance = TestAgentWithSourceIpRequest.from_json(json)
# print the JSON string representation of the object
print(TestAgentWithSourceIpRequest.to_json())

# convert the object into a dict
test_agent_with_source_ip_request_dict = test_agent_with_source_ip_request_instance.to_dict()
# create an instance of TestAgentWithSourceIpRequest from a dict
test_agent_with_source_ip_request_from_dict = TestAgentWithSourceIpRequest.from_dict(test_agent_with_source_ip_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


