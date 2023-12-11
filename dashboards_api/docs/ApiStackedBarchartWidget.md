# ApiStackedBarchartWidget


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identifier of the widget. | [optional] 
**type** | [**WidgetType**](WidgetType.md) |  | [optional] 
**title** | **str** | Title of the widget | [optional] 
**visual_mode** | [**VisualMode**](VisualMode.md) |  | [optional] 
**embed_url** | **str** | When &#x60;isEmbedded&#x60; is set to &#x60;true&#x60;, an &#x60;embedUrl&#x60; is provided. | [optional] [readonly] 
**is_embedded** | **bool** | Set to &#x60;true&#x60; if widget is marked as embedded; otherwise, set to &#x60;false&#x60;. | [optional] 
**metric_group** | [**MetricGroup**](MetricGroup.md) |  | [optional] 
**direction** | [**DashboardMetricDirection**](DashboardMetricDirection.md) |  | [optional] 
**metric** | [**DashboardMetric**](DashboardMetric.md) |  | [optional] 
**filters** | **Dict[str, List[object]]** | (Optional) Specifies the filters applied to the widget. When present, the &#x60;filters&#x60; property displays. Each filter object has two properties: &#x60;filterProperty&#x60; and &#x60;filterValue&#x60;. The &#x60;filterProperty&#x60; can be values like Agents, Agent Groups, Tests, Monitors, etc. The &#x60;filterValue&#x60; represents theIdentifierof the selected property. | [optional] 
**measure** | [**ApiWidgetMeasure**](ApiWidgetMeasure.md) |  | [optional] 
**fixed_timespan** | [**ApiDuration**](ApiDuration.md) |  | [optional] 
**api_link** | **str** |  | [optional] [readonly] 
**should_exclude_alert_suppression_windows** | **bool** | Excludes alert suppression window data if set to &#x60;true&#x60;. | [optional] 
**links** | [**SelfLinksLinks**](SelfLinksLinks.md) |  | [optional] 
**axis_group_by** | [**ApiAggregateProperty**](ApiAggregateProperty.md) |  | [optional] 
**sort_by** | [**WidgetSortProperty**](WidgetSortProperty.md) |  | [optional] 
**sort_direction** | [**WidgetSortDirection**](WidgetSortDirection.md) |  | [optional] 
**limit** | **int** | Limit configured in the widget. | [optional] 
**show_labels** | **bool** |  | [optional] 
**is_horizontal_bar_chart** | **bool** | Set to &#x60;true&#x60; to display bars horizontally in the widget. | [optional] 
**data_source** | [**StackedBarChartDatasource**](StackedBarChartDatasource.md) |  | [optional] 

## Example

```python
from dashboards_api.models.api_stacked_barchart_widget import ApiStackedBarchartWidget

# TODO update the JSON string below
json = "{}"
# create an instance of ApiStackedBarchartWidget from a JSON string
api_stacked_barchart_widget_instance = ApiStackedBarchartWidget.from_json(json)
# print the JSON string representation of the object
print ApiStackedBarchartWidget.to_json()

# convert the object into a dict
api_stacked_barchart_widget_dict = api_stacked_barchart_widget_instance.to_dict()
# create an instance of ApiStackedBarchartWidget from a dict
api_stacked_barchart_widget_form_dict = api_stacked_barchart_widget.from_dict(api_stacked_barchart_widget_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


