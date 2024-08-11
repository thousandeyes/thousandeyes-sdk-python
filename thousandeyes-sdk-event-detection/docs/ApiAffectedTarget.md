# ApiAffectedTarget


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**server_id** | **str** | The ID of the target server. | [optional] [readonly] 
**name** | **str** | The target name as configured in the test settings. | [optional] [readonly] 
**ip** | **str** | The target server IP resolved by the agent. Depending on the failure type, the IP may not be present. For example, if the agent failed to resolve it or if the requests were routed through the proxy. | [optional] [readonly] 
**affected_test_ids** | **List[str]** | An array of unique test IDs that contributed data points which generated the signal for the event. | [optional] 
**affected_agent_ids** | **List[str]** | An array of unique agent IDs that contributed data points which generated the signal for the event. | [optional] 

## Example

```python
from thousandeyes_sdk.event_detection.models.api_affected_target import ApiAffectedTarget

# TODO update the JSON string below
json = "{}"
# create an instance of ApiAffectedTarget from a JSON string
api_affected_target_instance = ApiAffectedTarget.from_json(json)
# print the JSON string representation of the object
print(ApiAffectedTarget.to_json())

# convert the object into a dict
api_affected_target_dict = api_affected_target_instance.to_dict()
# create an instance of ApiAffectedTarget from a dict
api_affected_target_from_dict = ApiAffectedTarget.from_dict(api_affected_target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


