# DashboardScheduleCustomRepeat


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**repeat_every** | **int** | Interval count for custom recurrence. | 
**days_of_week** | **List[int]** | Days of the week for custom weekly recurrence (&#x60;1&#x60; &#x3D; Monday through &#x60;7&#x60; &#x3D; Sunday). | [optional] 
**repeat_unit** | [**DashboardScheduleCustomRepeatUnit**](DashboardScheduleCustomRepeatUnit.md) |  | 

## Example

```python
from thousandeyes_sdk.dashboards.models.dashboard_schedule_custom_repeat import DashboardScheduleCustomRepeat

# TODO update the JSON string below
json = "{}"
# create an instance of DashboardScheduleCustomRepeat from a JSON string
dashboard_schedule_custom_repeat_instance = DashboardScheduleCustomRepeat.from_json(json)
# print the JSON string representation of the object
print(DashboardScheduleCustomRepeat.to_json())

# convert the object into a dict
dashboard_schedule_custom_repeat_dict = dashboard_schedule_custom_repeat_instance.to_dict()
# create an instance of DashboardScheduleCustomRepeat from a dict
dashboard_schedule_custom_repeat_from_dict = DashboardScheduleCustomRepeat.from_dict(dashboard_schedule_custom_repeat_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


