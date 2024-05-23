# ApiAgentStatusAgent

Agent shown in agent status widget.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_id** | **str** | Identifier of the agent. | [optional] 
**status** | [**EnterpriseAgentState**](EnterpriseAgentState.md) |  | [optional] 
**ip_info** | [**ApiAgentStatusIpInfo**](ApiAgentStatusIpInfo.md) |  | [optional] 
**agent_name** | **str** | Name of the agent | [optional] 
**location** | [**ApiAgentLocation**](ApiAgentLocation.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.dashboards.models.api_agent_status_agent import ApiAgentStatusAgent

# TODO update the JSON string below
json = "{}"
# create an instance of ApiAgentStatusAgent from a JSON string
api_agent_status_agent_instance = ApiAgentStatusAgent.from_json(json)
# print the JSON string representation of the object
print(ApiAgentStatusAgent.to_json())

# convert the object into a dict
api_agent_status_agent_dict = api_agent_status_agent_instance.to_dict()
# create an instance of ApiAgentStatusAgent from a dict
api_agent_status_agent_from_dict = ApiAgentStatusAgent.from_dict(api_agent_status_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


