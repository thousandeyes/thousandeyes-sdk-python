# EndpointRealUserTestDetailResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[EndpointRealUserTestDetail]**](EndpointRealUserTestDetail.md) |  | [optional] 
**links** | [**SelfLinks**](SelfLinks.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_test_results.models.endpoint_real_user_test_detail_results import EndpointRealUserTestDetailResults

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointRealUserTestDetailResults from a JSON string
endpoint_real_user_test_detail_results_instance = EndpointRealUserTestDetailResults.from_json(json)
# print the JSON string representation of the object
print(EndpointRealUserTestDetailResults.to_json())

# convert the object into a dict
endpoint_real_user_test_detail_results_dict = endpoint_real_user_test_detail_results_instance.to_dict()
# create an instance of EndpointRealUserTestDetailResults from a dict
endpoint_real_user_test_detail_results_from_dict = EndpointRealUserTestDetailResults.from_dict(endpoint_real_user_test_detail_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


