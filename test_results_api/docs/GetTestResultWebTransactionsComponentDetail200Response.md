# GetTestResultWebTransactionsComponentDetail200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[WebTransactionDetailTestResult]**](WebTransactionDetailTestResult.md) |  | [optional] 
**test** | [**SimpleTest**](SimpleTest.md) |  | [optional] 
**links** | [**SelfLinksLinks**](SelfLinksLinks.md) |  | [optional] 

## Example

```python
from test_results_api.models.get_test_result_web_transactions_component_detail200_response import GetTestResultWebTransactionsComponentDetail200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetTestResultWebTransactionsComponentDetail200Response from a JSON string
get_test_result_web_transactions_component_detail200_response_instance = GetTestResultWebTransactionsComponentDetail200Response.from_json(json)
# print the JSON string representation of the object
print GetTestResultWebTransactionsComponentDetail200Response.to_json()

# convert the object into a dict
get_test_result_web_transactions_component_detail200_response_dict = get_test_result_web_transactions_component_detail200_response_instance.to_dict()
# create an instance of GetTestResultWebTransactionsComponentDetail200Response from a dict
get_test_result_web_transactions_component_detail200_response_form_dict = get_test_result_web_transactions_component_detail200_response.from_dict(get_test_result_web_transactions_component_detail200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


