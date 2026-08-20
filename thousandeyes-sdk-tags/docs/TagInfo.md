# TagInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assignments** | [**List[Assignment]**](Assignment.md) |  | [optional] [readonly] 
**access_type** | [**AccessType**](AccessType.md) |  | [optional] 
**aid** | **int** | The account group ID | [optional] [readonly] 
**built_in** | **bool** | Indicates whether it is a built-in tag or a user-created (custom) tag. | [optional] [readonly] 
**color** | **str** | Tag color | [optional] 
**create_date** | **str** | Tag creation date | [optional] [readonly] 
**icon** | **str** |  | [optional] 
**description** | **str** | The tag&#39;s description. | [optional] 
**id** | **str** | The tag ID | [optional] [readonly] 
**key** | **str** | The tags&#39;s key | [optional] 
**legacy_id** | **float** |  | [optional] [readonly] 
**modified_date** | **datetime** | The date and time the tag was last modified. | [optional] [readonly] 
**object_type** | [**ObjectType**](ObjectType.md) |  | [optional] 
**type** | [**Type**](Type.md) |  | [optional] 
**value** | **str** | The tag&#39;s value | [optional] 
**match_type** | [**TagMatchType**](TagMatchType.md) |  | [optional] 
**filters** | [**List[TagFilter]**](TagFilter.md) | Filter criteria used to dynamically assign the tag to endpoint agents. The matching logic determines how multiple filters are evaluated: &#x60;and&#x60; requires all filters to match, while &#x60;or&#x60; requires any filter to match. Filters are supported only for &#x60;endpoint-agent&#x60; object types. | [optional] 

## Example

```python
from thousandeyes_sdk.tags.models.tag_info import TagInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TagInfo from a JSON string
tag_info_instance = TagInfo.from_json(json)
# print the JSON string representation of the object
print(TagInfo.to_json())

# convert the object into a dict
tag_info_dict = tag_info_instance.to_dict()
# create an instance of TagInfo from a dict
tag_info_from_dict = TagInfo.from_dict(tag_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


