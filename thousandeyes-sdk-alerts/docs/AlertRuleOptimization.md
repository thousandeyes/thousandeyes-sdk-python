# AlertRuleOptimization

A read-only, system-generated optimization recommendation for an alert rule. A rule has at most one active optimization at a time. An object means an authorized lookup found an active optimization. Explicit `null` means the lookup completed and no active optimization exists. If this field is omitted from the parent alert-rule detail, enrichment could not be completed and the absence must not be interpreted as no optimization.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique optimization ID. | [readonly] 
**title** | **str** | Short, human-readable title for the optimization. | [readonly] 
**rationale** | **str** | Explanation of why the alert rule is a candidate for optimization. | [readonly] 
**type** | [**OptimizationType**](OptimizationType.md) |  | 
**status** | [**OptimizationStatus**](OptimizationStatus.md) |  | 
**confidence** | [**OptimizationConfidence**](OptimizationConfidence.md) |  | 
**created_date** | **datetime** | UTC date and time when the optimization was created, in RFC 3339 format. | [readonly] 
**updated_date** | **datetime** | UTC date and time when the optimization was last updated, in RFC 3339 format. | [readonly] 
**links** | [**AlertRuleOptimizationLinks**](AlertRuleOptimizationLinks.md) |  | 

## Example

```python
from thousandeyes_sdk.alerts.models.alert_rule_optimization import AlertRuleOptimization

# TODO update the JSON string below
json = "{}"
# create an instance of AlertRuleOptimization from a JSON string
alert_rule_optimization_instance = AlertRuleOptimization.from_json(json)
# print the JSON string representation of the object
print(AlertRuleOptimization.to_json())

# convert the object into a dict
alert_rule_optimization_dict = alert_rule_optimization_instance.to_dict()
# create an instance of AlertRuleOptimization from a dict
alert_rule_optimization_from_dict = AlertRuleOptimization.from_dict(alert_rule_optimization_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


