# BulkTagAssignments


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tags** | [**List[BulkTagAssignment]**](BulkTagAssignment.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.tags.models.bulk_tag_assignments import BulkTagAssignments

# TODO update the JSON string below
json = "{}"
# create an instance of BulkTagAssignments from a JSON string
bulk_tag_assignments_instance = BulkTagAssignments.from_json(json)
# print the JSON string representation of the object
print(BulkTagAssignments.to_json())

# convert the object into a dict
bulk_tag_assignments_dict = bulk_tag_assignments_instance.to_dict()
# create an instance of BulkTagAssignments from a dict
bulk_tag_assignments_from_dict = BulkTagAssignments.from_dict(bulk_tag_assignments_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


