# EndpointAgentBulkTransfer207Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[EndpointAgentBulkTransfer207ResponseItemsInner]**](EndpointAgentBulkTransfer207ResponseItemsInner.md) |  | [optional] 

## Example

```python
from agents_api.models.endpoint_agent_bulk_transfer207_response import EndpointAgentBulkTransfer207Response

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointAgentBulkTransfer207Response from a JSON string
endpoint_agent_bulk_transfer207_response_instance = EndpointAgentBulkTransfer207Response.from_json(json)
# print the JSON string representation of the object
print EndpointAgentBulkTransfer207Response.to_json()

# convert the object into a dict
endpoint_agent_bulk_transfer207_response_dict = endpoint_agent_bulk_transfer207_response_instance.to_dict()
# create an instance of EndpointAgentBulkTransfer207Response from a dict
endpoint_agent_bulk_transfer207_response_form_dict = endpoint_agent_bulk_transfer207_response.from_dict(endpoint_agent_bulk_transfer207_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


