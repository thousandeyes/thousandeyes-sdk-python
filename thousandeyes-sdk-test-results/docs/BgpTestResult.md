# BgpTestResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **datetime** | Data point date UTC (ISO date-time format). | [optional] [readonly] 
**round_id** | **int** | Epoch time (seconds) indicating the start time of the round | [optional] [readonly] 
**links** | [**TestResultAppLinks**](TestResultAppLinks.md) |  | [optional] 
**monitor** | [**TestResultMonitor**](TestResultMonitor.md) |  | [optional] 
**prefix_id** | **str** | Internally tracked prefix ID. | [optional] 
**prefix** | **str** | Prefix being tracked. | [optional] 
**start_time** | **int** | Epoch time (seconds) indicating the start time of the round | [optional] [readonly] 
**end_time** | **int** | Epoch time (seconds) indicating the end time of the round | [optional] [readonly] 
**updates** | **float** | Number of updates tracked against this prefix by this monitor. | [optional] 
**path_changes** | **float** | Number of path changes tracked against this prefix by this monitor. | [optional] 
**reachability** | **float** | Percentage reachability | [optional] 

## Example

```python
from thousandeyes_sdk.test_results.models.bgp_test_result import BgpTestResult

# TODO update the JSON string below
json = "{}"
# create an instance of BgpTestResult from a JSON string
bgp_test_result_instance = BgpTestResult.from_json(json)
# print the JSON string representation of the object
print(BgpTestResult.to_json())

# convert the object into a dict
bgp_test_result_dict = bgp_test_result_instance.to_dict()
# create an instance of BgpTestResult from a dict
bgp_test_result_from_dict = BgpTestResult.from_dict(bgp_test_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


