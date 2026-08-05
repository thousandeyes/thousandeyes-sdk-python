# ApiListWidgetRow

A row in a **List** widget. Property names are dimension display labels mapped to their values for that row.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**ApiListWidgetRowLinks**](ApiListWidgetRowLinks.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.dashboards.models.api_list_widget_row import ApiListWidgetRow

# TODO update the JSON string below
json = "{}"
# create an instance of ApiListWidgetRow from a JSON string
api_list_widget_row_instance = ApiListWidgetRow.from_json(json)
# print the JSON string representation of the object
print(ApiListWidgetRow.to_json())

# convert the object into a dict
api_list_widget_row_dict = api_list_widget_row_instance.to_dict()
# create an instance of ApiListWidgetRow from a dict
api_list_widget_row_from_dict = ApiListWidgetRow.from_dict(api_list_widget_row_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


