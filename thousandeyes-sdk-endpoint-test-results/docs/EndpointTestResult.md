# EndpointTestResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aid** | **str** | A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. | [optional] 
**test_id** | **str** | Unique ID of endpoint test. | [optional] [readonly] 
**agent_id** | **str** | Unique ID of endpoint agent, from &#x60;/endpoint/agents&#x60; endpoint. | [optional] [readonly] 
**round_id** | **int** | Epoch time (seconds) indicating the start time of the round. | [optional] [readonly] 
**server_ip** | **str** | IP address of target server. | [optional] [readonly] 
**network_profile** | [**NetworkProfile**](NetworkProfile.md) |  | [optional] 
**system_metrics** | [**SystemMetrics**](SystemMetrics.md) |  | [optional] 
**original_target_profile** | [**TargetProfile**](TargetProfile.md) |  | [optional] 
**vpn_profile** | [**VpnProfile**](VpnProfile.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_test_results.models.endpoint_test_result import EndpointTestResult

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointTestResult from a JSON string
endpoint_test_result_instance = EndpointTestResult.from_json(json)
# print the JSON string representation of the object
print(EndpointTestResult.to_json())

# convert the object into a dict
endpoint_test_result_dict = endpoint_test_result_instance.to_dict()
# create an instance of EndpointTestResult from a dict
endpoint_test_result_from_dict = EndpointTestResult.from_dict(endpoint_test_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


