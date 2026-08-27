# DashboardScheduleEndCondition

Condition that determines when the recurring schedule ends.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_condition_type** | **str** | Identifies a schedule that ends on a specified date. | 
**value** | **int** | Unix timestamp in seconds when the recurrence ends. | 

## Example

```python
from thousandeyes_sdk.dashboards.models.dashboard_schedule_end_condition import DashboardScheduleEndCondition

# TODO update the JSON string below
json = "{}"
# create an instance of DashboardScheduleEndCondition from a JSON string
dashboard_schedule_end_condition_instance = DashboardScheduleEndCondition.from_json(json)
# print the JSON string representation of the object
print(DashboardScheduleEndCondition.to_json())

# convert the object into a dict
dashboard_schedule_end_condition_dict = dashboard_schedule_end_condition_instance.to_dict()
# create an instance of DashboardScheduleEndCondition from a dict
dashboard_schedule_end_condition_from_dict = DashboardScheduleEndCondition.from_dict(dashboard_schedule_end_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


