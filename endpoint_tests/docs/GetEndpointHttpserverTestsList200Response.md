# GetEndpointHttpserverTestsList200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tests** | [**List[EndpointHttpServerTest]**](EndpointHttpServerTest.md) |  | [optional] 
**links** | [**SelfLinksLinks**](SelfLinksLinks.md) |  | [optional] 

## Example

```python
from endpoint_tests.models.get_endpoint_httpserver_tests_list200_response import GetEndpointHttpserverTestsList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetEndpointHttpserverTestsList200Response from a JSON string
get_endpoint_httpserver_tests_list200_response_instance = GetEndpointHttpserverTestsList200Response.from_json(json)
# print the JSON string representation of the object
print(GetEndpointHttpserverTestsList200Response.to_json())

# convert the object into a dict
get_endpoint_httpserver_tests_list200_response_dict = get_endpoint_httpserver_tests_list200_response_instance.to_dict()
# create an instance of GetEndpointHttpserverTestsList200Response from a dict
get_endpoint_httpserver_tests_list200_response_from_dict = GetEndpointHttpserverTestsList200Response.from_dict(get_endpoint_httpserver_tests_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


