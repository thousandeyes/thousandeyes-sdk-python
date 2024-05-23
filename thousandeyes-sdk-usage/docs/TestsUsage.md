# TestsUsage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**breakdowns** | [**List[UnitsByTests]**](UnitsByTests.md) |  | [optional] 
**links** | [**PaginationLinks**](PaginationLinks.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.usage.models.tests_usage import TestsUsage

# TODO update the JSON string below
json = "{}"
# create an instance of TestsUsage from a JSON string
tests_usage_instance = TestsUsage.from_json(json)
# print the JSON string representation of the object
print(TestsUsage.to_json())

# convert the object into a dict
tests_usage_dict = tests_usage_instance.to_dict()
# create an instance of TestsUsage from a dict
tests_usage_from_dict = TestsUsage.from_dict(tests_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


