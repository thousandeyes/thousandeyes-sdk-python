# EnterpriseAgentResponseExpands


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tests** | [**List[SimpleTest]**](SimpleTest.md) | List of tests. See &#x60;/tests&#x60; for more information. | [optional] 
**notification_rules** | [**List[NotificationRules]**](NotificationRules.md) | List of notification rule objects configured on agent | [optional] 
**labels** | [**List[AgentLabel]**](AgentLabel.md) | List of labels. See &#x60;/labels&#x60; for more information. | [optional] [readonly] 

## Example

```python
from thousandeyes_sdk.agents.models.enterprise_agent_response_expands import EnterpriseAgentResponseExpands

# TODO update the JSON string below
json = "{}"
# create an instance of EnterpriseAgentResponseExpands from a JSON string
enterprise_agent_response_expands_instance = EnterpriseAgentResponseExpands.from_json(json)
# print the JSON string representation of the object
print(EnterpriseAgentResponseExpands.to_json())

# convert the object into a dict
enterprise_agent_response_expands_dict = enterprise_agent_response_expands_instance.to_dict()
# create an instance of EnterpriseAgentResponseExpands from a dict
enterprise_agent_response_expands_from_dict = EnterpriseAgentResponseExpands.from_dict(enterprise_agent_response_expands_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


