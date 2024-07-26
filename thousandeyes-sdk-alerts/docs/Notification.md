# Notification

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
from thousandeyes_sdk.alerts.models.notification import Notification

# TODO update the JSON string below
json = "{}"
# create an instance of Notification from a JSON string
notification_instance = Notification.from_json(json)
# print the JSON string representation of the object
print(Notification.to_json())

# convert the object into a dict
notification_dict = notification_instance.to_dict()
# create an instance of Notification from a dict
notification_from_dict = Notification.from_dict(notification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


