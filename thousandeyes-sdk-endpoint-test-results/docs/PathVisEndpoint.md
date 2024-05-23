# PathVisEndpoint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip_address** | **str** | IP address of the hop destination. | [optional] [readonly] 
**number_of_hops** | **int** | Number of hops for path trace to destination. | [optional] [readonly] 
**path_id** | **str** | Unique ID of path trace. | [optional] [readonly] 
**response_time** | **int** | RTT of the path trace to the destination in milliseconds. | [optional] [readonly] 

## Example

```python
from thousandeyes_sdk.endpoint_test_results.models.path_vis_endpoint import PathVisEndpoint

# TODO update the JSON string below
json = "{}"
# create an instance of PathVisEndpoint from a JSON string
path_vis_endpoint_instance = PathVisEndpoint.from_json(json)
# print the JSON string representation of the object
print(PathVisEndpoint.to_json())

# convert the object into a dict
path_vis_endpoint_dict = path_vis_endpoint_instance.to_dict()
# create an instance of PathVisEndpoint from a dict
path_vis_endpoint_from_dict = PathVisEndpoint.from_dict(path_vis_endpoint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


