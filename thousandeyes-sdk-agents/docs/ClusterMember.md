# ClusterMember


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip_addresses** | **List[str]** | Array of private IP addresses. | [optional] [readonly] 
**public_ip_addresses** | **List[str]** | Array of public IP addresses. | [optional] [readonly] 
**network** | **str** | Network (including ASN) of agent’s public IP. | [optional] [readonly] 
**member_id** | **str** | Unique ID of the cluster member | [optional] [readonly] 
**name** | **str** | Name of the cluster member | [optional] [readonly] 
**error_details** | [**List[ErrorDetail]**](ErrorDetail.md) | If an enterprise agent or a cluster member presents at least one error, the errors will be shown as an array of entries in the errorDetails field (Enterprise Agents and Enterprise Cluster members only) | [optional] [readonly] 
**last_seen** | **datetime** | UTC last seen date (ISO date-time format). | [optional] [readonly] 
**agent_state** | [**EnterpriseAgentState**](EnterpriseAgentState.md) |  | [optional] 
**target_for_tests** | **str** | Test target IP address. | [optional] 
**utilization** | **int** | Shows overall utilization percentage (online Enterprise Agents and Enterprise Clusters only). | [optional] [readonly] 

## Example

```python
from thousandeyes_sdk.agents.models.cluster_member import ClusterMember

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterMember from a JSON string
cluster_member_instance = ClusterMember.from_json(json)
# print the JSON string representation of the object
print(ClusterMember.to_json())

# convert the object into a dict
cluster_member_dict = cluster_member_instance.to_dict()
# create an instance of ClusterMember from a dict
cluster_member_from_dict = ClusterMember.from_dict(cluster_member_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


