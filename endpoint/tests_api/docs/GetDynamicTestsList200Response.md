# GetDynamicTestsList200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tests** | [**List[DynamicTest]**](DynamicTest.md) |  | [optional] 
**links** | [**SelfLinksLinks**](SelfLinksLinks.md) |  | [optional] 

## Example

```python
from tests_api.models.get_dynamic_tests_list200_response import GetDynamicTestsList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetDynamicTestsList200Response from a JSON string
get_dynamic_tests_list200_response_instance = GetDynamicTestsList200Response.from_json(json)
# print the JSON string representation of the object
print GetDynamicTestsList200Response.to_json()

# convert the object into a dict
get_dynamic_tests_list200_response_dict = get_dynamic_tests_list200_response_instance.to_dict()
# create an instance of GetDynamicTestsList200Response from a dict
get_dynamic_tests_list200_response_form_dict = get_dynamic_tests_list200_response.from_dict(get_dynamic_tests_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


