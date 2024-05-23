# WebTransactionTestResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[WebTransactionTestResult]**](WebTransactionTestResult.md) |  | [optional] 
**test** | [**SimpleTest**](SimpleTest.md) |  | [optional] 
**start_date** | **datetime** | (Optional) When passing &#x60;window&#x60; or &#x60;startDate&#x60; parameter,  the client will also receive the &#x60;startDate&#x60; field indicating the UTC start date of the data&#39;s time range being retrieved  (ISO date-time format). | [optional] [readonly] 
**end_date** | **datetime** | (Optional) When passing &#x60;window&#x60; or &#x60;endDate&#x60; parameter,  the client will also receive the &#x60;endDate&#x60; field indicating the UTC end date of the data&#39;s time range being retrieved  (ISO date-time format). | [optional] [readonly] 
**links** | [**PaginationLinks**](PaginationLinks.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.test_results.models.web_transaction_test_results import WebTransactionTestResults

# TODO update the JSON string below
json = "{}"
# create an instance of WebTransactionTestResults from a JSON string
web_transaction_test_results_instance = WebTransactionTestResults.from_json(json)
# print the JSON string representation of the object
print(WebTransactionTestResults.to_json())

# convert the object into a dict
web_transaction_test_results_dict = web_transaction_test_results_instance.to_dict()
# create an instance of WebTransactionTestResults from a dict
web_transaction_test_results_from_dict = WebTransactionTestResults.from_dict(web_transaction_test_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


