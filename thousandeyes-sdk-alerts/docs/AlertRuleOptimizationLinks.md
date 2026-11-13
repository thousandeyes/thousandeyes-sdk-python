# AlertRuleOptimizationLinks

Application link for the alert-rule optimization. When an optimization object is returned, `_links.appLink` and `_links.appLink.href` are required. MCP maps `_links.appLink.href` to `optimization.uiUrl`. This schema is optimization-specific so `appLink` can be required without changing shared `AppLinks`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_link** | [**Link**](Link.md) |  | 

## Example

```python
from thousandeyes_sdk.alerts.models.alert_rule_optimization_links import AlertRuleOptimizationLinks

# TODO update the JSON string below
json = "{}"
# create an instance of AlertRuleOptimizationLinks from a JSON string
alert_rule_optimization_links_instance = AlertRuleOptimizationLinks.from_json(json)
# print the JSON string representation of the object
print(AlertRuleOptimizationLinks.to_json())

# convert the object into a dict
alert_rule_optimization_links_dict = alert_rule_optimization_links_instance.to_dict()
# create an instance of AlertRuleOptimizationLinks from a dict
alert_rule_optimization_links_from_dict = AlertRuleOptimizationLinks.from_dict(alert_rule_optimization_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


