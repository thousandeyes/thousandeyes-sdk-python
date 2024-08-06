# HttpTestsDataThresholdFilters

All filters are applied based on the conditional operator (and/or).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | [**List[HttpTestsDataThresholdFilter]**](HttpTestsDataThresholdFilter.md) |  | [optional] 
**conditional_operator** | [**ConditionalOperator**](ConditionalOperator.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_test_results.models.http_tests_data_threshold_filters import HttpTestsDataThresholdFilters

# TODO update the JSON string below
json = "{}"
# create an instance of HttpTestsDataThresholdFilters from a JSON string
http_tests_data_threshold_filters_instance = HttpTestsDataThresholdFilters.from_json(json)
# print the JSON string representation of the object
print(HttpTestsDataThresholdFilters.to_json())

# convert the object into a dict
http_tests_data_threshold_filters_dict = http_tests_data_threshold_filters_instance.to_dict()
# create an instance of HttpTestsDataThresholdFilters from a dict
http_tests_data_threshold_filters_from_dict = HttpTestsDataThresholdFilters.from_dict(http_tests_data_threshold_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


