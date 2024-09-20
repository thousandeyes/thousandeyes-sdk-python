# NetworkTestResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **datetime** | Data point date in UTC (ISO date-time format). | [optional] [readonly] 
**round_id** | **int** | Epoch time (seconds) indicating the start time of the round | [optional] [readonly] 
**links** | [**TestResultAppLinks**](TestResultAppLinks.md) |  | [optional] 
**start_time** | **int** | Epoch time (seconds) indicating the start time of the round | [optional] [readonly] 
**end_time** | **int** | Epoch time (seconds) indicating the end time of the round | [optional] [readonly] 
**available_bandwidth** | **float** | The bandwidth from the client to the server measured in Mbps. This value is not available if bandwidth testing is disabled, if no value could be calculated, or if the target is a proxy. | [optional] [readonly] 
**avg_latency** | **float** | Average RTT for packets sent to destination | [optional] [readonly] 
**bandwidth** | **float** |  | [optional] [readonly] 
**capacity** | **float** | The capacity from the client to the server measured in Mbps. This value is not available if bandwidth testing is disabled, if no value could be calculated, or if the target is a proxy. | [optional] [readonly] 
**jitter** | **float** | Standard deviation of latency | [optional] [readonly] 
**loss** | **float** | Percentage of packets not reaching destination | [optional] [readonly] 
**max_latency** | **float** | Maximum RTT for packets sent to destination | [optional] [readonly] 
**min_latency** | **float** | Minimum RTT for packets sent to destination | [optional] [readonly] 
**packets_by_second** | **List[List[int]]** | Number of packets sent and received in a second. | [optional] [readonly] 
**agent** | [**TestResultAgent**](TestResultAgent.md) |  | [optional] 
**server_ip** | **str** | IP of target server | [optional] [readonly] 
**server** | **str** | Target server, including port (if method used is TCP) | [optional] [readonly] 
**health_score** | **float** | A normalized value (0.0-1.0) representing the network connection health of the test target. Returns negative values as error codes. -1.0 indicates there was insufficient data to calculate the health score. | [optional] 
**direction** | [**TestDirection**](TestDirection.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.test_results.models.network_test_result import NetworkTestResult

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkTestResult from a JSON string
network_test_result_instance = NetworkTestResult.from_json(json)
# print the JSON string representation of the object
print(NetworkTestResult.to_json())

# convert the object into a dict
network_test_result_dict = network_test_result_instance.to_dict()
# create an instance of NetworkTestResult from a dict
network_test_result_from_dict = NetworkTestResult.from_dict(network_test_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


