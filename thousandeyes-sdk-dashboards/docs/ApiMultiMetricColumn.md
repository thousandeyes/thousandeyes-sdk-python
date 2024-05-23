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
**filters** | **Dict[str, List[object]]** | (Optional) Specifies the filters applied to the widget. When present, the &#x60;filters&#x60; property displays. Each filter object has two properties: &#x60;filterProperty&#x60; and &#x60;filterValue&#x60;. The &#x60;filterProperty&#x60; can be values like &#x60;AGENT&#x60;, &#x60;ENDPOINT_MACHINE_ID&#x60;, &#x60;TEST&#x60;, &#x60;MONITOR&#x60;, etc.  The &#x60;filterValue&#x60; represents an identifier array of the selected property. | [optional] 
**measure** | [**ApiWidgetMeasure**](ApiWidgetMeasure.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.dashboards.models.api_multi_metric_column import ApiMultiMetricColumn

# TODO update the JSON string below
json = "{}"
# create an instance of ApiMultiMetricColumn from a JSON string
api_multi_metric_column_instance = ApiMultiMetricColumn.from_json(json)
# print the JSON string representation of the object
print(ApiMultiMetricColumn.to_json())

# convert the object into a dict
api_multi_metric_column_dict = api_multi_metric_column_instance.to_dict()
# create an instance of ApiMultiMetricColumn from a dict
api_multi_metric_column_from_dict = ApiMultiMetricColumn.from_dict(api_multi_metric_column_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


