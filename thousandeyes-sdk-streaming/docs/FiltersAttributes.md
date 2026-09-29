# FiltersAttributes

Excludes case-sensitive attribute names for the stream's signal and data model version. An empty list clears existing attribute exclusions.  Reserved attributes are always emitted and cannot be excluded:  - `v1`: `account.id`, `thousandeyes.data.version`, and `thousandeyes.stream.id` - `v2`: `thousandeyes.account.id`, `thousandeyes.data.version`, and `thousandeyes.stream.id` 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**excluded_attributes** | [**FiltersAttributesExcludedAttributes**](FiltersAttributesExcludedAttributes.md) |  | 

## Example

```python
from thousandeyes_sdk.streaming.models.filters_attributes import FiltersAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of FiltersAttributes from a JSON string
filters_attributes_instance = FiltersAttributes.from_json(json)
# print the JSON string representation of the object
print(FiltersAttributes.to_json())

# convert the object into a dict
filters_attributes_dict = filters_attributes_instance.to_dict()
# create an instance of FiltersAttributes from a dict
filters_attributes_from_dict = FiltersAttributes.from_dict(filters_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


