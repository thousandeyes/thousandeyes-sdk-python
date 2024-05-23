# WebTransactionDetailTestResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[WebTransactionDetailTestResult]**](WebTransactionDetailTestResult.md) |  | [optional] 
**test** | [**SimpleTest**](SimpleTest.md) |  | [optional] 
**links** | [**PaginationLinks**](PaginationLinks.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.test_results.models.web_transaction_detail_test_results import WebTransactionDetailTestResults

# TODO update the JSON string below
json = "{}"
# create an instance of WebTransactionDetailTestResults from a JSON string
web_transaction_detail_test_results_instance = WebTransactionDetailTestResults.from_json(json)
# print the JSON string representation of the object
print(WebTransactionDetailTestResults.to_json())

# convert the object into a dict
web_transaction_detail_test_results_dict = web_transaction_detail_test_results_instance.to_dict()
# create an instance of WebTransactionDetailTestResults from a dict
web_transaction_detail_test_results_from_dict = WebTransactionDetailTestResults.from_dict(web_transaction_detail_test_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


