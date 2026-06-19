# ApiPieChartWidgetProperties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Pie Chart widget type | 
**group_by** | [**ApiAggregateProperty**](ApiAggregateProperty.md) |  | [optional] 
**data_source** | [**PieChartDatasource**](PieChartDatasource.md) |  | [optional] 
**show_submetrics** | **bool** | Controls how metrics with submetric components are displayed. If &#x60;true&#x60; (default), the widget displays one chart per group. If &#x60;false&#x60;, the widget displays all submetrics in a single chart. For metrics without submetric components, this field is ignored and returned as &#x60;null&#x60;. | [optional] [default to True]

## Example

```python
from thousandeyes_sdk.dashboards.models.api_pie_chart_widget_properties import ApiPieChartWidgetProperties

# TODO update the JSON string below
json = "{}"
# create an instance of ApiPieChartWidgetProperties from a JSON string
api_pie_chart_widget_properties_instance = ApiPieChartWidgetProperties.from_json(json)
# print the JSON string representation of the object
print(ApiPieChartWidgetProperties.to_json())

# convert the object into a dict
api_pie_chart_widget_properties_dict = api_pie_chart_widget_properties_instance.to_dict()
# create an instance of ApiPieChartWidgetProperties from a dict
api_pie_chart_widget_properties_from_dict = ApiPieChartWidgetProperties.from_dict(api_pie_chart_widget_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


