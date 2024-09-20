# DnsServerTestResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **datetime** | Data point date UTC (ISO date-time format). | [optional] [readonly] 
**round_id** | **int** | Epoch time (seconds) indicating the start time of the round | [optional] [readonly] 
**links** | [**TestResultAppLinks**](TestResultAppLinks.md) |  | [optional] 
**start_time** | **int** | Epoch time (seconds) indicating the start time of the round | [optional] [readonly] 
**end_time** | **int** | Epoch time (seconds) indicating the end time of the round | [optional] [readonly] 
**agent** | [**TestResultAgent**](TestResultAgent.md) |  | [optional] 
**server_id** | **str** | Internal ID of DNS server being tested | [optional] [readonly] 
**server** | **str** | Canonical name of server being tested | [optional] [readonly] 
**resolution_time** | **int** | How long it took to run the query against the serverow long it took to run the query against the server | [optional] [readonly] 
**error_details** | **str** | Error details, if an error were encountered | [optional] [readonly] 
**mappings** | **str** | Final mappings returned from the request | [optional] [readonly] 

## Example

```python
from thousandeyes_sdk.test_results.models.dns_server_test_result import DnsServerTestResult

# TODO update the JSON string below
json = "{}"
# create an instance of DnsServerTestResult from a JSON string
dns_server_test_result_instance = DnsServerTestResult.from_json(json)
# print the JSON string representation of the object
print(DnsServerTestResult.to_json())

# convert the object into a dict
dns_server_test_result_dict = dns_server_test_result_instance.to_dict()
# create an instance of DnsServerTestResult from a dict
dns_server_test_result_from_dict = DnsServerTestResult.from_dict(dns_server_test_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


