# FiltersMetrics

Excludes case-sensitive metric names for the stream's data model version. An empty list clears existing metric exclusions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**excluded_metrics** | [**FiltersMetricsExcludedMetrics**](FiltersMetricsExcludedMetrics.md) |  | 

## Example

```python
from thousandeyes_sdk.streaming.models.filters_metrics import FiltersMetrics

# TODO update the JSON string below
json = "{}"
# create an instance of FiltersMetrics from a JSON string
filters_metrics_instance = FiltersMetrics.from_json(json)
# print the JSON string representation of the object
print(FiltersMetrics.to_json())

# convert the object into a dict
filters_metrics_dict = filters_metrics_instance.to_dict()
# create an instance of FiltersMetrics from a dict
filters_metrics_from_dict = FiltersMetrics.from_dict(filters_metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


