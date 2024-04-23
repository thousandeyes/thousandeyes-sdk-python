# GetAgentProxies200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_proxies** | [**List[AgentProxy]**](AgentProxy.md) |  | [optional] 
**links** | [**SelfLinksLinks**](SelfLinksLinks.md) |  | [optional] 

## Example

```python
from agents.models.get_agent_proxies200_response import GetAgentProxies200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetAgentProxies200Response from a JSON string
get_agent_proxies200_response_instance = GetAgentProxies200Response.from_json(json)
# print the JSON string representation of the object
print(GetAgentProxies200Response.to_json())

# convert the object into a dict
get_agent_proxies200_response_dict = get_agent_proxies200_response_instance.to_dict()
# create an instance of GetAgentProxies200Response from a dict
get_agent_proxies200_response_from_dict = GetAgentProxies200Response.from_dict(get_agent_proxies200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


