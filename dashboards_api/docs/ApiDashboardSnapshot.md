# ApiDashboardSnapshot


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**DashboardSnapshotLinksLinks**](DashboardSnapshotLinksLinks.md) |  | [optional] 
**snapshot_id** | **str** | Identifier of the dashboard snapshot. | [optional] 
**snapshot_name** | **str** | Name of the dashboard snapshot. | [optional] 
**aid** | **str** | Identifier of the account group that the snapshot belongs to. | [optional] 
**is_shared** | **bool** | Set &#x60;true&#x60; if dashboard snapshot is shared, &#x60;false&#x60; otherwise. | [optional] 
**snapshot_created_date** | **datetime** | UTC date when dashboard snapshot was created (ISO date-time format). | [optional] 
**dashboard** | [**ApiDashboardSnapshotAllOfDashboard**](ApiDashboardSnapshotAllOfDashboard.md) |  | [optional] 
**widgets** | [**List[ApiWidget]**](ApiWidget.md) |  | [optional] 
**is_scheduled** | **bool** | Set &#x60;true&#x60; if dashboard snapshot was generated from a schedule, &#x60;false&#x60; otherwise. | [optional] 
**time_span** | [**ApiReportSnapshotTimeSpan**](ApiReportSnapshotTimeSpan.md) |  | [optional] 
**snapshot_expiration_date** | **datetime** | Expiration date of the snapshot. If unspecified, the snapshot expires 1 year from its creation date. The expiration date must be set within 5 years from the current date and adhere to the ISO date-time format. | [optional] 

## Example

```python
from dashboards_api.models.api_dashboard_snapshot import ApiDashboardSnapshot

# TODO update the JSON string below
json = "{}"
# create an instance of ApiDashboardSnapshot from a JSON string
api_dashboard_snapshot_instance = ApiDashboardSnapshot.from_json(json)
# print the JSON string representation of the object
print ApiDashboardSnapshot.to_json()

# convert the object into a dict
api_dashboard_snapshot_dict = api_dashboard_snapshot_instance.to_dict()
# create an instance of ApiDashboardSnapshot from a dict
api_dashboard_snapshot_form_dict = api_dashboard_snapshot.from_dict(api_dashboard_snapshot_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


