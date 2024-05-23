# ApiWidgetDataPoint

Data point of a widget.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **int** | Timestamp of the aggregated data point. | [optional] 
**number_of_data_points** | **int** | Number of test data points aggregated into the widget data point. | [optional] 
**value** | **float** | Aggregated value. | [optional] 
**groups** | [**List[ApiDataPointGroup]**](ApiDataPointGroup.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.dashboards.models.api_widget_data_point import ApiWidgetDataPoint

# TODO update the JSON string below
json = "{}"
# create an instance of ApiWidgetDataPoint from a JSON string
api_widget_data_point_instance = ApiWidgetDataPoint.from_json(json)
# print the JSON string representation of the object
print(ApiWidgetDataPoint.to_json())

# convert the object into a dict
api_widget_data_point_dict = api_widget_data_point_instance.to_dict()
# create an instance of ApiWidgetDataPoint from a dict
api_widget_data_point_from_dict = ApiWidgetDataPoint.from_dict(api_widget_data_point_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


