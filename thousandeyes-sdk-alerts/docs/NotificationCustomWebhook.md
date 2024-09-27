# NotificationCustomWebhook

Custom webhook notification.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**integration_id** | **str** | Integration ID. | [optional] 
**integration_type** | [**CustomWebhookIntegrationType**](CustomWebhookIntegrationType.md) |  | [optional] 
**integration_name** | **str** | User-configured name of the integration. | [optional] 
**target** | **str** | Webhook target URL. | [optional] 

## Example

```python
from thousandeyes_sdk.alerts.models.notification_custom_webhook import NotificationCustomWebhook

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationCustomWebhook from a JSON string
notification_custom_webhook_instance = NotificationCustomWebhook.from_json(json)
# print the JSON string representation of the object
print(NotificationCustomWebhook.to_json())

# convert the object into a dict
notification_custom_webhook_dict = notification_custom_webhook_instance.to_dict()
# create an instance of NotificationCustomWebhook from a dict
notification_custom_webhook_from_dict = NotificationCustomWebhook.from_dict(notification_custom_webhook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


