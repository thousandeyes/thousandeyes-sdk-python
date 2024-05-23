# ApiRequestDetailAssertion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**step** | **int** | Index of the assertion, starting at 1. | [optional] 
**has_failed** | **bool** | Indicates if the assertion passed or failed. &#x60;true&#x60; if the assertion failed; &#x60;false&#x60; if the assertion passed. | [optional] 

## Example

```python
from thousandeyes_sdk.test_results.models.api_request_detail_assertion import ApiRequestDetailAssertion

# TODO update the JSON string below
json = "{}"
# create an instance of ApiRequestDetailAssertion from a JSON string
api_request_detail_assertion_instance = ApiRequestDetailAssertion.from_json(json)
# print the JSON string representation of the object
print(ApiRequestDetailAssertion.to_json())

# convert the object into a dict
api_request_detail_assertion_dict = api_request_detail_assertion_instance.to_dict()
# create an instance of ApiRequestDetailAssertion from a dict
api_request_detail_assertion_from_dict = ApiRequestDetailAssertion.from_dict(api_request_detail_assertion_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


