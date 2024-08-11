# ApiAffectedTest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**test_id** | **str** | The ID of the affected test. | [optional] [readonly] 
**test_type** | [**TestType**](TestType.md) |  | [optional] 
**name** | **str** | The test name as configured in the test settings. | [optional] [readonly] 
**affected_target_ids** | **List[str]** | An array of unique target IDs contributed data points which generated the signal for the event. | [optional] 
**affected_agent_ids** | **List[str]** | An array of unique agent IDs that contributed data points which generated the signal for the event. | [optional] 
**links** | [**TestLinks**](TestLinks.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.event_detection.models.api_affected_test import ApiAffectedTest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiAffectedTest from a JSON string
api_affected_test_instance = ApiAffectedTest.from_json(json)
# print the JSON string representation of the object
print(ApiAffectedTest.to_json())

# convert the object into a dict
api_affected_test_dict = api_affected_test_instance.to_dict()
# create an instance of ApiAffectedTest from a dict
api_affected_test_from_dict = ApiAffectedTest.from_dict(api_affected_test_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


