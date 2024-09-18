# HttpTestResult


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
**response_code** | **int** | HTTP response code | [optional] 
**num_redirects** | **int** | Number of redirects | [optional] 
**redirect_time** | **int** | Cumulative redirect timing in milliseconds | [optional] 
**dns_time** | **int** | Time required to resolve DNS in milliseconds | [optional] 
**ssl_time** | **int** | Time to negotiate SSL/TLS in milliseconds | [optional] 
**connect_time** | **int** | Time required to establish a TCP connection to the server | [optional] 
**wait_time** | **int** | Time elapsed between completion of request and first byte of response in milliseconds | [optional] 
**receive_time** | **int** | Elapsed time between first and last byte of response in milliseconds | [optional] 
**wire_size** | **int** | Size of content in bytes | [optional] 
**response_time** | **int** | Time to first byte in milliseconds | [optional] 
**throughput** | **float** | WireSize divided by receiveTime in byter per second | [optional] 
**total_time** | **int** | response time + receive time | [optional] 
**headers** | [**HttpTestResultHeaders**](HttpTestResultHeaders.md) |  | [optional] 
**error_type** | **str** | Type of error encountered; corresponds to phase of connection | [optional] [readonly] 
**error_details** | **str** | Error details, if an error were encountered | [optional] [readonly] 
**ssl_cipher** | **str** | Cipher suite | [optional] 
**ssl_version** | **str** | TLS version | [optional] 
**ssl_certificates** | [**List[SslCert]**](SslCert.md) |  | [optional] 
**health_score** | **float** | A normalized value (0.0-1.0) representing the web application connection health of the test target. Returns negative values as error codes. -1.0 indicates there was insufficient data to calculate the health score. | [optional] 

## Example

```python
from thousandeyes_sdk.test_results.models.http_test_result import HttpTestResult

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


