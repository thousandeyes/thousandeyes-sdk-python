# TagCollection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tags** | [**List[GetTag]**](GetTag.md) |  | [optional] 

## Example

```python
from tags.models.tag_collection import TagCollection

# TODO update the JSON string below
json = "{}"
# create an instance of TagCollection from a JSON string
tag_collection_instance = TagCollection.from_json(json)
# print the JSON string representation of the object
print(TagCollection.to_json())

# convert the object into a dict
tag_collection_dict = tag_collection_instance.to_dict()
# create an instance of TagCollection from a dict
tag_collection_from_dict = TagCollection.from_dict(tag_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


