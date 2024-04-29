# GetLabels200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**labels** | [**List[Label]**](Label.md) |  | [optional] 
**links** | [**SelfLinksLinks**](SelfLinksLinks.md) |  | [optional] 

## Example

```python
from labels.models.get_labels200_response import GetLabels200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetLabels200Response from a JSON string
get_labels200_response_instance = GetLabels200Response.from_json(json)
# print the JSON string representation of the object
print(GetLabels200Response.to_json())

# convert the object into a dict
get_labels200_response_dict = get_labels200_response_instance.to_dict()
# create an instance of GetLabels200Response from a dict
get_labels200_response_from_dict = GetLabels200Response.from_dict(get_labels200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

