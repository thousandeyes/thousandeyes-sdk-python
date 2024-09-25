# EventApiAffectedTest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**test_id** | **str** | The ID of the affected test. | [optional] [readonly] 
**test_type** | [**TestType**](TestType.md) |  | [optional] 
**name** | **str** | The test name as configured in the test settings. | [optional] [readonly] 
**affected_target_ids** | **List[str]** | An array of unique target IDs contributed data points which generated the signal for the event. | [optional] 
**affected_agent_ids** | **List[str]** | An array of unique agent IDs that contributed data points which generated the signal for the event. | [optional] 
**links** | [**EventTestLinks**](EventTestLinks.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.event_detection.models.event_api_affected_test import EventApiAffectedTest

# TODO update the JSON string below
json = "{}"
# create an instance of EventApiAffectedTest from a JSON string
event_api_affected_test_instance = EventApiAffectedTest.from_json(json)
# print the JSON string representation of the object
print(EventApiAffectedTest.to_json())

# convert the object into a dict
event_api_affected_test_dict = event_api_affected_test_instance.to_dict()
# create an instance of EventApiAffectedTest from a dict
event_api_affected_test_from_dict = EventApiAffectedTest.from_dict(event_api_affected_test_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


