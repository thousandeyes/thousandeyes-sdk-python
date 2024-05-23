# BulkAgentTransferResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[AgentTransferStatus]**](AgentTransferStatus.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_agents.models.bulk_agent_transfer_response import BulkAgentTransferResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BulkAgentTransferResponse from a JSON string
bulk_agent_transfer_response_instance = BulkAgentTransferResponse.from_json(json)
# print the JSON string representation of the object
print(BulkAgentTransferResponse.to_json())

# convert the object into a dict
bulk_agent_transfer_response_dict = bulk_agent_transfer_response_instance.to_dict()
# create an instance of BulkAgentTransferResponse from a dict
bulk_agent_transfer_response_from_dict = BulkAgentTransferResponse.from_dict(bulk_agent_transfer_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


