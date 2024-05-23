# ApiAgentStatusSummary

Summary of the agent status.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**online** | **int** | Shows the number of agents with an online status. | [optional] 
**offline** | **int** | Shows the number of agents with an offline status. | [optional] 
**disabled** | **int** | Shows the number of agents with disabled status. | [optional] 

## Example

```python
from thousandeyes_sdk.dashboards.models.api_agent_status_summary import ApiAgentStatusSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ApiAgentStatusSummary from a JSON string
api_agent_status_summary_instance = ApiAgentStatusSummary.from_json(json)
# print the JSON string representation of the object
print(ApiAgentStatusSummary.to_json())

# convert the object into a dict
api_agent_status_summary_dict = api_agent_status_summary_instance.to_dict()
# create an instance of ApiAgentStatusSummary from a dict
api_agent_status_summary_from_dict = ApiAgentStatusSummary.from_dict(api_agent_status_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


