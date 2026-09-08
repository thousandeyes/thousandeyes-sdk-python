# TestAgentWithSourceIpAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_id** | **str** | Identifier for the agent (get &#x60;agentId&#x60; from &#x60;/agents&#x60; endpoint). | [optional] 
**source_ip_address** | **str** | The Enterprise Agent interface IP address to use as the source for the test. The address must be listed in the agent&#39;s &#x60;ipAddresses&#x60; field, available from the &#x60;/agents&#x60; endpoint. It is not supported for Cloud Agents or Enterprise Agent clusters. | [optional] 

## Example

```python
from thousandeyes_sdk.instant_tests.models.test_agent_with_source_ip_address import TestAgentWithSourceIpAddress

# TODO update the JSON string below
json = "{}"
# create an instance of TestAgentWithSourceIpAddress from a JSON string
test_agent_with_source_ip_address_instance = TestAgentWithSourceIpAddress.from_json(json)
# print the JSON string representation of the object
print(TestAgentWithSourceIpAddress.to_json())

# convert the object into a dict
test_agent_with_source_ip_address_dict = test_agent_with_source_ip_address_instance.to_dict()
# create an instance of TestAgentWithSourceIpAddress from a dict
test_agent_with_source_ip_address_from_dict = TestAgentWithSourceIpAddress.from_dict(test_agent_with_source_ip_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


