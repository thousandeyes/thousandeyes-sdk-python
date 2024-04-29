# UnassignEnterpriseAgentFromClusterRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**members** | **List[str]** | Contains list of member IDs. (get &#x60;memberId&#x60; from &#x60;/agents/{agentId}&#x60; endpoint) | [optional] 

## Example

```python
from agents.models.unassign_enterprise_agent_from_cluster_request import UnassignEnterpriseAgentFromClusterRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UnassignEnterpriseAgentFromClusterRequest from a JSON string
unassign_enterprise_agent_from_cluster_request_instance = UnassignEnterpriseAgentFromClusterRequest.from_json(json)
# print the JSON string representation of the object
print(UnassignEnterpriseAgentFromClusterRequest.to_json())

# convert the object into a dict
unassign_enterprise_agent_from_cluster_request_dict = unassign_enterprise_agent_from_cluster_request_instance.to_dict()
# create an instance of UnassignEnterpriseAgentFromClusterRequest from a dict
unassign_enterprise_agent_from_cluster_request_from_dict = UnassignEnterpriseAgentFromClusterRequest.from_dict(unassign_enterprise_agent_from_cluster_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


