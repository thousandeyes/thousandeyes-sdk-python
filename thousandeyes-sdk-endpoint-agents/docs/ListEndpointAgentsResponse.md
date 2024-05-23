# ListEndpointAgentsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_agents** | **int** | The total number of agents. | [optional] 
**agents** | [**List[EndpointAgent]**](EndpointAgent.md) |  | [optional] 
**links** | [**PaginationNextAndSelfLink**](PaginationNextAndSelfLink.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_agents.models.list_endpoint_agents_response import ListEndpointAgentsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListEndpointAgentsResponse from a JSON string
list_endpoint_agents_response_instance = ListEndpointAgentsResponse.from_json(json)
# print the JSON string representation of the object
print(ListEndpointAgentsResponse.to_json())

# convert the object into a dict
list_endpoint_agents_response_dict = list_endpoint_agents_response_instance.to_dict()
# create an instance of ListEndpointAgentsResponse from a dict
list_endpoint_agents_response_from_dict = ListEndpointAgentsResponse.from_dict(list_endpoint_agents_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


