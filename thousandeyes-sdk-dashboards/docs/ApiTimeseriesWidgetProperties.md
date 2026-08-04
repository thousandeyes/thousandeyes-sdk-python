# ApiTimeseriesWidgetProperties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Time Series: Line widget type. | 
**show_timeseries_overall_baseline** | **bool** | Displays the overall baseline when set to &#x60;true&#x60;. | [optional] [default to False]
**group_by** | [**ApiAggregateProperty**](ApiAggregateProperty.md) |  | [optional] 
**is_timeseries_one_chart_per_line** | **bool** | Displays a separate chart for each line when set to &#x60;true&#x60;. | [optional] [default to False]
**show_zoom_slider** | **bool** | Displays the zoom slider on the time axis when set to &#x60;true&#x60;. | [optional] [default to False]
**data_source** | [**TimeseriesDatasource**](TimeseriesDatasource.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.dashboards.models.api_timeseries_widget_properties import ApiTimeseriesWidgetProperties

# TODO update the JSON string below
json = "{}"
# create an instance of ApiTimeseriesWidgetProperties from a JSON string
api_timeseries_widget_properties_instance = ApiTimeseriesWidgetProperties.from_json(json)
# print the JSON string representation of the object
print(ApiTimeseriesWidgetProperties.to_json())

# convert the object into a dict
api_timeseries_widget_properties_dict = api_timeseries_widget_properties_instance.to_dict()
# create an instance of ApiTimeseriesWidgetProperties from a dict
api_timeseries_widget_properties_from_dict = ApiTimeseriesWidgetProperties.from_dict(api_timeseries_widget_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


