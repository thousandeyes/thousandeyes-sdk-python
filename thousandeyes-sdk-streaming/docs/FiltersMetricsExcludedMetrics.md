# FiltersMetricsExcludedMetrics

Metric names to exclude. Values must match the stream's `dataModelVersion`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from thousandeyes_sdk.streaming.models.filters_metrics_excluded_metrics import FiltersMetricsExcludedMetrics

# TODO update the JSON string below
json = "{}"
# create an instance of FiltersMetricsExcludedMetrics from a JSON string
filters_metrics_excluded_metrics_instance = FiltersMetricsExcludedMetrics.from_json(json)
# print the JSON string representation of the object
print(FiltersMetricsExcludedMetrics.to_json())

# convert the object into a dict
filters_metrics_excluded_metrics_dict = filters_metrics_excluded_metrics_instance.to_dict()
# create an instance of FiltersMetricsExcludedMetrics from a dict
filters_metrics_excluded_metrics_from_dict = FiltersMetricsExcludedMetrics.from_dict(filters_metrics_excluded_metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


