# ApiMultiMetricColumn

Defines a column within a table that aggregates and displays various metrics (Multi-Metric table).

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**data_source** | [**MultiMetricsTableDatasource**](MultiMetricsTableDatasource.md) |  | [optional] 
**metric_group** | [**MetricGroup**](MetricGroup.md) |  | [optional] 
**direction** | [**DashboardMetricDirection**](DashboardMetricDirection.md) |  | [optional] 
**metric** | [**DashboardMetric**](DashboardMetric.md) |  | [optional] 
**filters** | **Dict[str, List[object]]** |  | [optional] 
**measure** | [**ApiWidgetMeasure**](ApiWidgetMeasure.md) |  | [optional] 

## Example

```python
from dashboards_api.models.api_multi_metric_column import ApiMultiMetricColumn

# TODO update the JSON string below
json = "{}"
# create an instance of ApiMultiMetricColumn from a JSON string
api_multi_metric_column_instance = ApiMultiMetricColumn.from_json(json)
# print the JSON string representation of the object
print ApiMultiMetricColumn.to_json()

# convert the object into a dict
api_multi_metric_column_dict = api_multi_metric_column_instance.to_dict()
# create an instance of ApiMultiMetricColumn from a dict
api_multi_metric_column_form_dict = api_multi_metric_column.from_dict(api_multi_metric_column_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


