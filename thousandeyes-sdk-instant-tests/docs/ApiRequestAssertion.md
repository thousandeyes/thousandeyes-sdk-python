# ApiRequestAssertion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | [**ApiRequestAssertionName**](ApiRequestAssertionName.md) |  | [optional] 
**operator** | [**ApiRequestAssertionOperator**](ApiRequestAssertionOperator.md) |  | [optional] 
**value** | **str** | The value of the assertion. If name &#x3D; &#x60;status-code&#x60;, the status code to assert. If name &#x3D; &#x60;response-body&#x60;, the lookup value to assert. | [optional] 

## Example

```python
from thousandeyes_sdk.instant_tests.models.api_request_assertion import ApiRequestAssertion

# TODO update the JSON string below
json = "{}"
# create an instance of ApiRequestAssertion from a JSON string
api_request_assertion_instance = ApiRequestAssertion.from_json(json)
# print the JSON string representation of the object
print(ApiRequestAssertion.to_json())

# convert the object into a dict
api_request_assertion_dict = api_request_assertion_instance.to_dict()
# create an instance of ApiRequestAssertion from a dict
api_request_assertion_from_dict = ApiRequestAssertion.from_dict(api_request_assertion_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


