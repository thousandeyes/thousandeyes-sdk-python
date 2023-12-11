# Alert


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique ID for each individual alert occurrence. | [optional] [readonly] 
**alert_type** | [**AlertType**](AlertType.md) |  | [optional] 
**start_date** | **datetime** | The start date and time (in UTC, ISO 8601 format) for querying alerts. | [optional] [readonly] 
**end_date** | **datetime** | The end date and time (in UTC, ISO 8601 format) for querying alerts. | [optional] [readonly] 
**violation_count** | **int** | Number of sources that meet the alert criteria. | [optional] 
**duration** | **float** | Duration in seconds the alert was active | [optional] 
**links** | [**RuleLinksLinks**](RuleLinksLinks.md) |  | [optional] 
**alert_rule_id** | **str** | Unique ID of the rule. | [optional] [readonly] 
**alert_state** | [**State**](State.md) |  | [optional] 
**alert_severity** | [**Severity**](Severity.md) |  | [optional] 

## Example

```python
from alerts_api.models.alert import Alert

# TODO update the JSON string below
json = "{}"
# create an instance of Alert from a JSON string
alert_instance = Alert.from_json(json)
# print the JSON string representation of the object
print Alert.to_json()

# convert the object into a dict
alert_dict = alert_instance.to_dict()
# create an instance of Alert from a dict
alert_form_dict = alert.from_dict(alert_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


