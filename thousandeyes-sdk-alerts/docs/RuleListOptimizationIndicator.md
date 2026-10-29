# RuleListOptimizationIndicator

Response-only optimization presence indicator for alert-rule list rows.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_optimization** | **bool** | Indicates whether the authorized optimization lookup found an active optimization for this rule. &#x60;true&#x60; means the lookup completed and an active optimization exists. &#x60;false&#x60; means the lookup completed and no active optimization exists. If this field is omitted, optimization enrichment could not be completed and the absence must not be interpreted as &#x60;false&#x60;. This field is not nullable; its three states are &#x60;true&#x60;, &#x60;false&#x60;, or absent. | [optional] [readonly] 

## Example

```python
from thousandeyes_sdk.alerts.models.rule_list_optimization_indicator import RuleListOptimizationIndicator

# TODO update the JSON string below
json = "{}"
# create an instance of RuleListOptimizationIndicator from a JSON string
rule_list_optimization_indicator_instance = RuleListOptimizationIndicator.from_json(json)
# print the JSON string representation of the object
print(RuleListOptimizationIndicator.to_json())

# convert the object into a dict
rule_list_optimization_indicator_dict = rule_list_optimization_indicator_instance.to_dict()
# create an instance of RuleListOptimizationIndicator from a dict
rule_list_optimization_indicator_from_dict = RuleListOptimizationIndicator.from_dict(rule_list_optimization_indicator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


