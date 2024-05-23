# ApiDashboard

Dashboard upon which this dashboard snapshot is based upon.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**global_filter_id** | **str** | Default global dashboard filter ID (obtained from &#x60;/dashboards/filters&#x60; endpoint). | [optional] 
**account_id** | **int** | Identifier for the account group associated with a dashboard. | [optional] [readonly] 
**created_by** | **int** | Identifier for the user that created a dashboard. | [optional] [readonly] 
**modified_by** | **int** | Identifier for the user that last modified a dashboard. | [optional] [readonly] 
**modified_date** | **str** | UTC date/time when a dashboard was last modified. | [optional] [readonly] 
**global_override** | **bool** | When set to &#x60;true&#x60;, the defaultTimespan is used and overrides the widget&#39;s timespan. If set to &#x60;false&#x60;, the the widget&#39;s timespan is used. | [optional] 
**migrated_report** | **bool** | True if this dashboard was previously a report. | [optional] [readonly] 
**api_link** | **List[Dict[str, object]]** | A links array containing the self and the snapshots links. | [optional] 
**dashboard_id** | **str** | Identifier of a dashboard. | [optional] [readonly] 
**title** | **str** | Title of a dashboard. | [optional] 
**is_built_in** | **bool** | Indicates if a dashboard is built-in. True for built-in dashboards, false for user-created dashboards. | [optional] [readonly] 
**aid** | **str** | Identifier for the account group associated with a dashboard. | [optional] [readonly] 
**dashboard_created_by** | **str** | Identifier for the user that created a dashboard. | [optional] [readonly] 
**dashboard_modified_by** | **str** | Identifier for the user that last modified a dashboard. | [optional] [readonly] 
**dashboard_modified_date** | **datetime** | UTC date/time when a dashboard was last modified (ISO date-time format). | [optional] [readonly] 
**is_private** | **bool** | A dashboard can be viewed by other users in the account. If true, only the creator of the dashboard may view it. If false, all users in the same account may view it. | [optional] 
**is_default_for_user** | **bool** | Indicates whether this dashboard is the user&#39;s default. True for default, false if not. | [optional] [readonly] 
**is_default_for_account** | **bool** | Indicates whether this dashboard is the account group&#39;s default. True for default, false if not. | [optional] [readonly] 
**widgets** | [**List[ApiWidget]**](ApiWidget.md) |  | [optional] 
**description** | **str** | A text description of the dashboard&#39;s purpose and functionality. This information assists users in understanding the dashboard but isn&#39;t displayed when viewing a dashboard. | [optional] 
**default_timespan** | [**DefaultTimespan**](DefaultTimespan.md) |  | [optional] 
**is_global_override** | **bool** | When set to &#x60;true&#x60;, the defaultTimespan is used and overrides the widget&#39;s timespan. If set to &#x60;false&#x60;, the the widget&#39;s timespan is used. | [optional] 
**is_migrated_report** | **bool** | True if this dashboard was previously a report. | [optional] [readonly] 
**links** | [**DashboardLinks**](DashboardLinks.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.dashboards.models.api_dashboard import ApiDashboard

# TODO update the JSON string below
json = "{}"
# create an instance of ApiDashboard from a JSON string
api_dashboard_instance = ApiDashboard.from_json(json)
# print the JSON string representation of the object
print(ApiDashboard.to_json())

# convert the object into a dict
api_dashboard_dict = api_dashboard_instance.to_dict()
# create an instance of ApiDashboard from a dict
api_dashboard_from_dict = ApiDashboard.from_dict(api_dashboard_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


