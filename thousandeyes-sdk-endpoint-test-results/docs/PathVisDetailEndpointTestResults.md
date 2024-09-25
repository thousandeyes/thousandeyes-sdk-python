# PathVisDetailEndpointTestResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[PathVisDetailEndpointTestResult]**](PathVisDetailEndpointTestResult.md) |  | [optional] 
**test** | [**EndpointScheduledTest**](EndpointScheduledTest.md) |  | [optional] 
**links** | [**SelfLinks**](SelfLinks.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_test_results.models.path_vis_detail_endpoint_test_results import PathVisDetailEndpointTestResults

# TODO update the JSON string below
json = "{}"
# create an instance of PathVisDetailEndpointTestResults from a JSON string
path_vis_detail_endpoint_test_results_instance = PathVisDetailEndpointTestResults.from_json(json)
# print the JSON string representation of the object
print(PathVisDetailEndpointTestResults.to_json())

# convert the object into a dict
path_vis_detail_endpoint_test_results_dict = path_vis_detail_endpoint_test_results_instance.to_dict()
# create an instance of PathVisDetailEndpointTestResults from a dict
path_vis_detail_endpoint_test_results_from_dict = PathVisDetailEndpointTestResults.from_dict(path_vis_detail_endpoint_test_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


