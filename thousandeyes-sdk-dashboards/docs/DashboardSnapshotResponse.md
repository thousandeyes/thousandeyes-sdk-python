# DashboardSnapshotResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**snapshot_id** | **str** | Identifier of the dashboard snapshot. | [optional] 
**links** | [**SelfLinks**](SelfLinks.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.dashboards.models.dashboard_snapshot_response import DashboardSnapshotResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DashboardSnapshotResponse from a JSON string
dashboard_snapshot_response_instance = DashboardSnapshotResponse.from_json(json)
# print the JSON string representation of the object
print(DashboardSnapshotResponse.to_json())

# convert the object into a dict
dashboard_snapshot_response_dict = dashboard_snapshot_response_instance.to_dict()
# create an instance of DashboardSnapshotResponse from a dict
dashboard_snapshot_response_from_dict = DashboardSnapshotResponse.from_dict(dashboard_snapshot_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


