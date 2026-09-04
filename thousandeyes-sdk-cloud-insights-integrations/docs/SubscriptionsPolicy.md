# SubscriptionsPolicy

Policy document that controls which Azure subscriptions are inventoried. Up to 10 rules can be provided. Rules are evaluated in order; if none match, the defaultAction is applied. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rules** | [**List[SubscriptionsPolicyRule]**](SubscriptionsPolicyRule.md) | Ordered list of subscription policy rules. Maximum of 10 entries. | 
**default_action** | [**SubscriptionsPolicyRuleAction**](SubscriptionsPolicyRuleAction.md) |  | 

## Example

```python
from thousandeyes_sdk.cloud_insights_integrations.models.subscriptions_policy import SubscriptionsPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionsPolicy from a JSON string
subscriptions_policy_instance = SubscriptionsPolicy.from_json(json)
# print the JSON string representation of the object
print(SubscriptionsPolicy.to_json())

# convert the object into a dict
subscriptions_policy_dict = subscriptions_policy_instance.to_dict()
# create an instance of SubscriptionsPolicy from a dict
subscriptions_policy_from_dict = SubscriptionsPolicy.from_dict(subscriptions_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


