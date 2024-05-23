# DashboardSnapshotsPage

Dashboard snapshots page.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pages** | **Dict[str, object]** |  | [optional] 
**dashboard_snapshots** | [**List[ApiDashboardSnapshot]**](ApiDashboardSnapshot.md) |  | [optional] 
**links** | [**PaginationLinks**](PaginationLinks.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.dashboards.models.dashboard_snapshots_page import DashboardSnapshotsPage

# TODO update the JSON string below
json = "{}"
# create an instance of DashboardSnapshotsPage from a JSON string
dashboard_snapshots_page_instance = DashboardSnapshotsPage.from_json(json)
# print the JSON string representation of the object
print(DashboardSnapshotsPage.to_json())

# convert the object into a dict
dashboard_snapshots_page_dict = dashboard_snapshots_page_instance.to_dict()
# create an instance of DashboardSnapshotsPage from a dict
dashboard_snapshots_page_from_dict = DashboardSnapshotsPage.from_dict(dashboard_snapshots_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


