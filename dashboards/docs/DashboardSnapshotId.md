# DashboardSnapshotId


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**snapshot_id** | **str** | Identifier of the dashboard snapshot. | [optional] 

## Example

```python
from dashboards.models.dashboard_snapshot_id import DashboardSnapshotId

# TODO update the JSON string below
json = "{}"
# create an instance of DashboardSnapshotId from a JSON string
dashboard_snapshot_id_instance = DashboardSnapshotId.from_json(json)
# print the JSON string representation of the object
print(DashboardSnapshotId.to_json())

# convert the object into a dict
dashboard_snapshot_id_dict = dashboard_snapshot_id_instance.to_dict()
# create an instance of DashboardSnapshotId from a dict
dashboard_snapshot_id_from_dict = DashboardSnapshotId.from_dict(dashboard_snapshot_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


