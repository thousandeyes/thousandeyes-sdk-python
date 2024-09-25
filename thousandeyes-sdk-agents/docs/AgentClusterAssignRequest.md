# AgentClusterAssignRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agents** | **List[str]** | Contains list of agent IDs (get &#x60;agentId&#x60; from &#x60;/agents&#x60; operation) | [optional] 

## Example

```python
from thousandeyes_sdk.agents.models.agent_cluster_assign_request import AgentClusterAssignRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AgentClusterAssignRequest from a JSON string
agent_cluster_assign_request_instance = AgentClusterAssignRequest.from_json(json)
# print the JSON string representation of the object
print(AgentClusterAssignRequest.to_json())

# convert the object into a dict
agent_cluster_assign_request_dict = agent_cluster_assign_request_instance.to_dict()
# create an instance of AgentClusterAssignRequest from a dict
agent_cluster_assign_request_from_dict = AgentClusterAssignRequest.from_dict(agent_cluster_assign_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


