# ScalableWidget


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min_scale** | **float** | Minimum scale configured in the widget. | [optional] 
**max_scale** | **float** | Maximum scale configured in the widget. | [optional] 
**unit** | [**ApiWidgetFixedYScalePrefix**](ApiWidgetFixedYScalePrefix.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.dashboards.models.scalable_widget import ScalableWidget

# TODO update the JSON string below
json = "{}"
# create an instance of ScalableWidget from a JSON string
scalable_widget_instance = ScalableWidget.from_json(json)
# print the JSON string representation of the object
print(ScalableWidget.to_json())

# convert the object into a dict
scalable_widget_dict = scalable_widget_instance.to_dict()
# create an instance of ScalableWidget from a dict
scalable_widget_from_dict = ScalableWidget.from_dict(scalable_widget_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


