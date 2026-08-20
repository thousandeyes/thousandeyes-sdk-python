# DashboardScheduleCustomCronSpec


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**repeat** | [**DashboardScheduleCustomRepeatType**](DashboardScheduleCustomRepeatType.md) |  | [optional] 
**custom_repeat** | [**DashboardScheduleCustomRepeat**](DashboardScheduleCustomRepeat.md) |  | 

## Example

```python
from thousandeyes_sdk.dashboards.models.dashboard_schedule_custom_cron_spec import DashboardScheduleCustomCronSpec

# TODO update the JSON string below
json = "{}"
# create an instance of DashboardScheduleCustomCronSpec from a JSON string
dashboard_schedule_custom_cron_spec_instance = DashboardScheduleCustomCronSpec.from_json(json)
# print the JSON string representation of the object
print(DashboardScheduleCustomCronSpec.to_json())

# convert the object into a dict
dashboard_schedule_custom_cron_spec_dict = dashboard_schedule_custom_cron_spec_instance.to_dict()
# create an instance of DashboardScheduleCustomCronSpec from a dict
dashboard_schedule_custom_cron_spec_from_dict = DashboardScheduleCustomCronSpec.from_dict(dashboard_schedule_custom_cron_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


