# DashboardScheduleNeverEndCondition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_condition_type** | **str** | Identifies a schedule that never ends. | 

## Example

```python
from thousandeyes_sdk.dashboards.models.dashboard_schedule_never_end_condition import DashboardScheduleNeverEndCondition

# TODO update the JSON string below
json = "{}"
# create an instance of DashboardScheduleNeverEndCondition from a JSON string
dashboard_schedule_never_end_condition_instance = DashboardScheduleNeverEndCondition.from_json(json)
# print the JSON string representation of the object
print(DashboardScheduleNeverEndCondition.to_json())

# convert the object into a dict
dashboard_schedule_never_end_condition_dict = dashboard_schedule_never_end_condition_instance.to_dict()
# create an instance of DashboardScheduleNeverEndCondition from a dict
dashboard_schedule_never_end_condition_from_dict = DashboardScheduleNeverEndCondition.from_dict(dashboard_schedule_never_end_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


