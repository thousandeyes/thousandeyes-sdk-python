# ApiAgentStatusIpInfo

IP information of the agent.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**public_ip** | **str** | Public IP of the agent. | [optional] 
**private_ip** | **str** | Private IP of the agent. | [optional] 
**ipv6** | **str** |  | [optional] 
**operative_system_version** | **str** |  | [optional] 

## Example

```python
from thousandeyes_sdk.dashboards.models.api_agent_status_ip_info import ApiAgentStatusIpInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ApiAgentStatusIpInfo from a JSON string
api_agent_status_ip_info_instance = ApiAgentStatusIpInfo.from_json(json)
# print the JSON string representation of the object
print(ApiAgentStatusIpInfo.to_json())

# convert the object into a dict
api_agent_status_ip_info_dict = api_agent_status_ip_info_instance.to_dict()
# create an instance of ApiAgentStatusIpInfo from a dict
api_agent_status_ip_info_from_dict = ApiAgentStatusIpInfo.from_dict(api_agent_status_ip_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


