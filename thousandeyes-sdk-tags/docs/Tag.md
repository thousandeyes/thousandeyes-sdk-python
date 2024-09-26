# Tag


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assignments** | [**List[Assignment]**](Assignment.md) |  | [optional] [readonly] 
**access_type** | [**AccessType**](AccessType.md) |  | [optional] 
**aid** | **int** | The account group ID | [optional] [readonly] 
**color** | **str** | Tag color | [optional] 
**create_date** | **str** | Tag creation date | [optional] [readonly] 
**icon** | **str** |  | [optional] 
**description** | **str** | The tag&#39;s description. | [optional] 
**id** | **str** | The tag ID | [optional] [readonly] 
**key** | **str** | The tags&#39;s key | [optional] 
**legacy_id** | **float** |  | [optional] [readonly] 
**object_type** | [**ObjectType**](ObjectType.md) |  | [optional] 
**value** | **str** | The tag&#39;s value | [optional] 
**links** | [**SelfLinks**](SelfLinks.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.tags.models.tag import Tag

# TODO update the JSON string below
json = "{}"
# create an instance of Tag from a JSON string
tag_instance = Tag.from_json(json)
# print the JSON string representation of the object
print(Tag.to_json())

# convert the object into a dict
tag_dict = tag_instance.to_dict()
# create an instance of Tag from a dict
tag_from_dict = Tag.from_dict(tag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


