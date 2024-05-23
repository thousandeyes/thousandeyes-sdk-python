# EndpointAgentLocation

Approximate location of the agent.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**latitude** | **float** |  | [optional] [readonly] 
**longitude** | **float** |  | [optional] [readonly] 
**location_name** | **str** |  | [optional] [readonly] 

## Example

```python
from thousandeyes_sdk.endpoint_agents.models.endpoint_agent_location import EndpointAgentLocation

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointAgentLocation from a JSON string
endpoint_agent_location_instance = EndpointAgentLocation.from_json(json)
# print the JSON string representation of the object
print(EndpointAgentLocation.to_json())

# convert the object into a dict
endpoint_agent_location_dict = endpoint_agent_location_instance.to_dict()
# create an instance of EndpointAgentLocation from a dict
endpoint_agent_location_from_dict = EndpointAgentLocation.from_dict(endpoint_agent_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


