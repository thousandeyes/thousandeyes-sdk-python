# GetEndpointAgentToserverTestsList200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tests** | [**List[EndpointAgentToServerTest]**](EndpointAgentToServerTest.md) |  | [optional] 
**links** | [**SelfLinksLinks**](SelfLinksLinks.md) |  | [optional] 

## Example

```python
from endpoint_tests.models.get_endpoint_agent_toserver_tests_list200_response import GetEndpointAgentToserverTestsList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetEndpointAgentToserverTestsList200Response from a JSON string
get_endpoint_agent_toserver_tests_list200_response_instance = GetEndpointAgentToserverTestsList200Response.from_json(json)
# print the JSON string representation of the object
print(GetEndpointAgentToserverTestsList200Response.to_json())

# convert the object into a dict
get_endpoint_agent_toserver_tests_list200_response_dict = get_endpoint_agent_toserver_tests_list200_response_instance.to_dict()
# create an instance of GetEndpointAgentToserverTestsList200Response from a dict
get_endpoint_agent_toserver_tests_list200_response_from_dict = GetEndpointAgentToserverTestsList200Response.from_dict(get_endpoint_agent_toserver_tests_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

