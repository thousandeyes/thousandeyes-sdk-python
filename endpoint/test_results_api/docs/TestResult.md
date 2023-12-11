# TestResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_id** | **str** | Unique ID of endpoint agent, from &#x60;/endpoint/agents&#x60; endpoint. | [optional] [readonly] 
**aid** | [**AccountGroupId**](AccountGroupId.md) |  | [optional] 
**round_id** | **int** | Epoch time (seconds) indicating the start time of the round. | [optional] [readonly] 
**server_ip** | **str** | IP address of target server. | [optional] [readonly] 
**system_metrics** | [**SystemMetrics**](SystemMetrics.md) |  | [optional] 
**vpn_profile** | [**VpnProfile**](VpnProfile.md) |  | [optional] 

## Example

```python
from test_results_api.models.test_result import TestResult

# TODO update the JSON string below
json = "{}"
# create an instance of TestResult from a JSON string
test_result_instance = TestResult.from_json(json)
# print the JSON string representation of the object
print TestResult.to_json()

# convert the object into a dict
test_result_dict = test_result_instance.to_dict()
# create an instance of TestResult from a dict
test_result_form_dict = test_result.from_dict(test_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


