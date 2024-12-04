# AgentToAgentProperties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**direction** | [**TestDirection**](TestDirection.md) |  | [optional] 
**dscp** | **str** | DSCP label. | [optional] [readonly] 
**dscp_id** | [**TestDscpId**](TestDscpId.md) |  | [optional] 
**mss** | **int** | Maximum segment size, in bytes. | [optional] 
**num_path_traces** | **int** | Number of path traces executed by the agent. | [optional] [default to 3]
**path_trace_mode** | [**TestPathTraceMode**](TestPathTraceMode.md) |  | [optional] 
**port** | **int** | Target port. | [optional] [default to 49153]
**protocol** | [**AgentToAgentTestProtocol**](AgentToAgentTestProtocol.md) |  | [optional] 
**randomized_start_time** | **bool** | Indicates whether agents should randomize the start time in each test round. | [optional] [default to False]
**target_agent_id** | **str** | &#x60;agentId&#x60; of the target agent for the test. | 
**throughput_measurements** | **bool** | Enable or disable throughput measurements. Throughput measurements cannot be enabled when the source or target of the test is a cloud agent. | [optional] [default to False]
**throughput_duration** | **int** | The throughput duration. | [optional] [default to 10000]
**throughput_rate** | **int** | The throughput rate, only applicable for UDP protocol. | [optional] 
**fixed_packet_rate** | **int** | Sets packets rate sent to measure the network in packets per second. | [optional] 
**type** | **str** |  | [optional] [readonly] 

## Example

```python
from thousandeyes_sdk.instant_tests.models.agent_to_agent_properties import AgentToAgentProperties

# TODO update the JSON string below
json = "{}"
# create an instance of AgentToAgentProperties from a JSON string
agent_to_agent_properties_instance = AgentToAgentProperties.from_json(json)
# print the JSON string representation of the object
print(AgentToAgentProperties.to_json())

# convert the object into a dict
agent_to_agent_properties_dict = agent_to_agent_properties_instance.to_dict()
# create an instance of AgentToAgentProperties from a dict
agent_to_agent_properties_from_dict = AgentToAgentProperties.from_dict(agent_to_agent_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


