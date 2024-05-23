# SnapshotResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Snapshot ID. | [optional] 
**start_round_id** | **int** | The start time of the test snapshot, represented in epoch time format (in seconds). | [optional] [readonly] 
**end_round_id** | **int** | The end time of the test snapshot, represented in epoch time format (in seconds). | [optional] [readonly] 
**round_id** | **int** | The selected time of the test snapshot, represented in epoch time format (in seconds). | [optional] [readonly] 
**share_date** | **datetime** | The date when the test snapshot was created in UTC time, formatted in ISO date-time. | [optional] 
**source_test_id** | **str** | Snapshot test ID. | [optional] 
**test_id** | **str** | Snapshot test ID. | [optional] 
**uid** | **str** | User ID. | [optional] 
**display_name** | **str** | Snapshot title. | [optional] 
**extra_params** | **str** | Extra parameters. | [optional] 
**test** | [**SnapshotTest**](SnapshotTest.md) |  | [optional] 
**links** | [**SnapshotLinks**](SnapshotLinks.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.snapshots.models.snapshot_response import SnapshotResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SnapshotResponse from a JSON string
snapshot_response_instance = SnapshotResponse.from_json(json)
# print the JSON string representation of the object
print(SnapshotResponse.to_json())

# convert the object into a dict
snapshot_response_dict = snapshot_response_instance.to_dict()
# create an instance of SnapshotResponse from a dict
snapshot_response_from_dict = SnapshotResponse.from_dict(snapshot_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


