# EndpointRealUserTestResultsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**search_filters** | [**EndpointRealUserTestResultRequestFilter**](EndpointRealUserTestResultRequestFilter.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_test_results.models.endpoint_real_user_test_results_request import EndpointRealUserTestResultsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointRealUserTestResultsRequest from a JSON string
endpoint_real_user_test_results_request_instance = EndpointRealUserTestResultsRequest.from_json(json)
# print the JSON string representation of the object
print(EndpointRealUserTestResultsRequest.to_json())

# convert the object into a dict
endpoint_real_user_test_results_request_dict = endpoint_real_user_test_results_request_instance.to_dict()
# create an instance of EndpointRealUserTestResultsRequest from a dict
endpoint_real_user_test_results_request_from_dict = EndpointRealUserTestResultsRequest.from_dict(endpoint_real_user_test_results_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


