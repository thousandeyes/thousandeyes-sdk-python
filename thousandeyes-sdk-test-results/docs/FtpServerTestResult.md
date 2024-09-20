# FtpServerTestResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **datetime** | Data point date UTC (ISO date-time format). | [optional] [readonly] 
**round_id** | **int** | Epoch time (seconds) indicating the start time of the round | [optional] [readonly] 
**links** | [**TestResultAppLinks**](TestResultAppLinks.md) |  | [optional] 
**start_time** | **int** | Epoch time (seconds) indicating the start time of the round | [optional] [readonly] 
**end_time** | **int** | Epoch time (seconds) indicating the end time of the round | [optional] [readonly] 
**agent** | [**TestResultAgent**](TestResultAgent.md) |  | [optional] 
**server_ip** | **str** | IP address of destination server | [optional] [readonly] 
**response_code** | **int** | FTP response code | [optional] [readonly] 
**dns_time** | **float** | Time required to resolve DNS  in milliseconds | [optional] [readonly] 
**connect_time** | **float** | Time required to establish a TCP connection to the server in milliseconds | [optional] [readonly] 
**negotiation_time** | **float** | Time negotiate the connection and authenticate with the destination server in milliseconds | [optional] [readonly] 
**wait_time** | **float** | Time elapsed between completion of request and first byte of response in milliseconds | [optional] [readonly] 
**response_time** | **float** | Sum of DNS, connect, negotiation and wait times in milliseconds | [optional] [readonly] 
**transfer_time** | **float** | Elapsed time between first and last byte of the transfer in milliseconds | [optional] [readonly] 
**wire_size** | **int** | Size of content in bytes | [optional] [readonly] 
**total_time** | **float** | Sum of response + transfer time in milliseconds | [optional] [readonly] 
**error_type** | **str** | Type of error encountered; corresponds to phase of connection | [optional] [readonly] 
**error_details** | **str** | Error details, if an error were encountered | [optional] [readonly] 
**throughput** | **int** | WireSize divided by receiveTime in byter per second | [optional] [readonly] 

## Example

```python
from thousandeyes_sdk.test_results.models.ftp_server_test_result import FtpServerTestResult

# TODO update the JSON string below
json = "{}"
# create an instance of FtpServerTestResult from a JSON string
ftp_server_test_result_instance = FtpServerTestResult.from_json(json)
# print the JSON string representation of the object
print(FtpServerTestResult.to_json())

# convert the object into a dict
ftp_server_test_result_dict = ftp_server_test_result_instance.to_dict()
# create an instance of FtpServerTestResult from a dict
ftp_server_test_result_from_dict = FtpServerTestResult.from_dict(ftp_server_test_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


