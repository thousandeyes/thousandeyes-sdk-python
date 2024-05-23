# BulkTagAssignment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assignments** | [**List[Assignment]**](Assignment.md) |  | [optional] 
**tag_id** | **str** | The ID of the tag to assign | [optional] 

## Example

```python
from thousandeyes_sdk.tags.models.bulk_tag_assignment import BulkTagAssignment

# TODO update the JSON string below
json = "{}"
# create an instance of BulkTagAssignment from a JSON string
bulk_tag_assignment_instance = BulkTagAssignment.from_json(json)
# print the JSON string representation of the object
print(BulkTagAssignment.to_json())

# convert the object into a dict
bulk_tag_assignment_dict = bulk_tag_assignment_instance.to_dict()
# create an instance of BulkTagAssignment from a dict
bulk_tag_assignment_from_dict = BulkTagAssignment.from_dict(bulk_tag_assignment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


