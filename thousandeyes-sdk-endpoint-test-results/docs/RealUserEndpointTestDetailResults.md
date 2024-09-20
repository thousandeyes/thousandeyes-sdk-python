# RealUserEndpointTestDetailResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[RealUserEndpointTestDetail]**](RealUserEndpointTestDetail.md) |  | [optional] 
**links** | [**SelfLinks**](SelfLinks.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_test_results.models.real_user_endpoint_test_detail_results import RealUserEndpointTestDetailResults

# TODO update the JSON string below
json = "{}"
# create an instance of RealUserEndpointTestDetailResults from a JSON string
real_user_endpoint_test_detail_results_instance = RealUserEndpointTestDetailResults.from_json(json)
# print the JSON string representation of the object
print(RealUserEndpointTestDetailResults.to_json())

# convert the object into a dict
real_user_endpoint_test_detail_results_dict = real_user_endpoint_test_detail_results_instance.to_dict()
# create an instance of RealUserEndpointTestDetailResults from a dict
real_user_endpoint_test_detail_results_from_dict = RealUserEndpointTestDetailResults.from_dict(real_user_endpoint_test_detail_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


