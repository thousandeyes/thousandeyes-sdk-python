# EndpointAgentsList200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_agents** | **int** | The total number of agents. | [optional] 
**agents** | [**List[EndpointAgentsAgentsInner]**](EndpointAgentsAgentsInner.md) |  | [optional] 
**links** | [**PaginationNextAndSelfLinkLinks**](PaginationNextAndSelfLinkLinks.md) |  | [optional] 

## Example

```python
from endpoint_agents.models.endpoint_agents_list200_response import EndpointAgentsList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointAgentsList200Response from a JSON string
endpoint_agents_list200_response_instance = EndpointAgentsList200Response.from_json(json)
# print the JSON string representation of the object
print(EndpointAgentsList200Response.to_json())

# convert the object into a dict
endpoint_agents_list200_response_dict = endpoint_agents_list200_response_instance.to_dict()
# create an instance of EndpointAgentsList200Response from a dict
endpoint_agents_list200_response_from_dict = EndpointAgentsList200Response.from_dict(endpoint_agents_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


