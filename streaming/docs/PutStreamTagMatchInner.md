# PutStreamTagMatchInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_type** | [**TagMatchObjectType**](TagMatchObjectType.md) |  | [optional] 
**key** | **str** | The name of the tag key to match | [optional] 
**value** | **str** | The value of the tag to match | [optional] 

## Example

```python
from streaming.models.put_stream_tag_match_inner import PutStreamTagMatchInner

# TODO update the JSON string below
json = "{}"
# create an instance of PutStreamTagMatchInner from a JSON string
put_stream_tag_match_inner_instance = PutStreamTagMatchInner.from_json(json)
# print the JSON string representation of the object
print(PutStreamTagMatchInner.to_json())

# convert the object into a dict
put_stream_tag_match_inner_dict = put_stream_tag_match_inner_instance.to_dict()
# create an instance of PutStreamTagMatchInner from a dict
put_stream_tag_match_inner_from_dict = PutStreamTagMatchInner.from_dict(put_stream_tag_match_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


