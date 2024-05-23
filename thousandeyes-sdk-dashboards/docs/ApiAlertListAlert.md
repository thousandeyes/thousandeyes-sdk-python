# ApiAlertListAlert

Alert shown in the alert list widget.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alert_id** | **str** | Identifier of the alert. | [optional] 
**test_id** | **str** | Identifier of the test. | [optional] 
**rule_id** | **str** | Identifier of the rule. | [optional] 
**alert_source** | **str** | Name of the agent, monitor or device producing the alert. | [optional] 
**alert_rule** | **str** | Name of the alert rule that this alert belongs to. | [optional] 
**alert_type** | [**AlertListAlertType**](AlertListAlertType.md) |  | [optional] 
**start_time** | **datetime** | UTC date when the alert was first active. | [optional] 
**duration_in_seconds** | **int** | Number of seconds the alert was active. If it’s still active, this number will increase every second. | [optional] 
**active** | **bool** | Set to &#x60;true&#x60; if alert is active, &#x60;false&#x60; otherwise. | [optional] 

## Example

```python
from thousandeyes_sdk.dashboards.models.api_alert_list_alert import ApiAlertListAlert

# TODO update the JSON string below
json = "{}"
# create an instance of ApiAlertListAlert from a JSON string
api_alert_list_alert_instance = ApiAlertListAlert.from_json(json)
# print the JSON string representation of the object
print(ApiAlertListAlert.to_json())

# convert the object into a dict
api_alert_list_alert_dict = api_alert_list_alert_instance.to_dict()
# create an instance of ApiAlertListAlert from a dict
api_alert_list_alert_from_dict = ApiAlertListAlert.from_dict(api_alert_list_alert_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


