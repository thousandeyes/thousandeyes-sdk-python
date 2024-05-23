# TestsDataThresholdFilters

All filters are applied based on the conditional operator (and/or).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | [**List[TestsDataThresholdFilter]**](TestsDataThresholdFilter.md) |  | [optional] 
**conditional_operator** | [**ConditionalOperator**](ConditionalOperator.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_test_results.models.tests_data_threshold_filters import TestsDataThresholdFilters

# TODO update the JSON string below
json = "{}"
# create an instance of TestsDataThresholdFilters from a JSON string
tests_data_threshold_filters_instance = TestsDataThresholdFilters.from_json(json)
# print the JSON string representation of the object
print(TestsDataThresholdFilters.to_json())

# convert the object into a dict
tests_data_threshold_filters_dict = tests_data_threshold_filters_instance.to_dict()
# create an instance of TestsDataThresholdFilters from a dict
tests_data_threshold_filters_from_dict = TestsDataThresholdFilters.from_dict(tests_data_threshold_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


