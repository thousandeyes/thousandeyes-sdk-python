# AgentProxy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aid** | **str** | Account id that this proxy configuration belongs to | [optional] 
**auth_type** | [**ProxyAuthType**](ProxyAuthType.md) |  | [optional] 
**bypass_list** | **List[str]** | A list of hostnames, network prefixes, or wildcards used to determine which test targets should not be proxied. If all tests should be proxied, leave empty. | [optional] 
**last_modified** | **datetime** | Last modification timestamp of the proxy. Expressed in UTC (ISO date-time format). | [optional] 
**location** | **str** | The location of the proxy. If proxyType is &#x60;static&#x60; use the format &#x60;hostname:port&#x60;. If location is &#x60;pac&#x60;, then specify the URL where the PAC file can be obtained. | [optional] 
**is_local_configured** | **bool** | Set to &#x60;true&#x60; if this proxy configuration comes from the agent’s config file. Specify &#x60;false&#x60; if the proxy configuration was created in the ThousandEyes application. | [optional] 
**name** | **str** | Expression of agent notification rule. | [optional] 
**password** | **str** | Password for proxy authentication | [optional] 
**proxy_id** | **str** | Agent proxy&#39;s unique ID. | [optional] 
**type** | [**ProxyType**](ProxyType.md) |  | [optional] 
**user** | **str** | Username for proxy authentication. | [optional] 

## Example

```python
from thousandeyes_sdk.agents.models.agent_proxy import AgentProxy

# TODO update the JSON string below
json = "{}"
# create an instance of AgentProxy from a JSON string
agent_proxy_instance = AgentProxy.from_json(json)
# print the JSON string representation of the object
print(AgentProxy.to_json())

# convert the object into a dict
agent_proxy_dict = agent_proxy_instance.to_dict()
# create an instance of AgentProxy from a dict
agent_proxy_from_dict = AgentProxy.from_dict(agent_proxy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


