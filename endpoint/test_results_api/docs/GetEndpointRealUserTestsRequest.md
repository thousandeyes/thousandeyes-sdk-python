# GetEndpointRealUserTestsRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**search_filters** | [**EndpointRealUserTestResultRequestFilter**](EndpointRealUserTestResultRequestFilter.md) |  | [optional] 

## Example

```python
from test_results_api.models.get_endpoint_real_user_tests_request import GetEndpointRealUserTestsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetEndpointRealUserTestsRequest from a JSON string
get_endpoint_real_user_tests_request_instance = GetEndpointRealUserTestsRequest.from_json(json)
# print the JSON string representation of the object
print GetEndpointRealUserTestsRequest.to_json()

# convert the object into a dict
get_endpoint_real_user_tests_request_dict = get_endpoint_real_user_tests_request_instance.to_dict()
# create an instance of GetEndpointRealUserTestsRequest from a dict
get_endpoint_real_user_tests_request_form_dict = get_endpoint_real_user_tests_request.from_dict(get_endpoint_real_user_tests_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


