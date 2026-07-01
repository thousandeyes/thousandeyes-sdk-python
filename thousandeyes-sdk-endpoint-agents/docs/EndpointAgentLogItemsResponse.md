# EndpointAgentLogItemsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**logs** | [**List[EndpointAgentLogItem]**](EndpointAgentLogItem.md) | Log items for the endpoint agent. | 
**links** | [**PaginationNextAndSelfLink**](PaginationNextAndSelfLink.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_agents.models.endpoint_agent_log_items_response import EndpointAgentLogItemsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointAgentLogItemsResponse from a JSON string
endpoint_agent_log_items_response_instance = EndpointAgentLogItemsResponse.from_json(json)
# print the JSON string representation of the object
print(EndpointAgentLogItemsResponse.to_json())

# convert the object into a dict
endpoint_agent_log_items_response_dict = endpoint_agent_log_items_response_instance.to_dict()
# create an instance of EndpointAgentLogItemsResponse from a dict
endpoint_agent_log_items_response_from_dict = EndpointAgentLogItemsResponse.from_dict(endpoint_agent_log_items_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


