# WebTransactionPageDetailTestResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **datetime** | Data point date UTC (ISO date-time format). | [optional] [readonly] 
**round_id** | **int** | Epoch time (seconds) indicating the start time of the round | [optional] [readonly] 
**links** | [**TestResultAppLinks**](TestResultAppLinks.md) |  | [optional] 
**start_time** | **int** | Epoch time (seconds) indicating the start time of the round | [optional] [readonly] 
**end_time** | **int** | Epoch time (seconds) indicating the end time of the round | [optional] [readonly] 
**agent** | [**TestResultAgent**](TestResultAgent.md) |  | [optional] 
**component_errors** | **int** | Number of components which did not successfully load | [optional] [readonly] 
**transaction_time** | **int** | Elapsed execution time of the web transaction script in milliseconds | [optional] [readonly] 
**error_type** | **str** | Type of error encountered; corresponds to phase of connection | [optional] [readonly] 
**error_details** | **str** | Error details, if an error were encountered | [optional] [readonly] 
**markers** | [**List[Marker]**](Marker.md) |  | [optional] 
**pages** | [**List[Page]**](Page.md) |  | [optional] 
**har** | **object** | See [HAR specification](http://www.softwareishard.com/blog/har-12-spec/) for details | [optional] [readonly] 

## Example

```python
from thousandeyes_sdk.test_results.models.web_transaction_page_detail_test_result import WebTransactionPageDetailTestResult

# TODO update the JSON string below
json = "{}"
# create an instance of WebTransactionPageDetailTestResult from a JSON string
web_transaction_page_detail_test_result_instance = WebTransactionPageDetailTestResult.from_json(json)
# print the JSON string representation of the object
print(WebTransactionPageDetailTestResult.to_json())

# convert the object into a dict
web_transaction_page_detail_test_result_dict = web_transaction_page_detail_test_result_instance.to_dict()
# create an instance of WebTransactionPageDetailTestResult from a dict
web_transaction_page_detail_test_result_from_dict = WebTransactionPageDetailTestResult.from_dict(web_transaction_page_detail_test_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


