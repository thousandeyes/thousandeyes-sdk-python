# Filters

Controls which test data the integration exports.  `testTypes` is an inclusion filter: when specified, only data from the selected test types is included. `metricsFilter` and `attributesFilter` exclude metrics or attributes from the included data.  Filter support depends on the stream's signal and data model version:  - For `metric` streams using data model `v1` or `v2`, both   `metricsFilter` and `attributesFilter` are supported. - For `log` and `trace` streams using data model `v2`, only   `attributesFilter` is supported. `metricsFilter` is not supported.  On create, an omitted `testTypes` filter includes all test types, while omitted exclusion filters exclude nothing. On update, each omitted filter remains unchanged. Empty exclusion lists clear existing exclusions; `testTypes.values` must not be empty. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**test_types** | [**FiltersTestTypes**](FiltersTestTypes.md) |  | [optional] 
**metrics_filter** | [**FiltersMetrics**](FiltersMetrics.md) |  | [optional] 
**attributes_filter** | [**FiltersAttributes**](FiltersAttributes.md) |  | [optional] 

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


