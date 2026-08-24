# DashboardScheduleCronSpec

Cron-style recurrence specification for a dashboard snapshot schedule.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_time** | **int** | Schedule start time as a Unix timestamp in seconds. | 
**zone_code** | **str** | An IANA time zone identifier used to interpret &#x60;startTime&#x60; and recurrence. For example, &#x60;America/Los_Angeles&#x60;. | 
**repeat** | [**DashboardScheduleRepeat**](DashboardScheduleRepeat.md) |  | 
**end_repeat** | [**DashboardScheduleEndCondition**](DashboardScheduleEndCondition.md) |  | [optional] 
**custom_repeat** | [**DashboardScheduleCustomRepeat**](DashboardScheduleCustomRepeat.md) |  | 

## Example

```python
from thousandeyes_sdk.dashboards.models.dashboard_schedule_cron_spec import DashboardScheduleCronSpec

# TODO update the JSON string below
json = "{}"
# create an instance of DashboardScheduleCronSpec from a JSON string
dashboard_schedule_cron_spec_instance = DashboardScheduleCronSpec.from_json(json)
# print the JSON string representation of the object
print(DashboardScheduleCronSpec.to_json())

# convert the object into a dict
dashboard_schedule_cron_spec_dict = dashboard_schedule_cron_spec_instance.to_dict()
# create an instance of DashboardScheduleCronSpec from a dict
dashboard_schedule_cron_spec_from_dict = DashboardScheduleCronSpec.from_dict(dashboard_schedule_cron_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


