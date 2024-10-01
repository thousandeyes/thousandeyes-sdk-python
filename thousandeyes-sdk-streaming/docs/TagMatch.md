# TagMatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The name of the tag key to match | [optional] 
**value** | **str** | The value of the tag to match | [optional] 

## Example

```python
from thousandeyes_sdk.streaming.models.tag_match import TagMatch

# TODO update the JSON string below
json = "{}"
# create an instance of TagMatch from a JSON string
tag_match_instance = TagMatch.from_json(json)
# print the JSON string representation of the object
print(TagMatch.to_json())

# convert the object into a dict
tag_match_dict = tag_match_instance.to_dict()
# create an instance of TagMatch from a dict
tag_match_from_dict = TagMatch.from_dict(tag_match_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


