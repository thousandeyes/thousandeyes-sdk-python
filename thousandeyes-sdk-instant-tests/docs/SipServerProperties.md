# SipServerProperties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mtu_measurements** | **bool** | Set &#x60;true&#x60; to measure MTU sizes on network from agents to the target. | [optional] 
**network_measurements** | **bool** | Enable or disable network measurements. Set to true to enable or false to disable network measurements. | [optional] [default to True]
**num_path_traces** | **int** | Number of path traces executed by the agent. | [optional] [default to 3]
**options_regex** | **str** | Options regex, this field does not require escaping. | [optional] 
**path_trace_mode** | [**TestPathTraceMode**](TestPathTraceMode.md) |  | [optional] 
**probe_mode** | [**TestProbeMode**](TestProbeMode.md) |  | [optional] 
**randomized_start_time** | **bool** | Indicates whether agents should randomize the start time in each test round. | [optional] [default to False]
**register_enabled** | **bool** | Set to true to perform SIP registration on the test target with the SIP REGISTER command. | [optional] [default to False]
**sip_target_time** | **int** | Target time for test completion in milliseconds. | [optional] 
**sip_time_limit** | **int** | Time limit in milliseconds. | [optional] [default to 5]
**fixed_packet_rate** | **int** | Sets packets rate sent to measure the network in packets per second. | [optional] 
**ipv6_policy** | [**TestIpv6Policy**](TestIpv6Policy.md) |  | [optional] 
**type** | **str** |  | [optional] [readonly] 

## Example

```python
from thousandeyes_sdk.instant_tests.models.sip_server_properties import SipServerProperties

# TODO update the JSON string below
json = "{}"
# create an instance of SipServerProperties from a JSON string
sip_server_properties_instance = SipServerProperties.from_json(json)
# print the JSON string representation of the object
print(SipServerProperties.to_json())

# convert the object into a dict
sip_server_properties_dict = sip_server_properties_instance.to_dict()
# create an instance of SipServerProperties from a dict
sip_server_properties_from_dict = SipServerProperties.from_dict(sip_server_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


