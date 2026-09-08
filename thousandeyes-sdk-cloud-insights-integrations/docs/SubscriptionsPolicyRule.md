# SubscriptionsPolicyRule

A single subscription rule consisting of a field, pattern, and action.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | [**SubscriptionsPolicyRuleField**](SubscriptionsPolicyRuleField.md) |  | 
**pattern** | **str** | String or regular expression used to match subscription identifiers or names. | 
**action** | [**SubscriptionsPolicyRuleAction**](SubscriptionsPolicyRuleAction.md) |  | 

## Example

```python
from thousandeyes_sdk.cloud_insights_integrations.models.subscriptions_policy_rule import SubscriptionsPolicyRule

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionsPolicyRule from a JSON string
subscriptions_policy_rule_instance = SubscriptionsPolicyRule.from_json(json)
# print the JSON string representation of the object
print(SubscriptionsPolicyRule.to_json())

# convert the object into a dict
subscriptions_policy_rule_dict = subscriptions_policy_rule_instance.to_dict()
# create an instance of SubscriptionsPolicyRule from a dict
subscriptions_policy_rule_from_dict = SubscriptionsPolicyRule.from_dict(subscriptions_policy_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


