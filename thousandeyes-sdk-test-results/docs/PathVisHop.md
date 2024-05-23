# PathVisHop


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hop** | **int** | Hop index | [optional] [readonly] 
**ip_address** | **str** | IP address of the hop | [optional] [readonly] 
**prefix** | **str** | Prefix of IP address shown in CIDR | [optional] [readonly] 
**rdns** | **str** | Reverse DNS entry of IP, if available | [optional] [readonly] 
**network** | **str** | Autonomous System originating the prefix | [optional] [readonly] 
**response_time** | **int** | RTT to the hop’s IP in milliseconds | [optional] [readonly] 
**location** | **str** | Location information for the hop | [optional] [readonly] 
**mpls** | **str** | Multiprotocol Label Switching information, if available | [optional] [readonly] 

## Example

```python
from thousandeyes_sdk.test_results.models.path_vis_hop import PathVisHop

# TODO update the JSON string below
json = "{}"
# create an instance of PathVisHop from a JSON string
path_vis_hop_instance = PathVisHop.from_json(json)
# print the JSON string representation of the object
print(PathVisHop.to_json())

# convert the object into a dict
path_vis_hop_dict = path_vis_hop_instance.to_dict()
# create an instance of PathVisHop from a dict
path_vis_hop_from_dict = PathVisHop.from_dict(path_vis_hop_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


