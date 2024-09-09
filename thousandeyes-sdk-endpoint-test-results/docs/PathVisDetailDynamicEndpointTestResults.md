# PathVisDetailDynamicEndpointTestResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[PathVisDetailDynamicEndpointTestResult]**](PathVisDetailDynamicEndpointTestResult.md) |  | [optional] 
**test** | [**DynamicTest**](DynamicTest.md) |  | [optional] 
**links** | [**SelfLinks**](SelfLinks.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_test_results.models.path_vis_detail_dynamic_endpoint_test_results import PathVisDetailDynamicEndpointTestResults

# TODO update the JSON string below
json = "{}"
# create an instance of PathVisDetailDynamicEndpointTestResults from a JSON string
path_vis_detail_dynamic_endpoint_test_results_instance = PathVisDetailDynamicEndpointTestResults.from_json(json)
# print the JSON string representation of the object
print(PathVisDetailDynamicEndpointTestResults.to_json())

# convert the object into a dict
path_vis_detail_dynamic_endpoint_test_results_dict = path_vis_detail_dynamic_endpoint_test_results_instance.to_dict()
# create an instance of PathVisDetailDynamicEndpointTestResults from a dict
path_vis_detail_dynamic_endpoint_test_results_from_dict = PathVisDetailDynamicEndpointTestResults.from_dict(path_vis_detail_dynamic_endpoint_test_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


