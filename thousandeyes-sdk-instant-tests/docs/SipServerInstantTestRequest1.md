# SipServerInstantTestRequest1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_by** | **str** | User that created the test. | [optional] [readonly] 
**created_date** | **datetime** | UTC created date (ISO date-time format). | [optional] [readonly] 
**description** | **str** | A description of the test. | [optional] 
**live_share** | **bool** | Indicates if the test is shared with the account group. | [optional] [readonly] 
**modified_by** | **str** | User that modified the test. | [optional] [readonly] 
**modified_date** | **datetime** | UTC last modification date (ISO date-time format). | [optional] [readonly] 
**saved_event** | **bool** | Indicates if the test is a saved event. | [optional] [readonly] 
**test_id** | **str** | Each test is assigned an unique ID; this is used to access test information and results from other endpoints. | [optional] [readonly] 
**test_name** | **str** | The name of the test. Test name must be unique. | [optional] 
**type** | **str** |  | [optional] [readonly] 
**links** | [**TestLinks**](TestLinks.md) |  | [optional] 
**labels** | [**List[TestLabel]**](TestLabel.md) |  | [optional] [readonly] 
**shared_with_accounts** | [**List[SharedWithAccount]**](SharedWithAccount.md) |  | [optional] [readonly] 
**mtu_measurements** | **bool** | Set &#x60;true&#x60; to measure MTU sizes on network from agents to the target. | [optional] 
**network_measurements** | **bool** | Enable or disable network measurements. Set to true to enable or false to disable network measurements. | [optional] [default to True]
**num_path_traces** | **int** | Number of path traces executed by the agent. | [optional] [default to 3]
**options_regex** | **str** | Options regex, this field does not require escaping. | [optional] 
**path_trace_mode** | [**TestPathTraceMode**](TestPathTraceMode.md) |  | [optional] 
**probe_mode** | [**TestProbeMode**](TestProbeMode.md) |  | [optional] 
**register_enabled** | **bool** | Set to true to perform SIP registration on the test target with the SIP REGISTER command. | [optional] [default to False]
**sip_target_time** | **int** | Target time for test completion in milliseconds. | [optional] 
**sip_time_limit** | **int** | Time limit in milliseconds. | [optional] [default to 5]
**fixed_packet_rate** | **int** | Sets packets rate sent to measure the network in packets per second. | [optional] 
**ipv6_policy** | [**TestIpv6Policy**](TestIpv6Policy.md) |  | [optional] 
**agents** | [**List[Agent]**](Agent.md) | Contains list of agents. | [optional] [readonly] 
**target_sip_credentials** | [**TestSipCredentials**](TestSipCredentials.md) |  | 

## Example

```python
from thousandeyes_sdk.instant_tests.models.sip_server_instant_test_request1 import SipServerInstantTestRequest1

# TODO update the JSON string below
json = "{}"
# create an instance of SipServerInstantTestRequest1 from a JSON string
sip_server_instant_test_request1_instance = SipServerInstantTestRequest1.from_json(json)
# print the JSON string representation of the object
print(SipServerInstantTestRequest1.to_json())

# convert the object into a dict
sip_server_instant_test_request1_dict = sip_server_instant_test_request1_instance.to_dict()
# create an instance of SipServerInstantTestRequest1 from a dict
sip_server_instant_test_request1_from_dict = SipServerInstantTestRequest1.from_dict(sip_server_instant_test_request1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


