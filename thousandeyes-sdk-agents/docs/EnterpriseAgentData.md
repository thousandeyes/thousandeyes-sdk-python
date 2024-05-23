# EnterpriseAgentData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_members** | [**List[ClusterMember]**](ClusterMember.md) | If an enterprise agent is clustered, detailed information about each cluster member will be shown as array entries in the clusterMembers field. This field is not shown for Enterprise Agents in standalone mode, or for Cloud Agents. | [optional] [readonly] 
**utilization** | **int** | Shows overall utilization percentage (online Enterprise Agents and Enterprise Clusters only). | [optional] [readonly] 
**account_groups** | [**List[AccountGroup]**](AccountGroup.md) | List of account groups. See /accounts-groups to pull a list of account IDs | [optional] 
**ipv6_policy** | [**EnterpriseAgentIpv6Policy**](EnterpriseAgentIpv6Policy.md) |  | [optional] 
**error_details** | [**List[ErrorDetail]**](ErrorDetail.md) | If an enterprise agent or a cluster member presents at least one error, the errors will be shown as an array of entries in the errorDetails field (Enterprise Agents and Enterprise Cluster members only) | [optional] [readonly] 
**hostname** | **str** | Fully qualified domain name of the agent (Enterprise Agents only) | [optional] [readonly] 
**last_seen** | **datetime** | UTC last seen date (ISO date-time format). | [optional] [readonly] 
**agent_state** | [**EnterpriseAgentState**](EnterpriseAgentState.md) |  | [optional] 
**keep_browser_cache** | **bool** | Flag indicating if the agent retains cache. | [optional] 
**created_date** | **datetime** | UTC Agent creation date (ISO date-time format). | [optional] [readonly] 
**target_for_tests** | **str** | Test target IP address. | [optional] 
**local_resolution_prefixes** | **List[str]** | To perform rDNS lookups for public IP ranges, this field represents the public IP ranges. The range must be in CIDR notation; for example, 10.1.1.0/24. Maximum of 5 prefixes allowed (Enterprise Agents and Enterprise Agent clusters only). | [optional] 
**interface_ip_mappings** | [**List[InterfaceIpMapping]**](InterfaceIpMapping.md) |  | [optional] [readonly] 

## Example

```python
from thousandeyes_sdk.agents.models.enterprise_agent_data import EnterpriseAgentData

# TODO update the JSON string below
json = "{}"
# create an instance of EnterpriseAgentData from a JSON string
enterprise_agent_data_instance = EnterpriseAgentData.from_json(json)
# print the JSON string representation of the object
print(EnterpriseAgentData.to_json())

# convert the object into a dict
enterprise_agent_data_dict = enterprise_agent_data_instance.to_dict()
# create an instance of EnterpriseAgentData from a dict
enterprise_agent_data_from_dict = EnterpriseAgentData.from_dict(enterprise_agent_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


