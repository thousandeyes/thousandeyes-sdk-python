# AgentProxies


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_proxies** | [**List[AgentProxy]**](AgentProxy.md) |  | [optional] 
**links** | [**SelfLinks**](SelfLinks.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.agents.models.agent_proxies import AgentProxies

# TODO update the JSON string below
json = "{}"
# create an instance of AgentProxies from a JSON string
agent_proxies_instance = AgentProxies.from_json(json)
# print the JSON string representation of the object
print(AgentProxies.to_json())

# convert the object into a dict
agent_proxies_dict = agent_proxies_instance.to_dict()
# create an instance of AgentProxies from a dict
agent_proxies_from_dict = AgentProxies.from_dict(agent_proxies_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


