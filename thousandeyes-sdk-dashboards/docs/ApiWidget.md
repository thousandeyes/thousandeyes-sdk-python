# ApiWidget


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identifier of the widget. | [optional] [readonly] 
**title** | **str** | Title of the widget | [optional] 
**visual_mode** | [**VisualMode**](VisualMode.md) |  | [optional] 
**embed_url** | **str** | When &#x60;isEmbedded&#x60; is set to &#x60;true&#x60;, an &#x60;embedUrl&#x60; is provided. | [optional] [readonly] 
**is_embedded** | **bool** | Set to &#x60;true&#x60; if widget is marked as embedded; otherwise, set to &#x60;false&#x60;. | [optional] 
**metric_group** | [**MetricGroup**](MetricGroup.md) |  | [optional] 
**direction** | [**DashboardMetricDirection**](DashboardMetricDirection.md) |  | [optional] 
**metric** | [**DashboardMetric**](DashboardMetric.md) |  | [optional] 
**filters** | **Dict[str, List[object]]** | (Optional) Specifies the filters applied to the widget. When present, the &#x60;filters&#x60; property displays. Each filter object has two properties: &#x60;filterProperty&#x60; and &#x60;filterValue&#x60;. The &#x60;filterProperty&#x60; can be values like &#x60;AGENT&#x60;, &#x60;ENDPOINT_MACHINE_ID&#x60;, &#x60;TEST&#x60;, &#x60;MONITOR&#x60;, etc.  The &#x60;filterValue&#x60; represents an identifier array of the selected property. | [optional] 
**measure** | [**ApiWidgetMeasure**](ApiWidgetMeasure.md) |  | [optional] 
**fixed_timespan** | [**ApiDuration**](ApiDuration.md) |  | [optional] 
**api_link** | **str** |  | [optional] [readonly] 
**should_exclude_alert_suppression_windows** | **bool** | Excludes alert suppression window data if set to &#x60;true&#x60;. | [optional] 
**links** | [**SelfLinks**](SelfLinks.md) |  | [optional] 
**type** | **str** | Time Series: Line widget type. | 
**agents** | [**LegacyAgentWidgetType**](LegacyAgentWidgetType.md) |  | [optional] 
**show** | [**LegacyAgentWidgetShow**](LegacyAgentWidgetShow.md) |  | [optional] 
**data_source** | [**TimeseriesDatasource**](TimeseriesDatasource.md) |  | [optional] 
**alert_types** | [**List[LegacyAlertListAlertType]**](LegacyAlertListAlertType.md) | List of alert types configured in the widget, an empty list means all alert types. | [optional] 
**limit_to** | **int** | Limit the number of alerts displayed in the widget. | [optional] 
**active_within** | [**ActiveWithin**](ActiveWithin.md) |  | [optional] 
**min_scale** | **float** | Minimum scale configured in the widget. | [optional] 
**max_scale** | **float** | Maximum scale configured in the widget. | [optional] 
**unit** | [**ApiWidgetFixedYScalePrefix**](ApiWidgetFixedYScalePrefix.md) |  | [optional] 
**group_by** | [**ApiAggregateProperty**](ApiAggregateProperty.md) |  | [optional] 
**cards** | [**ApiAggregateProperty**](ApiAggregateProperty.md) |  | [optional] 
**group_cards_by** | [**ApiAggregateProperty**](ApiAggregateProperty.md) |  | [optional] 
**columns** | **int** | Number of columns: 1 or 2. | [optional] 
**limit** | **int** | Limit configured in the widget. | [optional] 
**sort_by** | [**LegacyWidgetSortProperty**](LegacyWidgetSortProperty.md) |  | [optional] 
**sort_direction** | [**LegacyWidgetSortDirection**](LegacyWidgetSortDirection.md) |  | [optional] 
**is_geo_map_per_test** | **bool** | Indicates whether a separate map is displayed for each test within the widget. When set to true, individual maps are generated. | [optional] 
**axis_group_by** | [**ApiAggregateProperty**](ApiAggregateProperty.md) |  | [optional] 
**show_labels** | **bool** |  | [optional] 
**is_horizontal_bar_chart** | **bool** | Set to &#x60;true&#x60; to display bars horizontally in the widget. | [optional] 
**compare_to_previous_value** | **bool** |  | [optional] 
**row_group_by** | [**ApiAggregateProperty**](ApiAggregateProperty.md) |  | [optional] 
**multi_metric_columns** | [**List[ApiMultiMetricColumn]**](ApiMultiMetricColumn.md) |  | [optional] 
**number_cards** | [**List[ApiNumbersCard]**](ApiNumbersCard.md) |  | [optional] 
**column_group_by** | [**ApiAggregateProperty**](ApiAggregateProperty.md) |  | [optional] 
**filter** | [**ApiWidgetFilterApiTestTableFilterKey**](ApiWidgetFilterApiTestTableFilterKey.md) |  | [optional] 
**exclude** | [**ApiWidgetFilterApiTestTableFilterKey**](ApiWidgetFilterApiTestTableFilterKey.md) |  | [optional] 
**show_timeseries_overall_baseline** | **bool** | Displays the overall baseline if set to &#x60;true&#x60;. | [optional] 
**is_timeseries_one_chart_per_line** | **bool** | Displays a separate chart for each line if set to &#x60;true&#x60;. | [optional] 

## Example

```python
from thousandeyes_sdk.dashboards.models.api_widget import ApiWidget

# TODO update the JSON string below
json = "{}"
# create an instance of ApiWidget from a JSON string
api_widget_instance = ApiWidget.from_json(json)
# print the JSON string representation of the object
print(ApiWidget.to_json())

# convert the object into a dict
api_widget_dict = api_widget_instance.to_dict()
# create an instance of ApiWidget from a dict
api_widget_from_dict = ApiWidget.from_dict(api_widget_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


