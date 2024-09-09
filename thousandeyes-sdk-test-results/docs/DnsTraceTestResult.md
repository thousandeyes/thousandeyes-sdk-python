# DnsTraceTestResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **datetime** | Data point date UTC (ISO date-time format). | [optional] [readonly] 
**round_id** | **int** | Epoch time (seconds) indicating the start time of the round | [optional] [readonly] 
**links** | [**TestResultAppLinks**](TestResultAppLinks.md) |  | [optional] 
**start_time** | **int** | Epoch time (seconds) indicating the start time of the round | [optional] [readonly] 
**end_time** | **int** | Epoch time (seconds) indicating the end time of the round | [optional] [readonly] 
**agent** | [**TestResultAgent**](TestResultAgent.md) |  | [optional] 
**output** | **str** | Verbose output from the trace request | [optional] [readonly] 
**error_details** | **str** | Error details, if an error were encountered | [optional] [readonly] 
**queries** | **int** | How many queries were required to get to the requested result | [optional] [readonly] 
**failed_queries** | **int** | How many queries failed while getting to the requested result | [optional] [readonly] 
**final_server_queried** | **str** | DNS server that provided the final result | [optional] [readonly] 
**final_query_time** | **int** | How long the final query took to return a response | [optional] [readonly] 
**mappings** | **str** | Final mappings returned from the request | [optional] [readonly] 

## Example

```python
from thousandeyes_sdk.test_results.models.dns_trace_test_result import DnsTraceTestResult

# TODO update the JSON string below
json = "{}"
# create an instance of DnsTraceTestResult from a JSON string
dns_trace_test_result_instance = DnsTraceTestResult.from_json(json)
# print the JSON string representation of the object
print(DnsTraceTestResult.to_json())

# convert the object into a dict
dns_trace_test_result_dict = dns_trace_test_result_instance.to_dict()
# create an instance of DnsTraceTestResult from a dict
dns_trace_test_result_from_dict = DnsTraceTestResult.from_dict(dns_trace_test_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


