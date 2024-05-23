# SimpleTest

Each test includes additional fields depending on its `type`. Refer `/tests/{type}` endpoint to know the set of fields returned by a given `type`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interval** | [**TestInterval**](TestInterval.md) |  | [optional] 
**alerts_enabled** | **bool** | Indicates if alerts are enabled. | [optional] 
**enabled** | **bool** | Test is enabled. | [optional] [default to True]
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
from thousandeyes_sdk.tests.models.simple_test import SimpleTest

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleTest from a JSON string
simple_test_instance = SimpleTest.from_json(json)
# print the JSON string representation of the object
print(SimpleTest.to_json())

# convert the object into a dict
simple_test_dict = simple_test_instance.to_dict()
# create an instance of SimpleTest from a dict
simple_test_from_dict = SimpleTest.from_dict(simple_test_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


