# CloudAgentDetail


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
**agent_type** | **str** | Cloud agent type. | 
**tests** | [**List[SimpleTest]**](SimpleTest.md) | List of tests. See &#x60;/tests&#x60; for more information. | [optional] 
**labels** | [**List[AgentLabel]**](AgentLabel.md) | List of labels - see &#x60;/labels&#x60; for more information. | [optional] [readonly] 
**links** | [**SelfLinks**](SelfLinks.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.agents.models.cloud_agent_detail import CloudAgentDetail

# TODO update the JSON string below
json = "{}"
# create an instance of CloudAgentDetail from a JSON string
cloud_agent_detail_instance = CloudAgentDetail.from_json(json)
# print the JSON string representation of the object
print(CloudAgentDetail.to_json())

# convert the object into a dict
cloud_agent_detail_dict = cloud_agent_detail_instance.to_dict()
# create an instance of CloudAgentDetail from a dict
cloud_agent_detail_from_dict = CloudAgentDetail.from_dict(cloud_agent_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


