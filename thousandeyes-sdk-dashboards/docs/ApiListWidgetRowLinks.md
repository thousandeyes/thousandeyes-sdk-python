# ApiListWidgetRowLinks

Links for a **List** widget row.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**Link**](Link.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.dashboards.models.api_list_widget_row_links import ApiListWidgetRowLinks

# TODO update the JSON string below
json = "{}"
# create an instance of ApiListWidgetRowLinks from a JSON string
api_list_widget_row_links_instance = ApiListWidgetRowLinks.from_json(json)
# print the JSON string representation of the object
print(ApiListWidgetRowLinks.to_json())

# convert the object into a dict
api_list_widget_row_links_dict = api_list_widget_row_links_instance.to_dict()
# create an instance of ApiListWidgetRowLinks from a dict
api_list_widget_row_links_from_dict = ApiListWidgetRowLinks.from_dict(api_list_widget_row_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


