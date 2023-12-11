# InstantTestRequestAgentsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_id** | **str** | Identifier for the agent (get &#x60;agentId&#x60; from &#x60;/agents&#x60; endpoint). | [optional] 
**source_ip_address** | **str** | IP address from the agent&#39;s &#x60;ipAddresses&#x60; field (get &#x60;ipAddresses&#x60; from &#x60;/agents&#x60; endpoint). Used for interface selection. | [optional] 

## Example

```python
from instant_tests_api.models.instant_test_request_agents_inner import InstantTestRequestAgentsInner

# TODO update the JSON string below
json = "{}"
# create an instance of InstantTestRequestAgentsInner from a JSON string
instant_test_request_agents_inner_instance = InstantTestRequestAgentsInner.from_json(json)
# print the JSON string representation of the object
print InstantTestRequestAgentsInner.to_json()

# convert the object into a dict
instant_test_request_agents_inner_dict = instant_test_request_agents_inner_instance.to_dict()
# create an instance of InstantTestRequestAgentsInner from a dict
instant_test_request_agents_inner_form_dict = instant_test_request_agents_inner.from_dict(instant_test_request_agents_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


