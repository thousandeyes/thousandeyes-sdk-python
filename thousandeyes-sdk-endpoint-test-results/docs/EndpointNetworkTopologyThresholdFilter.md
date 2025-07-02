# EndpointNetworkTopologyThresholdFilter

Applies all filters using the specified conditional operator (AND or OR).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | [**List[LocalNetworksThresholdFilter]**](LocalNetworksThresholdFilter.md) |  | [optional] 
**conditional_operator** | [**ConditionalOperator**](ConditionalOperator.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_test_results.models.endpoint_network_topology_threshold_filter import EndpointNetworkTopologyThresholdFilter

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointNetworkTopologyThresholdFilter from a JSON string
endpoint_network_topology_threshold_filter_instance = EndpointNetworkTopologyThresholdFilter.from_json(json)
# print the JSON string representation of the object
print(EndpointNetworkTopologyThresholdFilter.to_json())

# convert the object into a dict
endpoint_network_topology_threshold_filter_dict = endpoint_network_topology_threshold_filter_instance.to_dict()
# create an instance of EndpointNetworkTopologyThresholdFilter from a dict
endpoint_network_topology_threshold_filter_from_dict = EndpointNetworkTopologyThresholdFilter.from_dict(endpoint_network_topology_threshold_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


