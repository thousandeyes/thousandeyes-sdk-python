# FiltersTestTypes

Test types that can be used for filtering data points.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[TestType]**](TestType.md) | A list of test types to filter data points. | [optional] 

## Example

```python
from thousandeyes_sdk.streaming.models.filters_test_types import FiltersTestTypes

# TODO update the JSON string below
json = "{}"
# create an instance of FiltersTestTypes from a JSON string
filters_test_types_instance = FiltersTestTypes.from_json(json)
# print the JSON string representation of the object
print(FiltersTestTypes.to_json())

# convert the object into a dict
filters_test_types_dict = filters_test_types_instance.to_dict()
# create an instance of FiltersTestTypes from a dict
filters_test_types_from_dict = FiltersTestTypes.from_dict(filters_test_types_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


