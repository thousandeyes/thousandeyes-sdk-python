# AgentToServerInstantTest


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
**bandwidth_measurements** | **bool** | Set to &#x60;true&#x60; to enable bandwidth measurements, only applies to Enterprise agents assigned to the test. | [optional] 
**continuous_mode** | **bool** | To enable continuous monitoring, set this parameter to &#x60;true&#x60; to.  When continuous monitoring is enabled, the following actions occur: * &#x60;fixedPacketRate&#x60; is enforced * &#x60;bandwidthMeasurements&#x60; are disabled * If the &#x60;protocol&#x60; is set to &#x60;tcp&#x60;, &#x60;probeMode&#x60; is set to &#x60;syn&#x60;.  | [optional] 
**fixed_packet_rate** | **int** | If continuousMode is &#x60;false&#x60;, set the fixedPacketRate to a value between 10-100. If &#x60;continuousMode&#x60; is &#x60;true&#x60;, set the &#x60;fixedPacketRate&#x60; to &#x60;1&#x60; | [optional] 
**mtu_measurements** | **bool** | Set &#x60;true&#x60; to measure MTU sizes on network from agents to the target. | [optional] 
**num_path_traces** | **int** | Number of path traces executed by the agent. | [optional] [default to 3]
**path_trace_mode** | [**TestPathTraceMode**](TestPathTraceMode.md) |  | [optional] 
**port** | **int** | Target port. | [optional] [default to 49153]
**probe_mode** | [**TestProbeMode**](TestProbeMode.md) |  | [optional] 
**protocol** | [**TestProtocol**](TestProtocol.md) |  | [optional] 
**randomized_start_time** | **bool** | Indicates whether agents should randomize the start time in each test round. | [optional] [default to False]
**server** | **str** | Target name or IP address. | 
**dscp** | **str** | DSCP label. | [optional] [readonly] 
**dscp_id** | [**TestDscpId**](TestDscpId.md) |  | [optional] 
**ipv6_policy** | [**TestIpv6Policy**](TestIpv6Policy.md) |  | [optional] 
**ping_payload_size** | **int** | Payload size (not total packet size) for the end-to-end metric&#39;s probes, ping payload size allows values from 0 to 1400 bytes. When set to null, payload sizes are 0 bytes for ICMP-based tests and 1 byte for TCP-based tests. | [optional] 
**network_measurements** | **bool** | View packet loss in 1-second intervals. This is only available for 1-minute interval tests. Set to &#x60;true&#x60; to enable network measurements. | [optional] [default to False]

## Example

```python
from thousandeyes_sdk.tests.models.agent_to_server_instant_test import AgentToServerInstantTest

# TODO update the JSON string below
json = "{}"
# create an instance of AgentToServerInstantTest from a JSON string
agent_to_server_instant_test_instance = AgentToServerInstantTest.from_json(json)
# print the JSON string representation of the object
print(AgentToServerInstantTest.to_json())

# convert the object into a dict
agent_to_server_instant_test_dict = agent_to_server_instant_test_instance.to_dict()
# create an instance of AgentToServerInstantTest from a dict
agent_to_server_instant_test_from_dict = AgentToServerInstantTest.from_dict(agent_to_server_instant_test_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


