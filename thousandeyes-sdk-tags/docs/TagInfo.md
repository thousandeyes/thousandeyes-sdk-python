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
**filters** | [**List[TagFilter]**](TagFilter.md) | The combination of filters (filter keys) dynamically assigned to an &#x60;endpoint-agent&#x60; as determined by the matching logic (&#x60;and&#x60; or &#x60;or&#x60;). For example, if you filter on &#x60;bssid&#x60; and &#x60;ssid&#x60; with a matching logic of &#x60;and&#x60;, both filters are assigned as tags to the &#x60;endpoint-agent&#x60;; &#x60;or&#x60; means either filter can be assigned. **Note:** filters currently only apply to &#x60;endpoint-agent&#x60; object types. | [optional] 

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


