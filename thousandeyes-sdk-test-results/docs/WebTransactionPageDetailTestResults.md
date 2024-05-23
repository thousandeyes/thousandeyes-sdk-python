# WebTransactionPageDetailTestResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[WebTransactionPageDetailTestResult]**](WebTransactionPageDetailTestResult.md) |  | [optional] 
**test** | [**SimpleTest**](SimpleTest.md) |  | [optional] 
**links** | [**PaginationLinks**](PaginationLinks.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.test_results.models.web_transaction_page_detail_test_results import WebTransactionPageDetailTestResults

# TODO update the JSON string below
json = "{}"
# create an instance of WebTransactionPageDetailTestResults from a JSON string
web_transaction_page_detail_test_results_instance = WebTransactionPageDetailTestResults.from_json(json)
# print the JSON string representation of the object
print(WebTransactionPageDetailTestResults.to_json())

# convert the object into a dict
web_transaction_page_detail_test_results_dict = web_transaction_page_detail_test_results_instance.to_dict()
# create an instance of WebTransactionPageDetailTestResults from a dict
web_transaction_page_detail_test_results_from_dict = WebTransactionPageDetailTestResults.from_dict(web_transaction_page_detail_test_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


