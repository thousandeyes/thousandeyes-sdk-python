# DashboardSnapshotLinks

A links object containing the self link.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**DashboardSnapshotLinksLinks**](DashboardSnapshotLinksLinks.md) |  | [optional] 

## Example

```python
from dashboards_api.models.dashboard_snapshot_links import DashboardSnapshotLinks

# TODO update the JSON string below
json = "{}"
# create an instance of DashboardSnapshotLinks from a JSON string
dashboard_snapshot_links_instance = DashboardSnapshotLinks.from_json(json)
# print the JSON string representation of the object
print DashboardSnapshotLinks.to_json()

# convert the object into a dict
dashboard_snapshot_links_dict = dashboard_snapshot_links_instance.to_dict()
# create an instance of DashboardSnapshotLinks from a dict
dashboard_snapshot_links_form_dict = dashboard_snapshot_links.from_dict(dashboard_snapshot_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


