# AgentBranchEventGrouping


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asn** | **int** | AS number of the agent&#39;s network (for agent-branch events). | [optional] [readonly] 
**asn_city** | **str** | City associated with the agent&#39;s AS (for agent-branch events). | [optional] [readonly] 

## Example

```python
from thousandeyes_sdk.event_detection.models.agent_branch_event_grouping import AgentBranchEventGrouping

# TODO update the JSON string below
json = "{}"
# create an instance of AgentBranchEventGrouping from a JSON string
agent_branch_event_grouping_instance = AgentBranchEventGrouping.from_json(json)
# print the JSON string representation of the object
print(AgentBranchEventGrouping.to_json())

# convert the object into a dict
agent_branch_event_grouping_dict = agent_branch_event_grouping_instance.to_dict()
# create an instance of AgentBranchEventGrouping from a dict
agent_branch_event_grouping_from_dict = AgentBranchEventGrouping.from_dict(agent_branch_event_grouping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


