# AlertRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rule_id** | **str** | Unique ID of the rule. | [optional] [readonly] 
**rule_name** | **str** | Name of the alert rule | [optional] [readonly] 
**expression** | **str** | String expression of alert rule | [optional] [readonly] 
**direction** | [**AlertDirection**](AlertDirection.md) |  | [optional] 
**is_default** | **bool** | Alert rules allow up to 1 alert rule to be selected as a default for each type. By checking the default option, this alert rule will be automatically included on subsequently created tests that test a metric used in alerting here | [optional] [readonly] 
**alert_type** | [**AlertType**](AlertType.md) |  | [optional] 
**minimum_sources** | **int** | The minimum number of agents or monitors that must meet the specified criteria in order to trigger the alert | [optional] [readonly] 
**minimum_sources_pct** | **int** | the minimum percentage of all assigned agents or monitors that must meet the specified criteria in order to trigger the alert | [optional] [readonly] 
**rounds_violating_mode** | [**AlertRoundsViolationMode**](AlertRoundsViolationMode.md) |  | [optional] 
**rounds_violating_out_of** | **int** | Specifies the divisor (y value) for the “X of Y times” condition. | [optional] [readonly] 
**rounds_violating_required** | **int** | Specifies the numerator (x value) for the “X of Y times” condition | [optional] [readonly] 
**sensitivity_level** | [**SensitivityLevel**](SensitivityLevel.md) |  | [optional] 
**severity** | [**Severity**](Severity.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.tests.models.alert_rule import AlertRule

# TODO update the JSON string below
json = "{}"
# create an instance of AlertRule from a JSON string
alert_rule_instance = AlertRule.from_json(json)
# print the JSON string representation of the object
print(AlertRule.to_json())

# convert the object into a dict
alert_rule_dict = alert_rule_instance.to_dict()
# create an instance of AlertRule from a dict
alert_rule_from_dict = AlertRule.from_dict(alert_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


