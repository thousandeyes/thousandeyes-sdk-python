# AgentExplainabilityFailure

A machine-readable explanation for an endpoint agent collection failure.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason_code** | **str** | Failure reason reported by the agent. New reason codes may be introduced over time. | 

## Example

```python
from thousandeyes_sdk.endpoint_agents.models.agent_explainability_failure import AgentExplainabilityFailure

# TODO update the JSON string below
json = "{}"
# create an instance of AgentExplainabilityFailure from a JSON string
agent_explainability_failure_instance = AgentExplainabilityFailure.from_json(json)
# print the JSON string representation of the object
print(AgentExplainabilityFailure.to_json())

# convert the object into a dict
agent_explainability_failure_dict = agent_explainability_failure_instance.to_dict()
# create an instance of AgentExplainabilityFailure from a dict
agent_explainability_failure_from_dict = AgentExplainabilityFailure.from_dict(agent_explainability_failure_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


