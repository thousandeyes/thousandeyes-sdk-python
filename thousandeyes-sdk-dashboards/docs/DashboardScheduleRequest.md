# DashboardScheduleRequest

Snapshot schedule configuration for create or update requests.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cron_spec** | [**DashboardScheduleCronSpec**](DashboardScheduleCronSpec.md) |  | 
**data_source** | [**DashboardScheduleDataSource**](DashboardScheduleDataSource.md) |  | 
**data_timespan** | [**DashboardScheduleTimespan**](DashboardScheduleTimespan.md) |  | 
**flag_enabled** | **bool** | When &#x60;true&#x60;, the schedule is active and snapshots are generated according to &#x60;cronSpec&#x60;. | 
**flag_locked** | **bool** | When &#x60;true&#x60;, the schedule configuration is locked and cannot be edited through the web application. | [optional] 
**flag_auto_share** | **bool** | When &#x60;true&#x60;, generated snapshots are automatically shared with schedule recipients. | [optional] 
**flag_is_include_pii_user_data** | **bool** | When &#x60;true&#x60;, generated snapshots include personally identifiable user data when permitted by account policy. | [optional] 
**flag_attach_pdf_to_email** | **bool** | When &#x60;true&#x60;, a PDF attachment is included in snapshot notification emails. | [optional] 
**recipients** | **List[str]** | Email addresses of active dashboard account users who receive snapshot notifications. Unknown or duplicate addresses are rejected. | [optional] 
**expires_after** | **int** | Snapshot retention period in seconds. Allowed range is 24 hours to 5 years. Defaults to 5 years when omitted. | [optional] [default to 157680000]

## Example

```python
from thousandeyes_sdk.dashboards.models.dashboard_schedule_request import DashboardScheduleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DashboardScheduleRequest from a JSON string
dashboard_schedule_request_instance = DashboardScheduleRequest.from_json(json)
# print the JSON string representation of the object
print(DashboardScheduleRequest.to_json())

# convert the object into a dict
dashboard_schedule_request_dict = dashboard_schedule_request_instance.to_dict()
# create an instance of DashboardScheduleRequest from a dict
dashboard_schedule_request_from_dict = DashboardScheduleRequest.from_dict(dashboard_schedule_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


