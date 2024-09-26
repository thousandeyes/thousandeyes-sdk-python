# AgentClusterUnassignRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**members** | **List[str]** | Contains list of member IDs. (get &#x60;memberId&#x60; from &#x60;/agents/{agentId}&#x60; operation) | [optional] 

## Example

```python
from thousandeyes_sdk.agents.models.agent_cluster_unassign_request import AgentClusterUnassignRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AgentClusterUnassignRequest from a JSON string
agent_cluster_unassign_request_instance = AgentClusterUnassignRequest.from_json(json)
# print the JSON string representation of the object
print(AgentClusterUnassignRequest.to_json())

# convert the object into a dict
agent_cluster_unassign_request_dict = agent_cluster_unassign_request_instance.to_dict()
# create an instance of AgentClusterUnassignRequest from a dict
agent_cluster_unassign_request_from_dict = AgentClusterUnassignRequest.from_dict(agent_cluster_unassign_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


