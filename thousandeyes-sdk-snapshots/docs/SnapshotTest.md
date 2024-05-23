# SnapshotTest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interval** | [**TestInterval**](TestInterval.md) |  | [optional] 
**alerts_enabled** | **bool** | Indicates if alerts are enabled. | [optional] 
**enabled** | **bool** | Test is enabled. | [optional] [default to True]
**created_by** | **str** | User that created the test. | [optional] [readonly] 
**created_date** | **datetime** | UTC created date (ISO date-time format). | [optional] [readonly] 
**description** | **str** | A description of the test. | [optional] 
**live_share** | **bool** | Indicates if the test is shared with the account group. | [optional] [readonly] 
**modified_by** | **str** | User that modified the test. | [optional] [readonly] 
**modified_date** | **datetime** | UTC last modification date (ISO date-time format). | [optional] [readonly] 
**saved_event** | **bool** | Indicates if the test is a saved event. | [optional] [readonly] 
**test_id** | **str** | Each test is assigned an unique ID; this is used to access test information and results from other endpoints. | [optional] [readonly] 
**test_name** | **str** | The name of the test. Test name must be unique. | [optional] 
**type** | [**TestType**](TestType.md) |  | [optional] 
**links** | [**TestLinks**](TestLinks.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.snapshots.models.snapshot_test import SnapshotTest

# TODO update the JSON string below
json = "{}"
# create an instance of SnapshotTest from a JSON string
snapshot_test_instance = SnapshotTest.from_json(json)
# print the JSON string representation of the object
print(SnapshotTest.to_json())

# convert the object into a dict
snapshot_test_dict = snapshot_test_instance.to_dict()
# create an instance of SnapshotTest from a dict
snapshot_test_from_dict = SnapshotTest.from_dict(snapshot_test_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


