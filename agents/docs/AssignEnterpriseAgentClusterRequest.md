# AssignEnterpriseAgentClusterRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agents** | **List[str]** | Contains list of agent IDs (get &#x60;agentId&#x60; from &#x60;/agents&#x60; endpoint) | [optional] 

## Example

```python
from agents.models.assign_enterprise_agent_cluster_request import AssignEnterpriseAgentClusterRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AssignEnterpriseAgentClusterRequest from a JSON string
assign_enterprise_agent_cluster_request_instance = AssignEnterpriseAgentClusterRequest.from_json(json)
# print the JSON string representation of the object
print(AssignEnterpriseAgentClusterRequest.to_json())

# convert the object into a dict
assign_enterprise_agent_cluster_request_dict = assign_enterprise_agent_cluster_request_instance.to_dict()
# create an instance of AssignEnterpriseAgentClusterRequest from a dict
assign_enterprise_agent_cluster_request_from_dict = AssignEnterpriseAgentClusterRequest.from_dict(assign_enterprise_agent_cluster_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


