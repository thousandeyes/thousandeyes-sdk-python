# DashboardScheduleAfterEndCondition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_condition_type** | **str** | Identifies a schedule that ends after a number of occurrences. | 
**value** | **int** | Number of schedule occurrences after which the recurrence ends. | 

## Example

```python
from thousandeyes_sdk.dashboards.models.dashboard_schedule_after_end_condition import DashboardScheduleAfterEndCondition

# TODO update the JSON string below
json = "{}"
# create an instance of DashboardScheduleAfterEndCondition from a JSON string
dashboard_schedule_after_end_condition_instance = DashboardScheduleAfterEndCondition.from_json(json)
# print the JSON string representation of the object
print(DashboardScheduleAfterEndCondition.to_json())

# convert the object into a dict
dashboard_schedule_after_end_condition_dict = dashboard_schedule_after_end_condition_instance.to_dict()
# create an instance of DashboardScheduleAfterEndCondition from a dict
dashboard_schedule_after_end_condition_from_dict = DashboardScheduleAfterEndCondition.from_dict(dashboard_schedule_after_end_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


