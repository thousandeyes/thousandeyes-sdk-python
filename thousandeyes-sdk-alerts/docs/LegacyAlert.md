# LegacyAlert


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alert_id** | **str** | A unique ID for each individual alert occurrence. | [optional] [readonly] 
**date_start** | **str** | The start date and time for querying alerts. | [optional] [readonly] 
**date_end** | **str** | The end date and time for querying alerts. | [optional] [readonly] 
**rule_id** | **int** | Unique ID of the rule. | [optional] [readonly] 
**state** | **str** | Current state of the alert. Possible values: clear or trigger. | [optional] [readonly] 
**severity** | **str** | The severity of the alert. | [optional] 
**permalink** | **str** | Hyperlink to alerts list, with row expanded | [optional] 
**api_links** | **List[Dict[str, object]]** | List of hyperlinks to other areas of the API | [optional] 

## Example

```python
from thousandeyes_sdk.alerts.models.legacy_alert import LegacyAlert

# TODO update the JSON string below
json = "{}"
# create an instance of LegacyAlert from a JSON string
legacy_alert_instance = LegacyAlert.from_json(json)
# print the JSON string representation of the object
print(LegacyAlert.to_json())

# convert the object into a dict
legacy_alert_dict = legacy_alert_instance.to_dict()
# create an instance of LegacyAlert from a dict
legacy_alert_from_dict = LegacyAlert.from_dict(legacy_alert_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


