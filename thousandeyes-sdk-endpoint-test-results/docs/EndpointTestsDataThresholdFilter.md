# EndpointTestsDataThresholdFilter

The metric is filtered based on the threshold value and operator provided.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | [**ThresholdFilterName**](ThresholdFilterName.md) |  | [optional] 
**value** | **float** | The threshold value. | [optional] 
**operator** | [**ThresholdFilterOperator**](ThresholdFilterOperator.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_test_results.models.endpoint_tests_data_threshold_filter import EndpointTestsDataThresholdFilter

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointTestsDataThresholdFilter from a JSON string
endpoint_tests_data_threshold_filter_instance = EndpointTestsDataThresholdFilter.from_json(json)
# print the JSON string representation of the object
print(EndpointTestsDataThresholdFilter.to_json())

# convert the object into a dict
endpoint_tests_data_threshold_filter_dict = endpoint_tests_data_threshold_filter_instance.to_dict()
# create an instance of EndpointTestsDataThresholdFilter from a dict
endpoint_tests_data_threshold_filter_from_dict = EndpointTestsDataThresholdFilter.from_dict(endpoint_tests_data_threshold_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


