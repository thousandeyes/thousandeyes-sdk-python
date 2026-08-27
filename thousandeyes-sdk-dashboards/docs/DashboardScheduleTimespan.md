# DashboardScheduleTimespan

Amount of historical data to include in each scheduled snapshot.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**n** | **int** | Number of time units in the snapshot data range. | 
**period** | [**DashboardScheduleTimespanPeriod**](DashboardScheduleTimespanPeriod.md) |  | 

## Example

```python
from thousandeyes_sdk.dashboards.models.dashboard_schedule_timespan import DashboardScheduleTimespan

# TODO update the JSON string below
json = "{}"
# create an instance of DashboardScheduleTimespan from a JSON string
dashboard_schedule_timespan_instance = DashboardScheduleTimespan.from_json(json)
# print the JSON string representation of the object
print(DashboardScheduleTimespan.to_json())

# convert the object into a dict
dashboard_schedule_timespan_dict = dashboard_schedule_timespan_instance.to_dict()
# create an instance of DashboardScheduleTimespan from a dict
dashboard_schedule_timespan_from_dict = DashboardScheduleTimespan.from_dict(dashboard_schedule_timespan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


