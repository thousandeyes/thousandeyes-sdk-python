# NotificationWebhook

Webhook notification.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**integration_id** | **str** | Integration ID. | [optional] 
**integration_type** | [**WebhookIntegrationType**](WebhookIntegrationType.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.alerts.models.notification_webhook import NotificationWebhook

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationWebhook from a JSON string
notification_webhook_instance = NotificationWebhook.from_json(json)
# print the JSON string representation of the object
print(NotificationWebhook.to_json())

# convert the object into a dict
notification_webhook_dict = notification_webhook_instance.to_dict()
# create an instance of NotificationWebhook from a dict
notification_webhook_from_dict = NotificationWebhook.from_dict(notification_webhook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


