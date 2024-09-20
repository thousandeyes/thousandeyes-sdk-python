# AgentNotification

Alert notification object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | [**AlertEmail**](AlertEmail.md) |  | [optional] 
**third_party** | [**List[AlertIntegrationBase]**](AlertIntegrationBase.md) |  | [optional] 
**webhook** | [**List[AlertIntegrationBase]**](AlertIntegrationBase.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.agents.models.agent_notification import AgentNotification

# TODO update the JSON string below
json = "{}"
# create an instance of AgentNotification from a JSON string
agent_notification_instance = AgentNotification.from_json(json)
# print the JSON string representation of the object
print(AgentNotification.to_json())

# convert the object into a dict
agent_notification_dict = agent_notification_instance.to_dict()
# create an instance of AgentNotification from a dict
agent_notification_from_dict = AgentNotification.from_dict(agent_notification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


