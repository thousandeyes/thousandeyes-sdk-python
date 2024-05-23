# AgentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_id** | **str** | Agent Id (get &#x60;agentId&#x60; from &#x60;/agents&#x60; endpoint) | 
**source_ip_address** | **str** | IP address from &#x60;ipAddresses&#x60; of Agent Details for interface selection (get &#x60;ipAddresses&#x60; from &#x60;/agents&#x60; endpoint) | [optional] 

## Example

```python
from thousandeyes_sdk.tests.models.agent_request import AgentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AgentRequest from a JSON string
agent_request_instance = AgentRequest.from_json(json)
# print the JSON string representation of the object
print(AgentRequest.to_json())

# convert the object into a dict
agent_request_dict = agent_request_instance.to_dict()
# create an instance of AgentRequest from a dict
agent_request_from_dict = AgentRequest.from_dict(agent_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


