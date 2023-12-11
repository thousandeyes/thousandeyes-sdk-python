# GetAgentsNotificationRule200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rule_id** | **str** | Agent notification rule ID | [optional] [readonly] 
**rule_name** | **str** | Name of the agent notification rule | [optional] 
**expression** | **str** | Expression of agent notification rule | [optional] 
**notify_on_clear** | **bool** | Send notification when notification clears | [optional] 
**is_default** | **bool** | Agent notification rule will be automatically included on all new Enterprise Agents. | [optional] 
**agents** | [**List[Agent]**](Agent.md) |  | [optional] 
**notifications** | [**Notification**](Notification.md) |  | [optional] 
**links** | [**SelfLinksLinks**](SelfLinksLinks.md) |  | [optional] 

## Example

```python
from agents_api.models.get_agents_notification_rule200_response import GetAgentsNotificationRule200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetAgentsNotificationRule200Response from a JSON string
get_agents_notification_rule200_response_instance = GetAgentsNotificationRule200Response.from_json(json)
# print the JSON string representation of the object
print GetAgentsNotificationRule200Response.to_json()

# convert the object into a dict
get_agents_notification_rule200_response_dict = get_agents_notification_rule200_response_instance.to_dict()
# create an instance of GetAgentsNotificationRule200Response from a dict
get_agents_notification_rule200_response_form_dict = get_agents_notification_rule200_response.from_dict(get_agents_notification_rule200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


