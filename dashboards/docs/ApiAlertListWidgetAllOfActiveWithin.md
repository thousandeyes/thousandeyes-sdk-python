# ApiAlertListWidgetAllOfActiveWithin


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **int** | Timespan value. | [optional] 
**unit** | [**LegacyDurationUnit**](LegacyDurationUnit.md) |  | [optional] 

## Example

```python
from dashboards.models.api_alert_list_widget_all_of_active_within import ApiAlertListWidgetAllOfActiveWithin

# TODO update the JSON string below
json = "{}"
# create an instance of ApiAlertListWidgetAllOfActiveWithin from a JSON string
api_alert_list_widget_all_of_active_within_instance = ApiAlertListWidgetAllOfActiveWithin.from_json(json)
# print the JSON string representation of the object
print(ApiAlertListWidgetAllOfActiveWithin.to_json())

# convert the object into a dict
api_alert_list_widget_all_of_active_within_dict = api_alert_list_widget_all_of_active_within_instance.to_dict()
# create an instance of ApiAlertListWidgetAllOfActiveWithin from a dict
api_alert_list_widget_all_of_active_within_from_dict = ApiAlertListWidgetAllOfActiveWithin.from_dict(api_alert_list_widget_all_of_active_within_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


