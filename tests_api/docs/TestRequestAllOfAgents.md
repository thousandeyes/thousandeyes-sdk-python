# TestRequestAllOfAgents


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_id** | **str** | Agent Id (get &#x60;agentId&#x60; from &#x60;/agents&#x60; endpoint) | [optional] 
**source_ip_address** | **str** | IP address from &#x60;ipAddresses&#x60; of Agent Details for interface selection (get &#x60;ipAddresses&#x60; from &#x60;/agents&#x60; endpoint) | [optional] 

## Example

```python
from tests_api.models.test_request_all_of_agents import TestRequestAllOfAgents

# TODO update the JSON string below
json = "{}"
# create an instance of TestRequestAllOfAgents from a JSON string
test_request_all_of_agents_instance = TestRequestAllOfAgents.from_json(json)
# print the JSON string representation of the object
print TestRequestAllOfAgents.to_json()

# convert the object into a dict
test_request_all_of_agents_dict = test_request_all_of_agents_instance.to_dict()
# create an instance of TestRequestAllOfAgents from a dict
test_request_all_of_agents_form_dict = test_request_all_of_agents.from_dict(test_request_all_of_agents_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


