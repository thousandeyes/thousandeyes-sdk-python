# EndpointAgent

The `EndpointAgent` object, which may include multiple clients.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique ID of endpoint agent, from &#x60;/endpoint/agents&#x60; endpoint. | [optional] [readonly] 
**aid** | **str** |  | [optional] 
**name** | **str** | The name of the agent. | [optional] 
**computer_name** | **str** |  | [optional] [readonly] 
**os_version** | **str** |  | [optional] [readonly] 
**platform** | [**Platform**](Platform.md) |  | [optional] 
**kernel_version** | **str** |  | [optional] [readonly] 
**manufacturer** | **str** |  | [optional] [readonly] 
**model** | **str** |  | [optional] [readonly] 
**last_seen** | **datetime** | The last time the agent checked-in. | [optional] [readonly] 
**status** | [**Status**](Status.md) |  | [optional] 
**deleted** | **bool** |  | [optional] [readonly] 
**version** | **str** | Version of the agent software running. | [optional] [readonly] 
**created_at** | **datetime** |  | [optional] [readonly] 
**number_of_clients** | **int** |  | [optional] [readonly] 
**public_ip** | **str** |  | [optional] [readonly] 
**location** | [**EndpointAgentLocation**](EndpointAgentLocation.md) |  | [optional] 
**clients** | [**List[EndpointClient]**](EndpointClient.md) | List of clients (user accounts) that the agent works with. Not populated by default.  | [optional] [readonly] 
**total_memory** | **str** |  | [optional] [readonly] 
**agent_type** | **str** |  | [optional] [readonly] 
**vpn_profiles** | [**List[EndpointVpnProfile]**](EndpointVpnProfile.md) | List of VPN connections on the agent. Not populated by default.  | [optional] [readonly] 
**network_interface_profiles** | [**List[InterfaceProfile]**](InterfaceProfile.md) | List of network interfaces on the agent. Not populated by default.  | [optional] [readonly] 
**asn_details** | [**EndpointAsnDetails**](EndpointAsnDetails.md) |  | [optional] 
**license_type** | [**AgentLicenseType**](AgentLicenseType.md) |  | [optional] 
**tcp_driver_available** | **bool** | Status of TCP test support on the agent. | [optional] [readonly] 
**npcap_version** | **str** | For Windows agents, the version of the NPCAP driver that the agent has loaded. | [optional] [readonly] 
**links** | [**SelfLinks**](SelfLinks.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_agents.models.endpoint_agent import EndpointAgent

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointAgent from a JSON string
endpoint_agent_instance = EndpointAgent.from_json(json)
# print the JSON string representation of the object
print(EndpointAgent.to_json())

# convert the object into a dict
endpoint_agent_dict = endpoint_agent_instance.to_dict()
# create an instance of EndpointAgent from a dict
endpoint_agent_from_dict = EndpointAgent.from_dict(endpoint_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


