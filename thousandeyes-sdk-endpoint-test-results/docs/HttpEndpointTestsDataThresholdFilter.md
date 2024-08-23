# HttpEndpointTestsDataThresholdFilter

The metric is filtered based on the threshold value and operator provided.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | [**HttpThresholdFilterName**](HttpThresholdFilterName.md) |  | [optional] 
**value** | **float** | The threshold value. | [optional] 
**operator** | [**ThresholdFilterOperator**](ThresholdFilterOperator.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_test_results.models.http_endpoint_tests_data_threshold_filter import HttpEndpointTestsDataThresholdFilter

# TODO update the JSON string below
json = "{}"
# create an instance of HttpEndpointTestsDataThresholdFilter from a JSON string
http_endpoint_tests_data_threshold_filter_instance = HttpEndpointTestsDataThresholdFilter.from_json(json)
# print the JSON string representation of the object
print(HttpEndpointTestsDataThresholdFilter.to_json())

# convert the object into a dict
http_endpoint_tests_data_threshold_filter_dict = http_endpoint_tests_data_threshold_filter_instance.to_dict()
# create an instance of HttpEndpointTestsDataThresholdFilter from a dict
http_endpoint_tests_data_threshold_filter_from_dict = HttpEndpointTestsDataThresholdFilter.from_dict(http_endpoint_tests_data_threshold_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


