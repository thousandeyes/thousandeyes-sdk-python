# NetworkMetrics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**jitter** | **int** | Network jitter. | [optional] [readonly] 
**latency** | **int** | Network latency. | [optional] [readonly] 
**loss** | **float** | Network loss. | [optional] [readonly] 
**target** | **str** | Network target IP address. | [optional] [readonly] 

## Example

```python
from thousandeyes_sdk.endpoint_test_results.models.network_metrics import NetworkMetrics

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkMetrics from a JSON string
network_metrics_instance = NetworkMetrics.from_json(json)
# print the JSON string representation of the object
print(NetworkMetrics.to_json())

# convert the object into a dict
network_metrics_dict = network_metrics_instance.to_dict()
# create an instance of NetworkMetrics from a dict
network_metrics_from_dict = NetworkMetrics.from_dict(network_metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


