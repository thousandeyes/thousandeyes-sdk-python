# NotificationEmail

Email notifications.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recipients** | **List[str]** | An array containing the email addresses to receive notifications. | [optional] 
**message** | **str** | Custom text included in alert email notifications sent to recipients. | [optional] 

## Example

```python
from thousandeyes_sdk.alerts.models.notification_email import NotificationEmail

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationEmail from a JSON string
notification_email_instance = NotificationEmail.from_json(json)
# print the JSON string representation of the object
print(NotificationEmail.to_json())

# convert the object into a dict
notification_email_dict = notification_email_instance.to_dict()
# create an instance of NotificationEmail from a dict
notification_email_from_dict = NotificationEmail.from_dict(notification_email_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


