# SnapshotRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | Snapshot title. | 
**start_date** | **datetime** | The start date for the snapshot in UTC time, formatted in ISO date-time. | 
**end_date** | **datetime** | The end date for the snapshot in UTC time, formatted in ISO date-time. | 
**is_public** | **bool** | Set to &#x60;true&#x60; for saved events and &#x60;false&#x60; for share links. Its default value is &#x60;false&#x60;. | [optional] 

## Example

```python
from thousandeyes_sdk.snapshots.models.snapshot_request import SnapshotRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SnapshotRequest from a JSON string
snapshot_request_instance = SnapshotRequest.from_json(json)
# print the JSON string representation of the object
print(SnapshotRequest.to_json())

# convert the object into a dict
snapshot_request_dict = snapshot_request_instance.to_dict()
# create an instance of SnapshotRequest from a dict
snapshot_request_from_dict = SnapshotRequest.from_dict(snapshot_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


