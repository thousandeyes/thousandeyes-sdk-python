# ApiNumbersCard

An individual number card within the numbers card widget.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min_scale** | **float** | Minimum scale configured in the widget. | [optional] 
**max_scale** | **float** | Maximum scale configured in the widget. | [optional] 
**unit** | [**ApiWidgetFixedYScalePrefix**](ApiWidgetFixedYScalePrefix.md) |  | [optional] 
**id** | **str** | Identifier of the widget. | [optional] 
**description** | **str** | Description of the number card. | [optional] 
**measure** | [**ApiWidgetMeasure**](ApiWidgetMeasure.md) |  | [optional] 
**compare_to_previous_value** | **bool** |  | [optional] 
**fixed_timespan** | [**ApiDuration**](ApiDuration.md) |  | [optional] 
**should_exclude_alert_suppression_windows** | **bool** | Excludes alert suppression windows from the widget when set to &#x60;true&#x60;. | [optional] 
**data_source** | [**NumbersCardDatasource**](NumbersCardDatasource.md) |  | [optional] 
**metric_group** | [**MetricGroup**](MetricGroup.md) |  | [optional] 
**direction** | [**DashboardMetricDirection**](DashboardMetricDirection.md) |  | [optional] 
**metric** | [**DashboardMetric**](DashboardMetric.md) |  | [optional] 
**filters** | **Dict[str, List[object]]** | (Optional) Specifies the filters applied to the widget. When present, the &#x60;filters&#x60; property displays. Each filter object has two properties: &#x60;filterProperty&#x60; and &#x60;filterValue&#x60;. The &#x60;filterProperty&#x60; can be values like &#x60;AGENT&#x60;, &#x60;ENDPOINT_MACHINE_ID&#x60;, &#x60;TEST&#x60;, &#x60;MONITOR&#x60;, etc.  The &#x60;filterValue&#x60; represents an identifier array of the selected property. | [optional] 

## Example

```python
from thousandeyes_sdk.dashboards.models.api_numbers_card import ApiNumbersCard

# TODO update the JSON string below
json = "{}"
# create an instance of ApiNumbersCard from a JSON string
api_numbers_card_instance = ApiNumbersCard.from_json(json)
# print the JSON string representation of the object
print(ApiNumbersCard.to_json())

# convert the object into a dict
api_numbers_card_dict = api_numbers_card_instance.to_dict()
# create an instance of ApiNumbersCard from a dict
api_numbers_card_from_dict = ApiNumbersCard.from_dict(api_numbers_card_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


