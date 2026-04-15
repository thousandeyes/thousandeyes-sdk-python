# TagFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | [**TagFilterType**](TagFilterType.md) |  | [optional] 
**values** | **List[str]** |  | [optional] 
**mode** | [**TagFilterMode**](TagFilterMode.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.tags.models.tag_filter import TagFilter

# TODO update the JSON string below
json = "{}"
# create an instance of TagFilter from a JSON string
tag_filter_instance = TagFilter.from_json(json)
# print the JSON string representation of the object
print(TagFilter.to_json())

# convert the object into a dict
tag_filter_dict = tag_filter_instance.to_dict()
# create an instance of TagFilter from a dict
tag_filter_from_dict = TagFilter.from_dict(tag_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


