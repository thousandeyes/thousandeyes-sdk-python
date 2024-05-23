# BulkAgentTransferRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transfers** | [**List[AgentTransfer]**](AgentTransfer.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_agents.models.bulk_agent_transfer_request import BulkAgentTransferRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BulkAgentTransferRequest from a JSON string
bulk_agent_transfer_request_instance = BulkAgentTransferRequest.from_json(json)
# print the JSON string representation of the object
print(BulkAgentTransferRequest.to_json())

# convert the object into a dict
bulk_agent_transfer_request_dict = bulk_agent_transfer_request_instance.to_dict()
# create an instance of BulkAgentTransferRequest from a dict
bulk_agent_transfer_request_from_dict = BulkAgentTransferRequest.from_dict(bulk_agent_transfer_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


