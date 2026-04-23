# WidgetPosition

Position and size of a widget in the layout grid.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**x** | **int** | Horizontal position. | 
**y** | **int** | Vertical position. | 
**w** | **int** | Width in grid units. | 
**h** | **int** | Height in grid units. | 
**id** | **str** | Identifier of the widget this position applies to. | [optional] 

## Example

```python
from thousandeyes_sdk.dashboards.models.widget_position import WidgetPosition

# TODO update the JSON string below
json = "{}"
# create an instance of WidgetPosition from a JSON string
widget_position_instance = WidgetPosition.from_json(json)
# print the JSON string representation of the object
print(WidgetPosition.to_json())

# convert the object into a dict
widget_position_dict = widget_position_instance.to_dict()
# create an instance of WidgetPosition from a dict
widget_position_from_dict = WidgetPosition.from_dict(widget_position_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


