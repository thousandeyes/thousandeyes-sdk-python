# EnterpriseAgentClusterDetail


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
**tests** | [**List[SimpleTest]**](SimpleTest.md) | List of tests. See &#x60;/tests&#x60; for more information. | [optional] 
**notification_rules** | [**List[NotificationRules]**](NotificationRules.md) | List of notification rule objects configured on agent | [optional] 
**labels** | [**List[AgentLabel]**](AgentLabel.md) | List of labels. See &#x60;/labels&#x60; for more information. | [optional] [readonly] 
**agent_type** | **str** | Enterprise Cluster agent type. | 
**links** | [**SelfLinks**](SelfLinks.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.agents.models.enterprise_agent_cluster_detail import EnterpriseAgentClusterDetail

# TODO update the JSON string below
json = "{}"
# create an instance of EnterpriseAgentClusterDetail from a JSON string
enterprise_agent_cluster_detail_instance = EnterpriseAgentClusterDetail.from_json(json)
# print the JSON string representation of the object
print(EnterpriseAgentClusterDetail.to_json())

# convert the object into a dict
enterprise_agent_cluster_detail_dict = enterprise_agent_cluster_detail_instance.to_dict()
# create an instance of EnterpriseAgentClusterDetail from a dict
enterprise_agent_cluster_detail_from_dict = EnterpriseAgentClusterDetail.from_dict(enterprise_agent_cluster_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


