# NotificationThirdParty

Webhook notification.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**integration_id** | **str** | Integration ID. | [optional] 
**integration_type** | [**ThirdPartyIntegrationType**](ThirdPartyIntegrationType.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.alerts.models.notification_third_party import NotificationThirdParty

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationThirdParty from a JSON string
notification_third_party_instance = NotificationThirdParty.from_json(json)
# print the JSON string representation of the object
print(NotificationThirdParty.to_json())

# convert the object into a dict
notification_third_party_dict = notification_third_party_instance.to_dict()
# create an instance of NotificationThirdParty from a dict
notification_third_party_from_dict = NotificationThirdParty.from_dict(notification_third_party_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


