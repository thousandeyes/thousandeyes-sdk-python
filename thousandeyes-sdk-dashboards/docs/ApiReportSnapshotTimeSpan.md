# ApiReportSnapshotTimeSpan

Time span of the dashboard snapshot.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **str** | UTC start date of dashboard snapshot. | [optional] 
**start** | **datetime** | UTC start date of dashboard snapshot (ISO date-time format). | [optional] 
**duration** | **int** | Duration of dashboard snapshot in seconds. | [optional] 

## Example

```python
from thousandeyes_sdk.dashboards.models.api_report_snapshot_time_span import ApiReportSnapshotTimeSpan

# TODO update the JSON string below
json = "{}"
# create an instance of ApiReportSnapshotTimeSpan from a JSON string
api_report_snapshot_time_span_instance = ApiReportSnapshotTimeSpan.from_json(json)
# print the JSON string representation of the object
print(ApiReportSnapshotTimeSpan.to_json())

# convert the object into a dict
api_report_snapshot_time_span_dict = api_report_snapshot_time_span_instance.to_dict()
# create an instance of ApiReportSnapshotTimeSpan from a dict
api_report_snapshot_time_span_from_dict = ApiReportSnapshotTimeSpan.from_dict(api_report_snapshot_time_span_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


