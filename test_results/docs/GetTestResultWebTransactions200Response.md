# GetTestResultWebTransactions200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** | (Optional) When passing &#x60;window&#x60; or &#x60;startDate&#x60; parameter,  the client will also receive the &#x60;startDate&#x60; field indicating the UTC start date of the data&#39;s time range being retrieved  (ISO date-time format). | [optional] [readonly] 
**end_date** | **datetime** | (Optional) When passing &#x60;window&#x60; or &#x60;endDate&#x60; parameter,  the client will also receive the &#x60;endDate&#x60; field indicating the UTC end date of the data&#39;s time range being retrieved  (ISO date-time format). | [optional] [readonly] 
**results** | [**List[WebTransactionTestResult]**](WebTransactionTestResult.md) |  | [optional] 
**test** | [**SimpleTest**](SimpleTest.md) |  | [optional] 
**links** | [**PaginationLinksLinks**](PaginationLinksLinks.md) |  | [optional] 

## Example

```python
from test_results.models.get_test_result_web_transactions200_response import GetTestResultWebTransactions200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetTestResultWebTransactions200Response from a JSON string
get_test_result_web_transactions200_response_instance = GetTestResultWebTransactions200Response.from_json(json)
# print the JSON string representation of the object
print(GetTestResultWebTransactions200Response.to_json())

# convert the object into a dict
get_test_result_web_transactions200_response_dict = get_test_result_web_transactions200_response_instance.to_dict()
# create an instance of GetTestResultWebTransactions200Response from a dict
get_test_result_web_transactions200_response_from_dict = GetTestResultWebTransactions200Response.from_dict(get_test_result_web_transactions200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


