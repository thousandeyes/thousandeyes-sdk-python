# EndpointRealUserTestsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**real_user_tests** | [**List[EndpointRealUserTest]**](EndpointRealUserTest.md) | Real user test domain monitoring profiles. | 

## Example

```python
from thousandeyes_sdk.endpoint_tests.models.endpoint_real_user_tests_response import EndpointRealUserTestsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointRealUserTestsResponse from a JSON string
endpoint_real_user_tests_response_instance = EndpointRealUserTestsResponse.from_json(json)
# print the JSON string representation of the object
print(EndpointRealUserTestsResponse.to_json())

# convert the object into a dict
endpoint_real_user_tests_response_dict = endpoint_real_user_tests_response_instance.to_dict()
# create an instance of EndpointRealUserTestsResponse from a dict
endpoint_real_user_tests_response_from_dict = EndpointRealUserTestsResponse.from_dict(endpoint_real_user_tests_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


