# UnexpandedInstantTest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_by** | **str** | User that created the test. | [optional] [readonly] 
**created_date** | **datetime** | UTC created date (ISO date-time format). | [optional] [readonly] 
**description** | **str** | A description of the test. | [optional] 
**live_share** | **bool** | Indicates if the test is shared with the account group. | [optional] [readonly] 
**modified_by** | **str** | User that modified the test. | [optional] [readonly] 
**modified_date** | **datetime** | UTC last modification date (ISO date-time format). | [optional] [readonly] 
**saved_event** | **bool** | Indicates if the test is a saved event. | [optional] [readonly] 
**test_id** | **str** | Each test is assigned an unique ID; this is used to access test information and results from other endpoints. | [optional] [readonly] 
**test_name** | **str** | The name of the test. Test name must be unique. | [optional] 
**type** | [**TestType**](TestType.md) |  | [optional] 
**links** | [**TestLinks**](TestLinks.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.instant_tests.models.unexpanded_instant_test import UnexpandedInstantTest

# TODO update the JSON string below
json = "{}"
# create an instance of UnexpandedInstantTest from a JSON string
unexpanded_instant_test_instance = UnexpandedInstantTest.from_json(json)
# print the JSON string representation of the object
print(UnexpandedInstantTest.to_json())

# convert the object into a dict
unexpanded_instant_test_dict = unexpanded_instant_test_instance.to_dict()
# create an instance of UnexpandedInstantTest from a dict
unexpanded_instant_test_from_dict = UnexpandedInstantTest.from_dict(unexpanded_instant_test_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


