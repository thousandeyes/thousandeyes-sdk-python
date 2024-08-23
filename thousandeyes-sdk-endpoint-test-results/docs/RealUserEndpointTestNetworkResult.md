# RealUserEndpointTestNetworkResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_id** | **str** | Unique ID of endpoint agent, from &#x60;/endpoint/agents&#x60; endpoint. | [optional] [readonly] 
**var_date** | **datetime** | UTC date when endpoint real user test took place (ISO date-time format). | [optional] [readonly] 
**id** | **str** | Endpoint real user test ID. Each endpoint real user test occurrence has a unique ID. | [optional] [readonly] 
**round_id** | **int** | Epoch time (seconds) indicating the start time of the round. | [optional] [readonly] 
**destination** | [**NetworkMetrics**](NetworkMetrics.md) |  | [optional] 
**vpn** | [**NetworkMetrics**](NetworkMetrics.md) |  | [optional] 
**proxy** | [**NetworkMetrics**](NetworkMetrics.md) |  | [optional] 
**system_metrics** | [**SystemMetrics**](SystemMetrics.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_test_results.models.real_user_endpoint_test_network_result import RealUserEndpointTestNetworkResult

# TODO update the JSON string below
json = "{}"
# create an instance of RealUserEndpointTestNetworkResult from a JSON string
real_user_endpoint_test_network_result_instance = RealUserEndpointTestNetworkResult.from_json(json)
# print the JSON string representation of the object
print(RealUserEndpointTestNetworkResult.to_json())

# convert the object into a dict
real_user_endpoint_test_network_result_dict = real_user_endpoint_test_network_result_instance.to_dict()
# create an instance of RealUserEndpointTestNetworkResult from a dict
real_user_endpoint_test_network_result_from_dict = RealUserEndpointTestNetworkResult.from_dict(real_user_endpoint_test_network_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


