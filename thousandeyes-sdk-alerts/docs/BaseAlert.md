# BaseAlert


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique ID for each individual alert occurrence. | [optional] [readonly] 
**alert_type** | [**AlertType**](AlertType.md) |  | [optional] 
**start_date** | **datetime** | The start date and time (in UTC, ISO 8601 format) for querying alerts. | [optional] [readonly] 
**end_date** | **datetime** | The end date and time (in UTC, ISO 8601 format) for querying alerts. | [optional] [readonly] 
**violation_count** | **int** | Number of sources that meet the alert criteria. | [optional] 
**duration** | **int** | Duration in seconds the alert was active | [optional] 
**suppressed** | **bool** | Indicates whether the alert is currently suppressed by a real-time ASW. | [optional] 
**meta** | [**AlertMeta**](AlertMeta.md) |  | [optional] 
**links** | [**AlertLinks**](AlertLinks.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.alerts.models.base_alert import BaseAlert

# TODO update the JSON string below
json = "{}"
# create an instance of BaseAlert from a JSON string
base_alert_instance = BaseAlert.from_json(json)
# print the JSON string representation of the object
print(BaseAlert.to_json())

# convert the object into a dict
base_alert_dict = base_alert_instance.to_dict()
# create an instance of BaseAlert from a dict
base_alert_from_dict = BaseAlert.from_dict(base_alert_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


