# GetTestResultWebTransactionsComponentPageDetail200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[WebTransactionPageDetailTestResult]**](WebTransactionPageDetailTestResult.md) |  | [optional] 
**test** | [**SimpleTest**](SimpleTest.md) |  | [optional] 
**links** | [**PaginationLinksLinks**](PaginationLinksLinks.md) |  | [optional] 

## Example

```python
from test_results.models.get_test_result_web_transactions_component_page_detail200_response import GetTestResultWebTransactionsComponentPageDetail200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetTestResultWebTransactionsComponentPageDetail200Response from a JSON string
get_test_result_web_transactions_component_page_detail200_response_instance = GetTestResultWebTransactionsComponentPageDetail200Response.from_json(json)
# print the JSON string representation of the object
print(GetTestResultWebTransactionsComponentPageDetail200Response.to_json())

# convert the object into a dict
get_test_result_web_transactions_component_page_detail200_response_dict = get_test_result_web_transactions_component_page_detail200_response_instance.to_dict()
# create an instance of GetTestResultWebTransactionsComponentPageDetail200Response from a dict
get_test_result_web_transactions_component_page_detail200_response_from_dict = GetTestResultWebTransactionsComponentPageDetail200Response.from_dict(get_test_result_web_transactions_component_page_detail200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


