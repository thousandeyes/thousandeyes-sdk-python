# DynamicTestRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aid** | **str** | A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. | [optional] 
**links** | [**DynamicTestLinks**](DynamicTestLinks.md) |  | [optional] 
**agent_selector_config** | [**EndpointAgentSelectorConfig**](EndpointAgentSelectorConfig.md) |  | [optional] 
**application** | **str** | Which supported application to monitor, can be one of &#x60;webex&#x60;, &#x60;zoom&#x60;, &#x60;microsoft-teams&#x60;. | [optional] 
**created_date** | **datetime** | UTC created date (ISO date-time format). | [optional] [readonly] 
**interval** | [**TestInterval**](TestInterval.md) |  | [optional] 
**is_enabled** | **bool** | Indicates if test is enabled. | [optional] [default to True]
**has_path_trace_in_session** | **bool** | Enables \&quot;in session\&quot; path trace. When enabled, this option initiates a TCP session with the target server and sends path trace packets within the established TCP session. | [optional] 
**has_ping** | **bool** | Optional flag indicating if the test should run ping. | [optional] [default to True]
**has_traceroute** | **bool** | Optional flag indicating if the test should run traceroute. | [optional] [default to True]
**modified_date** | **datetime** | UTC last modification date (ISO date-time format). | [optional] [readonly] 
**network_measurements** | **bool** | Enable or disable network measurements. Set to true to enable or false to disable network measurements. | [optional] [default to True]
**protocol** | [**EndpointTestProtocol**](EndpointTestProtocol.md) |  | [optional] 
**tcp_probe_mode** | [**TestProbeModeResponse**](TestProbeModeResponse.md) |  | [optional] 
**test_id** | **str** | Each test is assigned a unique ID; this is used to access test information and results from other endpoints. | [optional] [readonly] 
**test_name** | **str** | Name of the test. | [optional] 
**labels** | [**List[TestLabel]**](TestLabel.md) |  | [optional] [readonly] 
**agent_selector_type** | [**EndpointTestAgentSelectorType**](EndpointTestAgentSelectorType.md) |  | [optional] 
**agents** | **List[str]** | List of endpoint agent IDs (obtained from &#x60;/endpoint/agents&#x60; endpoint). Required when &#x60;agentSelectorType&#x60; is set to &#x60;specific-agent&#x60;. | [optional] 
**endpoint_agent_labels** | **List[str]** | List of endpoint agent label IDs (obtained from &#x60;/endpoint/labels&#x60; endpoint), required when &#x60;agentSelectorType&#x60; is set to &#x60;agent-labels&#x60;. | [optional] 
**max_machines** | **int** | Maximum number of agents which can execute this test. | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_tests.models.dynamic_test_request import DynamicTestRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DynamicTestRequest from a JSON string
dynamic_test_request_instance = DynamicTestRequest.from_json(json)
# print the JSON string representation of the object
print(DynamicTestRequest.to_json())

# convert the object into a dict
dynamic_test_request_dict = dynamic_test_request_instance.to_dict()
# create an instance of DynamicTestRequest from a dict
dynamic_test_request_from_dict = DynamicTestRequest.from_dict(dynamic_test_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


