# ApiAgentLocation

Location of the agent.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**latitude** | **float** | Latitude of the agent. | [optional] 
**longitude** | **float** | Longitude of the agent. | [optional] 
**location_name** | **str** | Name of the agent location. | [optional] 

## Example

```python
from thousandeyes_sdk.dashboards.models.api_agent_location import ApiAgentLocation

# TODO update the JSON string below
json = "{}"
# create an instance of ApiAgentLocation from a JSON string
api_agent_location_instance = ApiAgentLocation.from_json(json)
# print the JSON string representation of the object
print(ApiAgentLocation.to_json())

# convert the object into a dict
api_agent_location_dict = api_agent_location_instance.to_dict()
# create an instance of ApiAgentLocation from a dict
api_agent_location_from_dict = ApiAgentLocation.from_dict(api_agent_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


