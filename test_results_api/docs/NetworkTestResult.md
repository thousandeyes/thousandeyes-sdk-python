# NetworkTestResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **datetime** | Data point date in UTC (ISO date-time format). | [optional] [readonly] 
**round_id** | **int** | Epoch time (seconds) indicating the start time of the round | [optional] [readonly] 
**links** | **object** |  | [optional] 
**start_time** | **int** | Epoch time (seconds) indicating the start time of the round | [optional] [readonly] 
**end_time** | **int** | Epoch time (seconds) indicating the end time of the round | [optional] [readonly] 
**available_bandwidth** | **float** |  | [optional] [readonly] 
**avg_latency** | **float** | Average RTT for packets sent to destination | [optional] [readonly] 
**bandwidth** | **float** |  | [optional] [readonly] 
**capacity** | **float** |  | [optional] [readonly] 
**jitter** | **float** | Standard deviation of latency | [optional] [readonly] 
**loss** | **float** | Percentage of packets not reaching destination | [optional] [readonly] 
**max_latency** | **float** | Maximum RTT for packets sent to destination | [optional] [readonly] 
**min_latency** | **float** | Minimum RTT for packets sent to destination | [optional] [readonly] 
**agent** | [**Agent**](Agent.md) |  | [optional] 
**server_ip** | **str** | IP of target server | [optional] [readonly] 
**server** | **str** | Target server, including port (if method used is TCP) | [optional] [readonly] 
**direction** | [**TestDirection**](TestDirection.md) |  | [optional] 

## Example

```python
from test_results_api.models.network_test_result import NetworkTestResult

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkTestResult from a JSON string
network_test_result_instance = NetworkTestResult.from_json(json)
# print the JSON string representation of the object
print NetworkTestResult.to_json()

# convert the object into a dict
network_test_result_dict = network_test_result_instance.to_dict()
# create an instance of NetworkTestResult from a dict
network_test_result_form_dict = network_test_result.from_dict(network_test_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


