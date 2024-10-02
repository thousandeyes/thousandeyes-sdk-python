# Filters

Provides the ability to filter data points based on the specified test types.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**test_types** | [**FiltersTestTypes**](FiltersTestTypes.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.streaming.models.filters import Filters

# TODO update the JSON string below
json = "{}"
# create an instance of Filters from a JSON string
filters_instance = Filters.from_json(json)
# print the JSON string representation of the object
print(Filters.to_json())

# convert the object into a dict
filters_dict = filters_instance.to_dict()
# create an instance of Filters from a dict
filters_from_dict = Filters.from_dict(filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


