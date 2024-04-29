# GetEndpointTestsList200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tests** | [**List[EndpointTest]**](EndpointTest.md) |  | [optional] 
**links** | [**SelfLinksLinks**](SelfLinksLinks.md) |  | [optional] 

## Example

```python
from endpoint_tests.models.get_endpoint_tests_list200_response import GetEndpointTestsList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetEndpointTestsList200Response from a JSON string
get_endpoint_tests_list200_response_instance = GetEndpointTestsList200Response.from_json(json)
# print the JSON string representation of the object
print(GetEndpointTestsList200Response.to_json())

# convert the object into a dict
get_endpoint_tests_list200_response_dict = get_endpoint_tests_list200_response_instance.to_dict()
# create an instance of GetEndpointTestsList200Response from a dict
get_endpoint_tests_list200_response_from_dict = GetEndpointTestsList200Response.from_dict(get_endpoint_tests_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


