# GetWebTransactionsTests200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tests** | [**List[UnexpandedWebTransactionTest]**](UnexpandedWebTransactionTest.md) |  | [optional] 
**links** | [**SelfLinksLinks**](SelfLinksLinks.md) |  | [optional] 

## Example

```python
from tests.models.get_web_transactions_tests200_response import GetWebTransactionsTests200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetWebTransactionsTests200Response from a JSON string
get_web_transactions_tests200_response_instance = GetWebTransactionsTests200Response.from_json(json)
# print the JSON string representation of the object
print(GetWebTransactionsTests200Response.to_json())

# convert the object into a dict
get_web_transactions_tests200_response_dict = get_web_transactions_tests200_response_instance.to_dict()
# create an instance of GetWebTransactionsTests200Response from a dict
get_web_transactions_tests200_response_from_dict = GetWebTransactionsTests200Response.from_dict(get_web_transactions_tests200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


