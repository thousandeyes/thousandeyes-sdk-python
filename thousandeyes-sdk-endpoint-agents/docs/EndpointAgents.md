# EndpointAgents

A list of `EndpointAgents`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_agents** | **int** | The total number of agents. | [optional] 
**agents** | [**List[EndpointAgent]**](EndpointAgent.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_agents.models.endpoint_agents import EndpointAgents

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointAgents from a JSON string
endpoint_agents_instance = EndpointAgents.from_json(json)
# print the JSON string representation of the object
print(EndpointAgents.to_json())

# convert the object into a dict
endpoint_agents_dict = endpoint_agents_instance.to_dict()
# create an instance of EndpointAgents from a dict
endpoint_agents_from_dict = EndpointAgents.from_dict(endpoint_agents_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


