# SipServerTestResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **datetime** | Data point date UTC (ISO date-time format). | [optional] [readonly] 
**round_id** | **int** | Epoch time (seconds) indicating the start time of the round | [optional] [readonly] 
**links** | [**TestResultAppLinks**](TestResultAppLinks.md) |  | [optional] 
**start_time** | **int** | Epoch time (seconds) indicating the start time of the round | [optional] [readonly] 
**end_time** | **int** | Epoch time (seconds) indicating the end time of the round | [optional] [readonly] 
**server_ip** | **str** | Target agent IP address | [optional] [readonly] 
**agent** | [**TestResultAgent**](TestResultAgent.md) |  | [optional] 
**availability** | **float** | availability of the service | [optional] [readonly] 
**connect_time** | **int** | Time required to establish a TCP connection to the server in milliseconds, only available when TCP is configured as protocol | [optional] [readonly] 
**dns_time** | **int** | Time required to resolve DNS in milliseconds | [optional] [readonly] 
**invite_time** | **int** | Time to complete INVITE in milliseconds | [optional] [readonly] 
**options_time** | **int** | Time to complete OPTIONS in milliseconds | [optional] [readonly] 
**num_redirects** | **int** | Number of redirects | [optional] [readonly] 
**options_request** | **str** | Entire OPTIONS request | [optional] [readonly] 
**options_response** | **str** | Entire OPTIONS response | [optional] [readonly] 
**register_time** | **int** | Time to complete REGISTER in milliseconds | [optional] [readonly] 
**response_code** | **int** | SIP server response code | [optional] [readonly] 
**response_time** | **int** | Time to first byte | [optional] [readonly] 
**total_time** | **int** | Total time | [optional] [readonly] 
**wait_time** | **int** | Time elapsed between completion of request and first byte of response | [optional] [readonly] 
**error_type** | [**SipServerErrorType**](SipServerErrorType.md) |  | [optional] 
**problem_detail** | **str** | Error details, if an error was encountered | [optional] [readonly] 

## Example

```python
from thousandeyes_sdk.test_results.models.sip_server_test_result import SipServerTestResult

# TODO update the JSON string below
json = "{}"
# create an instance of SipServerTestResult from a JSON string
sip_server_test_result_instance = SipServerTestResult.from_json(json)
# print the JSON string representation of the object
print(SipServerTestResult.to_json())

# convert the object into a dict
sip_server_test_result_dict = sip_server_test_result_instance.to_dict()
# create an instance of SipServerTestResult from a dict
sip_server_test_result_from_dict = SipServerTestResult.from_dict(sip_server_test_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


