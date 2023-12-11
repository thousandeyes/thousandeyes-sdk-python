# DynamicTest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**DynamicTestLinks**](DynamicTestLinks.md) |  | [optional] 
**agent_selector_config** | [**EndpointAgentSelectorConfig**](EndpointAgentSelectorConfig.md) |  | [optional] 
**application** | [**DynamicTestApplication**](DynamicTestApplication.md) |  | [optional] 
**created_date** | **datetime** | UTC created date (ISO date-time format). | [optional] [readonly] 
**interval** | [**TestInterval**](TestInterval.md) |  | [optional] 
**is_enabled** | **bool** | Indicates if test is enabled. | [optional] [readonly] [default to True]
**has_path_trace_in_session** | **bool** | Enables \&quot;in session\&quot; path trace. When enabled, this option initiates a TCP session with the target server and sends path trace packets within the established TCP session. | [optional] [readonly] 
**has_ping** | **bool** | Optional flag indicating if the test should run ping. | [optional] [default to True]
**has_traceroute** | **bool** | Optional flag indicating if the test should run traceroute. | [optional] [default to True]
**modified_date** | **datetime** | UTC last modification date (ISO date-time format). | [optional] [readonly] 
**network_measurements** | **bool** | Enable or disable network measurements. Set to true to enable or false to disable network measurements. | [optional] [readonly] 
**protocol** | [**EndpointTestProtocol**](EndpointTestProtocol.md) |  | [optional] 
**tcp_probe_mode** | [**TestProbeMode**](TestProbeMode.md) |  | [optional] [readonly] 
**test_id** | **str** | Each test is assigned a unique ID; this is used to access test information and results from other endpoints. | [optional] [readonly] 
**aid** | [**EndpointTestAid**](EndpointTestAid.md) |  | [optional] 
**test_name** | **str** | Name of the test. | [optional] 

## Example

```python
from tests_api.models.dynamic_test import DynamicTest

# TODO update the JSON string below
json = "{}"
# create an instance of DynamicTest from a JSON string
dynamic_test_instance = DynamicTest.from_json(json)
# print the JSON string representation of the object
print DynamicTest.to_json()

# convert the object into a dict
dynamic_test_dict = dynamic_test_instance.to_dict()
# create an instance of DynamicTest from a dict
dynamic_test_form_dict = dynamic_test.from_dict(dynamic_test_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


