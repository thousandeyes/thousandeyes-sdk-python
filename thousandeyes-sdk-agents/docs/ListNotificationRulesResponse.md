# ListNotificationRulesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_alert_rules** | [**List[NotificationRule]**](NotificationRule.md) |  | [optional] 
**links** | [**SelfLinks**](SelfLinks.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.agents.models.list_notification_rules_response import ListNotificationRulesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListNotificationRulesResponse from a JSON string
list_notification_rules_response_instance = ListNotificationRulesResponse.from_json(json)
# print the JSON string representation of the object
print(ListNotificationRulesResponse.to_json())

# convert the object into a dict
list_notification_rules_response_dict = list_notification_rules_response_instance.to_dict()
# create an instance of ListNotificationRulesResponse from a dict
list_notification_rules_response_from_dict = ListNotificationRulesResponse.from_dict(list_notification_rules_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


