# GetTests200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tests** | [**List[SimpleTest]**](SimpleTest.md) |  | [optional] 
**links** | [**SelfLinksLinks**](SelfLinksLinks.md) |  | [optional] 

## Example

```python
from tests_api.models.get_tests200_response import GetTests200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetTests200Response from a JSON string
get_tests200_response_instance = GetTests200Response.from_json(json)
# print the JSON string representation of the object
print GetTests200Response.to_json()

# convert the object into a dict
get_tests200_response_dict = get_tests200_response_instance.to_dict()
# create an instance of GetTests200Response from a dict
get_tests200_response_form_dict = get_tests200_response.from_dict(get_tests200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


