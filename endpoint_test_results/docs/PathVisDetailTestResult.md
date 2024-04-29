# PathVisDetailTestResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aid** | **str** | A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. | [optional] 
**agent_id** | **str** | Unique ID of endpoint agent, from &#x60;/endpoint/agents&#x60; endpoint. | [optional] [readonly] 
**round_id** | **int** | Epoch time (seconds) indicating the start time of the round. | [optional] [readonly] 
**server_ip** | **str** | IP address of target server. | [optional] [readonly] 
**network_profile** | [**NetworkProfile**](NetworkProfile.md) |  | [optional] 
**system_metrics** | [**SystemMetrics**](SystemMetrics.md) |  | [optional] 
**vpn_profile** | [**VpnProfile**](VpnProfile.md) |  | [optional] 
**asn_details** | [**AsnDetails**](AsnDetails.md) |  | [optional] 
**server** | **str** | Target server, including port. | [optional] [readonly] 
**source_ip** | **str** | IP address of source endpoint agent. | [optional] [readonly] 
**source_prefix** | **str** | IP prefix of source endpoint agent. | [optional] [readonly] 
**path_traces** | [**List[PathVisRoute]**](PathVisRoute.md) | Shows iterations of path trace, with each iteration specified by a pathId. | [optional] 
**vpn_path_traces** | [**List[PathVisRoute]**](PathVisRoute.md) | Shows iterations of the VPN path trace, with each iteration specified by a pathId. | [optional] 

## Example

```python
from endpoint_test_results.models.path_vis_detail_test_result import PathVisDetailTestResult

# TODO update the JSON string below
json = "{}"
# create an instance of PathVisDetailTestResult from a JSON string
path_vis_detail_test_result_instance = PathVisDetailTestResult.from_json(json)
# print the JSON string representation of the object
print(PathVisDetailTestResult.to_json())

# convert the object into a dict
path_vis_detail_test_result_dict = path_vis_detail_test_result_instance.to_dict()
# create an instance of PathVisDetailTestResult from a dict
path_vis_detail_test_result_from_dict = PathVisDetailTestResult.from_dict(path_vis_detail_test_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

