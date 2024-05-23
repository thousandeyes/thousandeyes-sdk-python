# ApiAgentStatusWidget


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
**type** | **str** | Agent Status widget type. | 
**agents** | [**LegacyAgentWidgetType**](LegacyAgentWidgetType.md) |  | [optional] 
**show** | [**LegacyAgentWidgetShow**](LegacyAgentWidgetShow.md) |  | [optional] 
**data_source** | [**AgentStatusDatasource**](AgentStatusDatasource.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.dashboards.models.api_agent_status_widget import ApiAgentStatusWidget

# TODO update the JSON string below
json = "{}"
# create an instance of ApiAgentStatusWidget from a JSON string
api_agent_status_widget_instance = ApiAgentStatusWidget.from_json(json)
# print the JSON string representation of the object
print(ApiAgentStatusWidget.to_json())

# convert the object into a dict
api_agent_status_widget_dict = api_agent_status_widget_instance.to_dict()
# create an instance of ApiAgentStatusWidget from a dict
api_agent_status_widget_from_dict = ApiAgentStatusWidget.from_dict(api_agent_status_widget_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


