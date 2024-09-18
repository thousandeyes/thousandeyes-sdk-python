# PathTrace


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip_address** | **str** | IP address of the hop | [optional] [readonly] 
**mss** | **int** | Maximum segment size in bytes | [optional] [readonly] 
**number_of_hops** | **int** | Number of hops for path trace to destination | [optional] [readonly] 
**path_id** | **str** | Unique ID of path trace | [optional] [readonly] 
**path_mtu** | **int** | MTU sizes on network from agents to the target | [optional] [readonly] 
**response_time** | **int** | RTT of the path trace to the destination in milliseconds | [optional] [readonly] 

## Example

```python
from thousandeyes_sdk.test_results.models.path_trace import PathTrace

# TODO update the JSON string below
json = "{}"
# create an instance of PathTrace from a JSON string
path_trace_instance = PathTrace.from_json(json)
# print the JSON string representation of the object
print(PathTrace.to_json())

# convert the object into a dict
path_trace_dict = path_trace_instance.to_dict()
# create an instance of PathTrace from a dict
path_trace_from_dict = PathTrace.from_dict(path_trace_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


