# ApiNumbersCard

An individual number card within the numbers card widget.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min_scale** | **float** | Mininum scale configured in the widget. | [optional] 
**max_scale** | **float** | Maximum scale configured in the widget. | [optional] 
**unit** | [**ApiWidgetFixedYScalePrefix**](ApiWidgetFixedYScalePrefix.md) |  | [optional] 
**id** | **str** | Identifier of the widget. | [optional] 
**description** | **str** | Description of the number card. | [optional] 
**measure** | [**ApiWidgetMeasure**](ApiWidgetMeasure.md) |  | [optional] 
**compare_to_previous_value** | **bool** |  | [optional] 
**fixed_timespan** | [**ApiNumbersCardAllOfFixedTimespan**](ApiNumbersCardAllOfFixedTimespan.md) |  | [optional] 
**should_exclude_alert_suppression_windows** | **bool** | Excludes alert suppression windows from the widget when set to &#x60;true&#x60;. | [optional] 
**data_source** | [**NumbersCardDatasource**](NumbersCardDatasource.md) |  | [optional] 
**metric_group** | [**MetricGroup**](MetricGroup.md) |  | [optional] 
**direction** | [**DashboardMetricDirection**](DashboardMetricDirection.md) |  | [optional] 
**metric** | [**DashboardMetric**](DashboardMetric.md) |  | [optional] 
**filters** | **Dict[str, List[object]]** | Filters to apply to the widget. | [optional] 

## Example

```python
from dashboards_api.models.api_numbers_card import ApiNumbersCard

# TODO update the JSON string below
json = "{}"
# create an instance of ApiNumbersCard from a JSON string
api_numbers_card_instance = ApiNumbersCard.from_json(json)
# print the JSON string representation of the object
print ApiNumbersCard.to_json()

# convert the object into a dict
api_numbers_card_dict = api_numbers_card_instance.to_dict()
# create an instance of ApiNumbersCard from a dict
api_numbers_card_form_dict = api_numbers_card.from_dict(api_numbers_card_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


