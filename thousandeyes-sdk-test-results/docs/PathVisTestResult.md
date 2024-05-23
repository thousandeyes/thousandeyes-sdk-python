# PathVisTestResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **datetime** | Data point date UTC (ISO date-time format). | [optional] [readonly] 
**round_id** | **int** | Epoch time (seconds) indicating the start time of the round | [optional] [readonly] 
**links** | [**TestResultAppLinks**](TestResultAppLinks.md) |  | [optional] 
**start_time** | **int** | Epoch time (seconds) indicating the start time of the round | [optional] [readonly] 
**end_time** | **int** | Epoch time (seconds) indicating the end time of the round | [optional] [readonly] 
**agent** | [**Agent**](Agent.md) |  | [optional] 
**server** | **str** | Target server, including port (if method used is TCP) | [optional] [readonly] 
**server_ip** | **str** | IP of target server | [optional] [readonly] 
**source_ip** | **str** | IP address of source agent | [optional] [readonly] 
**source_prefix** | **str** | IP prefix of source agent | [optional] [readonly] 
**target_is_proxy** | **bool** | Specifies whether the traces are targeting a proxy. If not set, it is considered as false. | [optional] [readonly] 
**direction** | [**PathVisDirection**](PathVisDirection.md) |  | [optional] 
**path_traces** | [**List[PathVisEndpoint]**](PathVisEndpoint.md) | Shows all iterations of path trace, with each iteration specified by a pathId | [optional] 

## Example

```python
from thousandeyes_sdk.test_results.models.path_vis_test_result import PathVisTestResult

# TODO update the JSON string below
json = "{}"
# create an instance of PathVisTestResult from a JSON string
path_vis_test_result_instance = PathVisTestResult.from_json(json)
# print the JSON string representation of the object
print(PathVisTestResult.to_json())

# convert the object into a dict
path_vis_test_result_dict = path_vis_test_result_instance.to_dict()
# create an instance of PathVisTestResult from a dict
path_vis_test_result_from_dict = PathVisTestResult.from_dict(path_vis_test_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


