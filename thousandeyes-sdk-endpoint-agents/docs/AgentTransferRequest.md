# AgentTransferRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**to_aid** | **str** | A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_agents.models.agent_transfer_request import AgentTransferRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AgentTransferRequest from a JSON string
agent_transfer_request_instance = AgentTransferRequest.from_json(json)
# print the JSON string representation of the object
print(AgentTransferRequest.to_json())

# convert the object into a dict
agent_transfer_request_dict = agent_transfer_request_instance.to_dict()
# create an instance of AgentTransferRequest from a dict
agent_transfer_request_from_dict = AgentTransferRequest.from_dict(agent_transfer_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


