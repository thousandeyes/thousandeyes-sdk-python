# FiltersAttributesExcludedAttributes

Attribute names to exclude. Values must match the stream's `signal` and `dataModelVersion`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from thousandeyes_sdk.streaming.models.filters_attributes_excluded_attributes import FiltersAttributesExcludedAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of FiltersAttributesExcludedAttributes from a JSON string
filters_attributes_excluded_attributes_instance = FiltersAttributesExcludedAttributes.from_json(json)
# print the JSON string representation of the object
print(FiltersAttributesExcludedAttributes.to_json())

# convert the object into a dict
filters_attributes_excluded_attributes_dict = filters_attributes_excluded_attributes_instance.to_dict()
# create an instance of FiltersAttributesExcludedAttributes from a dict
filters_attributes_excluded_attributes_from_dict = FiltersAttributesExcludedAttributes.from_dict(filters_attributes_excluded_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


