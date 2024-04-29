# UnitsByTests


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**breakdowns** | [**List[UnitsByTestsBreakdownsInner]**](UnitsByTestsBreakdownsInner.md) |  | [optional] 

## Example

```python
from usage.models.units_by_tests import UnitsByTests

# TODO update the JSON string below
json = "{}"
# create an instance of UnitsByTests from a JSON string
units_by_tests_instance = UnitsByTests.from_json(json)
# print the JSON string representation of the object
print(UnitsByTests.to_json())

# convert the object into a dict
units_by_tests_dict = units_by_tests_instance.to_dict()
# create an instance of UnitsByTests from a dict
units_by_tests_from_dict = UnitsByTests.from_dict(units_by_tests_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


