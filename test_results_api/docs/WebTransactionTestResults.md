# WebTransactionTestResults


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[WebTransactionTestResult]**](WebTransactionTestResult.md) |  | [optional] 
**test** | [**SimpleTest**](SimpleTest.md) |  | [optional] 

## Example

```python
from test_results_api.models.web_transaction_test_results import WebTransactionTestResults

# TODO update the JSON string below
json = "{}"
# create an instance of WebTransactionTestResults from a JSON string
web_transaction_test_results_instance = WebTransactionTestResults.from_json(json)
# print the JSON string representation of the object
print WebTransactionTestResults.to_json()

# convert the object into a dict
web_transaction_test_results_dict = web_transaction_test_results_instance.to_dict()
# create an instance of WebTransactionTestResults from a dict
web_transaction_test_results_form_dict = web_transaction_test_results.from_dict(web_transaction_test_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


