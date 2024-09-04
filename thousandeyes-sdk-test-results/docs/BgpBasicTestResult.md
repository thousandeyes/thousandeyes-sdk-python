# BgpBasicTestResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **datetime** | Data point date UTC (ISO date-time format). | [optional] [readonly] 
**round_id** | **int** | Epoch time (seconds) indicating the start time of the round | [optional] [readonly] 
**links** | [**TestResultAppLinks**](TestResultAppLinks.md) |  | [optional] 
**monitor** | [**TestResultMonitor**](TestResultMonitor.md) |  | [optional] 
**prefix_id** | **str** | Internally tracked prefix ID. | [optional] 
**prefix** | **str** | Prefix being tracked. | [optional] 

## Example

```python
from thousandeyes_sdk.test_results.models.bgp_basic_test_result import BgpBasicTestResult

# TODO update the JSON string below
json = "{}"
# create an instance of BgpBasicTestResult from a JSON string
bgp_basic_test_result_instance = BgpBasicTestResult.from_json(json)
# print the JSON string representation of the object
print(BgpBasicTestResult.to_json())

# convert the object into a dict
bgp_basic_test_result_dict = bgp_basic_test_result_instance.to_dict()
# create an instance of BgpBasicTestResult from a dict
bgp_basic_test_result_from_dict = BgpBasicTestResult.from_dict(bgp_basic_test_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


