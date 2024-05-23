# TagAssignment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assignments** | [**List[Assignment]**](Assignment.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.tags.models.tag_assignment import TagAssignment

# TODO update the JSON string below
json = "{}"
# create an instance of TagAssignment from a JSON string
tag_assignment_instance = TagAssignment.from_json(json)
# print the JSON string representation of the object
print(TagAssignment.to_json())

# convert the object into a dict
tag_assignment_dict = tag_assignment_instance.to_dict()
# create an instance of TagAssignment from a dict
tag_assignment_from_dict = TagAssignment.from_dict(tag_assignment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


