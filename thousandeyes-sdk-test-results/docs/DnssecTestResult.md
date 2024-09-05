# DnssecTestResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **datetime** | Data point date UTC (ISO date-time format). | [optional] [readonly] 
**round_id** | **int** | Epoch time (seconds) indicating the start time of the round | [optional] [readonly] 
**links** | [**TestResultAppLinks**](TestResultAppLinks.md) |  | [optional] 
**start_time** | **int** | Epoch time (seconds) indicating the start time of the round | [optional] [readonly] 
**end_time** | **int** | Epoch time (seconds) indicating the end time of the round | [optional] [readonly] 
**agent** | [**TestResultAgent**](TestResultAgent.md) |  | [optional] 
**is_valid** | **bool** | Indicates if keychain is valid (if false see errorDetails field) | [optional] [readonly] 
**error_details** | **str** | Error details, if an error were encountered | [optional] [readonly] 

## Example

```python
from thousandeyes_sdk.test_results.models.dnssec_test_result import DnssecTestResult

# TODO update the JSON string below
json = "{}"
# create an instance of DnssecTestResult from a JSON string
dnssec_test_result_instance = DnssecTestResult.from_json(json)
# print the JSON string representation of the object
print(DnssecTestResult.to_json())

# convert the object into a dict
dnssec_test_result_dict = dnssec_test_result_instance.to_dict()
# create an instance of DnssecTestResult from a dict
dnssec_test_result_from_dict = DnssecTestResult.from_dict(dnssec_test_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


