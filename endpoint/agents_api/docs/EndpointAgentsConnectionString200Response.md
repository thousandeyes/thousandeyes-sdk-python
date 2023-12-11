# EndpointAgentsConnectionString200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**SelfLinksLinks**](SelfLinksLinks.md) |  | [optional] 
**connection_string** | **str** | The connection string is used for some integrations and other client types.  | [optional] 

## Example

```python
from agents_api.models.endpoint_agents_connection_string200_response import EndpointAgentsConnectionString200Response

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointAgentsConnectionString200Response from a JSON string
endpoint_agents_connection_string200_response_instance = EndpointAgentsConnectionString200Response.from_json(json)
# print the JSON string representation of the object
print EndpointAgentsConnectionString200Response.to_json()

# convert the object into a dict
endpoint_agents_connection_string200_response_dict = endpoint_agents_connection_string200_response_instance.to_dict()
# create an instance of EndpointAgentsConnectionString200Response from a dict
endpoint_agents_connection_string200_response_form_dict = endpoint_agents_connection_string200_response.from_dict(endpoint_agents_connection_string200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


