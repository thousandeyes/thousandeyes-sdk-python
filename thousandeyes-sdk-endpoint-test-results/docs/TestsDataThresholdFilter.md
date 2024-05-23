# TestsDataThresholdFilter

The metric is filtered based on the threshold value and operator provided.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | [**ThresholdFilterName**](ThresholdFilterName.md) |  | [optional] 
**value** | **float** | The threshold value. | [optional] 
**operator** | [**ThresholdFilterOperator**](ThresholdFilterOperator.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_test_results.models.tests_data_threshold_filter import TestsDataThresholdFilter

# TODO update the JSON string below
json = "{}"
# create an instance of TestsDataThresholdFilter from a JSON string
tests_data_threshold_filter_instance = TestsDataThresholdFilter.from_json(json)
# print the JSON string representation of the object
print(TestsDataThresholdFilter.to_json())

# convert the object into a dict
tests_data_threshold_filter_dict = tests_data_threshold_filter_instance.to_dict()
# create an instance of TestsDataThresholdFilter from a dict
tests_data_threshold_filter_from_dict = TestsDataThresholdFilter.from_dict(tests_data_threshold_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


