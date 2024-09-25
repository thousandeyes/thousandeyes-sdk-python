# RealUserEndpointTestResultsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**search_filters** | [**RealUserEndpointTestResultRequestFilter**](RealUserEndpointTestResultRequestFilter.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_test_results.models.real_user_endpoint_test_results_request import RealUserEndpointTestResultsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RealUserEndpointTestResultsRequest from a JSON string
real_user_endpoint_test_results_request_instance = RealUserEndpointTestResultsRequest.from_json(json)
# print the JSON string representation of the object
print(RealUserEndpointTestResultsRequest.to_json())

# convert the object into a dict
real_user_endpoint_test_results_request_dict = real_user_endpoint_test_results_request_instance.to_dict()
# create an instance of RealUserEndpointTestResultsRequest from a dict
real_user_endpoint_test_results_request_from_dict = RealUserEndpointTestResultsRequest.from_dict(real_user_endpoint_test_results_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


