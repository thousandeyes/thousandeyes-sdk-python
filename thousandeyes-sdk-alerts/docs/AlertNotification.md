# AlertNotification

Alert notification object. See Alert notification integrations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | [**NotificationEmail**](NotificationEmail.md) |  | [optional] 
**third_party** | [**List[NotificationThirdParty]**](NotificationThirdParty.md) | Third party notifications. | [optional] 
**webhook** | [**List[NotificationWebhook]**](NotificationWebhook.md) | Webhook notifications. | [optional] 
**custom_webhook** | [**List[NotificationCustomWebhook]**](NotificationCustomWebhook.md) | Custom webhook notifications. | [optional] 

## Example

```python
from thousandeyes_sdk.alerts.models.alert_notification import AlertNotification

# TODO update the JSON string below
json = "{}"
# create an instance of AlertNotification from a JSON string
alert_notification_instance = AlertNotification.from_json(json)
# print the JSON string representation of the object
print(AlertNotification.to_json())

# convert the object into a dict
alert_notification_dict = alert_notification_instance.to_dict()
# create an instance of AlertNotification from a dict
alert_notification_from_dict = AlertNotification.from_dict(alert_notification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


