# TagBulkCreateError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tag** | [**Dict[str, TagInfo]**](TagInfo.md) |  | [optional] 
**response_code** | **int** | HTTP response code | [optional] 
**message** | **str** | Status / error message | [optional] 

## Example

```python
from thousandeyes_sdk.tags.models.tag_bulk_create_error import TagBulkCreateError

# TODO update the JSON string below
json = "{}"
# create an instance of TagBulkCreateError from a JSON string
tag_bulk_create_error_instance = TagBulkCreateError.from_json(json)
# print the JSON string representation of the object
print(TagBulkCreateError.to_json())

# convert the object into a dict
tag_bulk_create_error_dict = tag_bulk_create_error_instance.to_dict()
# create an instance of TagBulkCreateError from a dict
tag_bulk_create_error_from_dict = TagBulkCreateError.from_dict(tag_bulk_create_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


