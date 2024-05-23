# PathVisRoute


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path_id** | **str** | Unique ID of path trace | [optional] [readonly] 
**hops** | [**List[PathVisHop]**](PathVisHop.md) | Array of hop objects indicating each step in the traceroute | [optional] 

## Example

```python
from thousandeyes_sdk.test_results.models.path_vis_route import PathVisRoute

# TODO update the JSON string below
json = "{}"
# create an instance of PathVisRoute from a JSON string
path_vis_route_instance = PathVisRoute.from_json(json)
# print the JSON string representation of the object
print(PathVisRoute.to_json())

# convert the object into a dict
path_vis_route_dict = path_vis_route_instance.to_dict()
# create an instance of PathVisRoute from a dict
path_vis_route_from_dict = PathVisRoute.from_dict(path_vis_route_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


