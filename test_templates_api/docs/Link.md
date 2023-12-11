# Link


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**hreflang** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**deprecation** | **str** |  | [optional] 
**profile** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**templated** | **bool** |  | [optional] 

## Example

```python
from test_templates_api.models.link import Link

# TODO update the JSON string below
json = "{}"
# create an instance of Link from a JSON string
link_instance = Link.from_json(json)
# print the JSON string representation of the object
print Link.to_json()

# convert the object into a dict
link_dict = link_instance.to_dict()
# create an instance of Link from a dict
link_form_dict = link.from_dict(link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


