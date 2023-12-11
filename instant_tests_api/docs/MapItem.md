# MapItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from instant_tests_api.models.map_item import MapItem

# TODO update the JSON string below
json = "{}"
# create an instance of MapItem from a JSON string
map_item_instance = MapItem.from_json(json)
# print the JSON string representation of the object
print MapItem.to_json()

# convert the object into a dict
map_item_dict = map_item_instance.to_dict()
# create an instance of MapItem from a dict
map_item_form_dict = map_item.from_dict(map_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


