# ApiWidgetMeasure

Determines how to aggregate the the metric.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**WidgetMeasureType**](WidgetMeasureType.md) |  | [optional] 
**percentile_value** | **float** | The percentile value to use when &#x60;type &#x3D;&#x3D; NTH_PERCENTILE&#x60;. | [optional] 

## Example

```python
from thousandeyes_sdk.dashboards.models.api_widget_measure import ApiWidgetMeasure

# TODO update the JSON string below
json = "{}"
# create an instance of ApiWidgetMeasure from a JSON string
api_widget_measure_instance = ApiWidgetMeasure.from_json(json)
# print the JSON string representation of the object
print(ApiWidgetMeasure.to_json())

# convert the object into a dict
api_widget_measure_dict = api_widget_measure_instance.to_dict()
# create an instance of ApiWidgetMeasure from a dict
api_widget_measure_from_dict = ApiWidgetMeasure.from_dict(api_widget_measure_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


