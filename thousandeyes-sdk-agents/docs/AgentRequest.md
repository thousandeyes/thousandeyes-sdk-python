# AgentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_name** | **str** | Name of the agent. | [optional] 
**enabled** | **bool** | Flag indicating if the agent is enabled. | [optional] 
**account_groups** | **List[str]** | Contains a list of account groups IDs. See &#x60;/accounts-groups&#x60; for a list of account IDs | [optional] 
**ipv6_policy** | [**AgentIpv6Policy**](AgentIpv6Policy.md) |  | [optional] 
**keep_browser_cache** | **bool** | Flag indicating if the agent retains cache. | [optional] 
**target_for_tests** | **str** | Test target IP address. | [optional] 
**local_resolution_prefixes** | **List[str]** | Public IP ranges for rDNS lookups. The range must be in CIDR notation; for example, 10.1.1.0/24. Maximum of 5 prefixes allowed (Enterprise Agents and Enterprise Agent clusters only). | [optional] 
**tests** | **List[str]** | Contains list of test IDs. See &#x60;/tests&#x60; to pull a list of available tests. | [optional] 

## Example

```python
from thousandeyes_sdk.agents.models.agent_request import AgentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AgentRequest from a JSON string
agent_request_instance = AgentRequest.from_json(json)
# print the JSON string representation of the object
print(AgentRequest.to_json())

# convert the object into a dict
agent_request_dict = agent_request_instance.to_dict()
# create an instance of AgentRequest from a dict
agent_request_from_dict = AgentRequest.from_dict(agent_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


