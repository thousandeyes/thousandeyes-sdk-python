# GetAgentsNotificationRules200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_alert_rules** | [**List[NotificationRule]**](NotificationRule.md) |  | [optional] 
**links** | [**SelfLinksLinks**](SelfLinksLinks.md) |  | [optional] 

## Example

```python
from agents_api.models.get_agents_notification_rules200_response import GetAgentsNotificationRules200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetAgentsNotificationRules200Response from a JSON string
get_agents_notification_rules200_response_instance = GetAgentsNotificationRules200Response.from_json(json)
# print the JSON string representation of the object
print GetAgentsNotificationRules200Response.to_json()

# convert the object into a dict
get_agents_notification_rules200_response_dict = get_agents_notification_rules200_response_instance.to_dict()
# create an instance of GetAgentsNotificationRules200Response from a dict
get_agents_notification_rules200_response_form_dict = get_agents_notification_rules200_response.from_dict(get_agents_notification_rules200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


