# ApiDetailTestResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **datetime** | Data point date UTC (ISO date-time format). | [optional] [readonly] 
**round_id** | **int** | Epoch time (seconds) indicating the start time of the round | [optional] [readonly] 
**links** | [**TestResultAppLinks**](TestResultAppLinks.md) |  | [optional] 
**start_time** | **int** | Epoch time (seconds) indicating the start time of the round | [optional] [readonly] 
**end_time** | **int** | Epoch time (seconds) indicating the end time of the round | [optional] [readonly] 
**agent** | [**TestResultAgent**](TestResultAgent.md) |  | [optional] 
**api_transaction_time** | **float** | Elapsed execution time of the API steps. | [optional] [readonly] 
**completion** | **float** | Percentage of steps which completed successfully and passed assertions. | [optional] [readonly] 
**error_type** | **str** | Type of error encountered. | [optional] [readonly] 
**error_details** | **str** | Error details, if an error were encountered | [optional] [readonly] 
**requests** | [**List[ApiRequestDetail]**](ApiRequestDetail.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.test_results.models.api_detail_test_result import ApiDetailTestResult

# TODO update the JSON string below
json = "{}"
# create an instance of ApiDetailTestResult from a JSON string
api_detail_test_result_instance = ApiDetailTestResult.from_json(json)
# print the JSON string representation of the object
print(ApiDetailTestResult.to_json())

# convert the object into a dict
api_detail_test_result_dict = api_detail_test_result_instance.to_dict()
# create an instance of ApiDetailTestResult from a dict
api_detail_test_result_from_dict = ApiDetailTestResult.from_dict(api_detail_test_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


