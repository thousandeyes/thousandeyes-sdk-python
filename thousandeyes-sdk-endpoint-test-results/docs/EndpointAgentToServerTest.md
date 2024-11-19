# EndpointAgentToServerTest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aid** | **str** | A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. | [optional] 
**links** | [**EndpointTestLinks**](EndpointTestLinks.md) |  | [optional] 
**agent_selector_config** | [**EndpointAgentSelectorConfig**](EndpointAgentSelectorConfig.md) |  | [optional] 
**created_date** | **datetime** | UTC created date (ISO date-time format). | [optional] [readonly] 
**interval** | [**TestInterval**](TestInterval.md) |  | [optional] 
**is_enabled** | **bool** | Indicates if test is enabled. | [optional] [default to True]
**is_saved_event** | **bool** | Indicates if the test is a saved event. | [optional] [readonly] 
**has_path_trace_in_session** | **bool** | Enables \&quot;in session\&quot; path trace. When enabled, this option initiates a TCP session with the target server and sends path trace packets within the established TCP session. | [optional] 
**modified_date** | **datetime** | UTC last modification date (ISO date-time format). | [optional] [readonly] 
**network_measurements** | **bool** | Enable or disable network measurements. Set to true to enable or false to disable network measurements. | [optional] [default to True]
**protocol** | [**EndpointTestProtocol**](EndpointTestProtocol.md) |  | [optional] 
**ip_version** | [**EndpointIpVersionTemplate**](EndpointIpVersionTemplate.md) |  | [optional] 
**server** | **str** | Target domain name or IP address. | [optional] 
**test_id** | **str** | Each test is assigned a unique ID to access test data from other endpoints. | [optional] [readonly] 
**test_name** | **str** | Name of the test. | [optional] 
**type** | **str** | Type of test being queried. | [readonly] 
**tcp_probe_mode** | [**TestProbeModeResponse**](TestProbeModeResponse.md) |  | [optional] 
**port** | **int** | Port number. | [optional] [default to 443]
**labels** | [**List[TestLabel]**](TestLabel.md) |  | [optional] [readonly] 

## Example

```python
from thousandeyes_sdk.endpoint_test_results.models.endpoint_agent_to_server_test import EndpointAgentToServerTest

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointAgentToServerTest from a JSON string
endpoint_agent_to_server_test_instance = EndpointAgentToServerTest.from_json(json)
# print the JSON string representation of the object
print(EndpointAgentToServerTest.to_json())

# convert the object into a dict
endpoint_agent_to_server_test_dict = endpoint_agent_to_server_test_instance.to_dict()
# create an instance of EndpointAgentToServerTest from a dict
endpoint_agent_to_server_test_from_dict = EndpointAgentToServerTest.from_dict(endpoint_agent_to_server_test_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


