# BaseRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rule_id** | **str** | Unique ID of the rule. | [optional] [readonly] 
**rule_name** | **str** | Name of the alert rule. | 
**expression** | **str** | The expression of the alert rule. | 
**direction** | [**AlertDirection**](AlertDirection.md) |  | [optional] 
**notify_on_clear** | **bool** | Send notification when alert clears. | [optional] 
**is_default** | **bool** | If set to &#x60;true&#x60;, this alert rule becomes the default for its test type and is automatically applied to newly created tests with relevant metrics. Only one default alert rule is allowed per test type. | [optional] 
**alert_type** | [**AlertType**](AlertType.md) |  | 
**minimum_sources** | **int** | The minimum number of agents or monitors that must meet the specified criteria to trigger the alert. | [optional] 
**minimum_sources_pct** | **int** | The minimum percentage of all assigned agents or monitors that must meet the specified criteria to trigger the alert. | [optional] 
**rounds_violating_mode** | [**AlertRoundsViolationMode**](AlertRoundsViolationMode.md) |  | [optional] 
**rounds_violating_out_of** | **int** | Specifies the divisor (y value) in the “X of Y times” condition. | 
**rounds_violating_required** | **int** | Specifies the numerator (x value) in the “X of Y times” condition. | 
**include_covered_prefixes** | **bool** | Set true to include covered prefixes in the BGP alert rule. Only applicable to BGP alert rules. | [optional] 
**sensitivity_level** | [**SensitivityLevel**](SensitivityLevel.md) |  | [optional] 
**severity** | [**Severity**](Severity.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.alerts.models.base_rule import BaseRule

# TODO update the JSON string below
json = "{}"
# create an instance of BaseRule from a JSON string
base_rule_instance = BaseRule.from_json(json)
# print the JSON string representation of the object
print(BaseRule.to_json())

# convert the object into a dict
base_rule_dict = base_rule_instance.to_dict()
# create an instance of BaseRule from a dict
base_rule_from_dict = BaseRule.from_dict(base_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


