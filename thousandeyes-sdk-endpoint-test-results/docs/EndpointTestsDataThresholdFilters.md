# EndpointTestsDataThresholdFilters

All filters are applied based on the conditional operator (and/or).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | [**List[EndpointTestsDataThresholdFilter]**](EndpointTestsDataThresholdFilter.md) |  | [optional] 
**conditional_operator** | [**ConditionalOperator**](ConditionalOperator.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_test_results.models.endpoint_tests_data_threshold_filters import EndpointTestsDataThresholdFilters

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointTestsDataThresholdFilters from a JSON string
endpoint_tests_data_threshold_filters_instance = EndpointTestsDataThresholdFilters.from_json(json)
# print the JSON string representation of the object
print(EndpointTestsDataThresholdFilters.to_json())

# convert the object into a dict
endpoint_tests_data_threshold_filters_dict = endpoint_tests_data_threshold_filters_instance.to_dict()
# create an instance of EndpointTestsDataThresholdFilters from a dict
endpoint_tests_data_threshold_filters_from_dict = EndpointTestsDataThresholdFilters.from_dict(endpoint_tests_data_threshold_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


