# AgentBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip_addresses** | **List[str]** | Array of private IP addresses. | [optional] [readonly] 
**public_ip_addresses** | **List[str]** | Array of public IP addresses. | [optional] [readonly] 
**network** | **str** | Network (including ASN) of agent’s public IP. | [optional] [readonly] 

## Example

```python
from thousandeyes_sdk.administrative.models.agent_base import AgentBase

# TODO update the JSON string below
json = "{}"
# create an instance of AgentBase from a JSON string
agent_base_instance = AgentBase.from_json(json)
# print the JSON string representation of the object
print(AgentBase.to_json())

# convert the object into a dict
agent_base_dict = agent_base_instance.to_dict()
# create an instance of AgentBase from a dict
agent_base_from_dict = AgentBase.from_dict(agent_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


