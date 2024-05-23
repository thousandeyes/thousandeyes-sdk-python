# FilterEndpointAgentsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_agents** | **int** | The total number of agents. | [optional] 
**agents** | [**List[EndpointAgent]**](EndpointAgent.md) |  | [optional] 
**links** | [**PaginationNextLink**](PaginationNextLink.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_agents.models.filter_endpoint_agents_response import FilterEndpointAgentsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FilterEndpointAgentsResponse from a JSON string
filter_endpoint_agents_response_instance = FilterEndpointAgentsResponse.from_json(json)
# print the JSON string representation of the object
print(FilterEndpointAgentsResponse.to_json())

# convert the object into a dict
filter_endpoint_agents_response_dict = filter_endpoint_agents_response_instance.to_dict()
# create an instance of FilterEndpointAgentsResponse from a dict
filter_endpoint_agents_response_from_dict = FilterEndpointAgentsResponse.from_dict(filter_endpoint_agents_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


