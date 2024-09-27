# EndpointPathVisHop


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hop** | **int** | The hop index. | [optional] [readonly] 
**ip_address** | **str** | IP address of the hop. | [optional] [readonly] 
**prefix** | **str** | Prefix of IP address shown in CIDR. | [optional] [readonly] 
**rdns** | **str** | Reverse DNS entry of IP, if available. | [optional] [readonly] 
**network** | **str** | Autonomous System originating the prefix. | [optional] [readonly] 
**response_time** | **int** | RTT to the hop’s IP in milliseconds. | [optional] [readonly] 
**location** | **str** | Location information for the hop. | [optional] [readonly] 

## Example

```python
from thousandeyes_sdk.endpoint_test_results.models.endpoint_path_vis_hop import EndpointPathVisHop

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointPathVisHop from a JSON string
endpoint_path_vis_hop_instance = EndpointPathVisHop.from_json(json)
# print the JSON string representation of the object
print(EndpointPathVisHop.to_json())

# convert the object into a dict
endpoint_path_vis_hop_dict = endpoint_path_vis_hop_instance.to_dict()
# create an instance of EndpointPathVisHop from a dict
endpoint_path_vis_hop_from_dict = EndpointPathVisHop.from_dict(endpoint_path_vis_hop_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


