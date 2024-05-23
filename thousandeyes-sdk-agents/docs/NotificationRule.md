# NotificationRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rule_id** | **str** | Agent notification rule ID | [optional] [readonly] 
**rule_name** | **str** | Name of the agent notification rule | [optional] 
**expression** | **str** | Expression of agent notification rule | [optional] 
**notify_on_clear** | **bool** | Send notification when notification clears | [optional] 
**is_default** | **bool** | Agent notification rule will be automatically included on all new Enterprise Agents. | [optional] 

## Example

```python
from thousandeyes_sdk.agents.models.notification_rule import NotificationRule

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationRule from a JSON string
notification_rule_instance = NotificationRule.from_json(json)
# print the JSON string representation of the object
print(NotificationRule.to_json())

# convert the object into a dict
notification_rule_dict = notification_rule_instance.to_dict()
# create an instance of NotificationRule from a dict
notification_rule_from_dict = NotificationRule.from_dict(notification_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


