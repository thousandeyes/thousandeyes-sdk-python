# PathVisTestResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_id** | **str** | Unique ID of endpoint agent, from &#x60;/endpoint/agents&#x60; endpoint. | [optional] [readonly] 
**aid** | [**AccountGroupId**](AccountGroupId.md) |  | [optional] 
**round_id** | **int** | Epoch time (seconds) indicating the start time of the round. | [optional] [readonly] 
**server_ip** | **str** | IP address of target server. | [optional] [readonly] 
**system_metrics** | [**SystemMetrics**](SystemMetrics.md) |  | [optional] 
**vpn_profile** | [**VpnProfile**](VpnProfile.md) |  | [optional] 
**asn_details** | [**AsnDetails**](AsnDetails.md) |  | [optional] 
**server** | **str** | Target server, including port. | [optional] [readonly] 
**source_ip** | **str** | IP address of source endpoint agent. | [optional] [readonly] 
**source_prefix** | **str** | IP prefix of source endpoint agent. | [optional] [readonly] 
**location** | **str** | Geographic location of the pathvis. | [optional] [readonly] 
**endpoints** | [**List[PathVisEndpoint]**](PathVisEndpoint.md) | Shows an iteration of path trace, with each iteration specified by a pathId. | [optional] 

## Example

```python
from test_results_api.models.path_vis_test_result import PathVisTestResult

# TODO update the JSON string below
json = "{}"
# create an instance of PathVisTestResult from a JSON string
path_vis_test_result_instance = PathVisTestResult.from_json(json)
# print the JSON string representation of the object
print PathVisTestResult.to_json()

# convert the object into a dict
path_vis_test_result_dict = path_vis_test_result_instance.to_dict()
# create an instance of PathVisTestResult from a dict
path_vis_test_result_form_dict = path_vis_test_result.from_dict(path_vis_test_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


