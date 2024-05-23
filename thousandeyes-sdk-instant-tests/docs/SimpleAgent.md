# SimpleAgent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip_addresses** | **List[str]** | Array of private IP addresses. | [optional] [readonly] 
**public_ip_addresses** | **List[str]** | Array of public IP addresses. | [optional] [readonly] 
**network** | **str** | Network (including ASN) of agent’s public IP. | [optional] [readonly] 
**agent_id** | **str** | Unique ID of the agent. | [optional] [readonly] 
**agent_name** | **str** | Name of the agent. | [optional] 
**location** | **str** | Location of the agent. | [optional] [readonly] 
**country_id** | **str** | 2-digit ISO country code | [optional] [readonly] 
**enabled** | **bool** | Flag indicating if the agent is enabled. | [optional] 
**prefix** | **str** | Prefix containing agents public IP address. | [optional] [readonly] 
**verify_ssl_certificates** | **bool** | Flag indicating if has normal SSL operations or  if instead it&#39;s set to ignore SSL errors on browserbot-based tests. | [optional] [readonly] 

## Example

```python
from thousandeyes_sdk.instant_tests.models.simple_agent import SimpleAgent

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleAgent from a JSON string
simple_agent_instance = SimpleAgent.from_json(json)
# print the JSON string representation of the object
print(SimpleAgent.to_json())

# convert the object into a dict
simple_agent_dict = simple_agent_instance.to_dict()
# create an instance of SimpleAgent from a dict
simple_agent_from_dict = SimpleAgent.from_dict(simple_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


