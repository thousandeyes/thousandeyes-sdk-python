# WebTransactionTests


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tests** | [**List[UnexpandedWebTransactionTest]**](UnexpandedWebTransactionTest.md) |  | [optional] 
**links** | [**SelfLinks**](SelfLinks.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.tests.models.web_transaction_tests import WebTransactionTests

# TODO update the JSON string below
json = "{}"
# create an instance of WebTransactionTests from a JSON string
web_transaction_tests_instance = WebTransactionTests.from_json(json)
# print the JSON string representation of the object
print(WebTransactionTests.to_json())

# convert the object into a dict
web_transaction_tests_dict = web_transaction_tests_instance.to_dict()
# create an instance of WebTransactionTests from a dict
web_transaction_tests_from_dict = WebTransactionTests.from_dict(web_transaction_tests_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


