# HttpTestResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aid** | **str** | A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. | [optional] 
**agent_id** | **str** | Unique ID of endpoint agent, from &#x60;/endpoint/agents&#x60; endpoint. | [optional] [readonly] 
**round_id** | **int** | Epoch time (seconds) indicating the start time of the round. | [optional] [readonly] 
**server_ip** | **str** | IP address of destination server. | [optional] [readonly] 
**network_profile** | [**NetworkProfile**](NetworkProfile.md) |  | [optional] 
**system_metrics** | [**SystemMetrics**](SystemMetrics.md) |  | [optional] 
**original_target_profile** | [**TargetProfile**](TargetProfile.md) |  | [optional] 
**vpn_profile** | [**VpnProfile**](VpnProfile.md) |  | [optional] 
**connect_time** | **int** | Time required to establish a TCP connection to the server in milliseconds. | [optional] [readonly] 
**dns_time** | **int** | Time required to resolve DNS in milliseconds. | [optional] [readonly] 
**error_type** | [**HttpErrorType**](HttpErrorType.md) |  | [optional] 
**error_details** | **str** | Error details, if an error were encountered. | [optional] [readonly] 
**headers** | [**HttpTestResultHeaders**](HttpTestResultHeaders.md) |  | [optional] 
**num_redirects** | **int** | Number of redirects. | [optional] [readonly] 
**receive_time** | **int** | Elapsed time between first and last byte of response in milliseconds. | [optional] [readonly] 
**redirect_time** | **int** | Cumulative redirect timing in milliseconds. | [optional] [readonly] 
**response_code** | **int** | HTTP response code. | [optional] [readonly] 
**response_time** | **int** | Time to first byte in milliseconds. | [optional] [readonly] 
**ssl_time** | **int** | Time to negotiate SSL/TLS in milliseconds. | [optional] [readonly] 
**total_time** | **int** | Total time is the response time + receive time. | [optional] [readonly] 
**wait_time** | **int** | Time elapsed between completion of request and first byte of response in milliseconds. | [optional] [readonly] 
**wire_size** | **int** | Size of content in bytes. | [optional] [readonly] 

## Example

```python
from thousandeyes_sdk.endpoint_test_results.models.http_test_result import HttpTestResult

# TODO update the JSON string below
json = "{}"
# create an instance of HttpTestResult from a JSON string
http_test_result_instance = HttpTestResult.from_json(json)
# print the JSON string representation of the object
print(HttpTestResult.to_json())

# convert the object into a dict
http_test_result_dict = http_test_result_instance.to_dict()
# create an instance of HttpTestResult from a dict
http_test_result_from_dict = HttpTestResult.from_dict(http_test_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


