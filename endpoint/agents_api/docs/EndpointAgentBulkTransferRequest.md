# EndpointAgentBulkTransferRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transfers** | [**List[AgentTransfer]**](AgentTransfer.md) |  | [optional] 

## Example

```python
from agents_api.models.endpoint_agent_bulk_transfer_request import EndpointAgentBulkTransferRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointAgentBulkTransferRequest from a JSON string
endpoint_agent_bulk_transfer_request_instance = EndpointAgentBulkTransferRequest.from_json(json)
# print the JSON string representation of the object
print EndpointAgentBulkTransferRequest.to_json()

# convert the object into a dict
endpoint_agent_bulk_transfer_request_dict = endpoint_agent_bulk_transfer_request_instance.to_dict()
# create an instance of EndpointAgentBulkTransferRequest from a dict
endpoint_agent_bulk_transfer_request_form_dict = endpoint_agent_bulk_transfer_request.from_dict(endpoint_agent_bulk_transfer_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


