# UnexpandedAgentToAgentTest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interval** | [**TestInterval**](TestInterval.md) |  | 
**alerts_enabled** | **bool** | Indicates if alerts are enabled. | [optional] 
**enabled** | **bool** | Test is enabled. | [optional] [default to True]
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
**bgp_measurements** | **bool** | Set to &#x60;true&#x60; to enable bgp measurements. | [optional] [default to True]
**use_public_bgp** | **bool** | Indicate if all available public BGP monitors should be used, when ommited defaults to &#x60;bgpMeasurements&#x60; value. | [optional] [default to True]

## Example

```python
from thousandeyes_sdk.tests.models.unexpanded_agent_to_agent_test import UnexpandedAgentToAgentTest

# TODO update the JSON string below
json = "{}"
# create an instance of UnexpandedAgentToAgentTest from a JSON string
unexpanded_agent_to_agent_test_instance = UnexpandedAgentToAgentTest.from_json(json)
# print the JSON string representation of the object
print(UnexpandedAgentToAgentTest.to_json())

# convert the object into a dict
unexpanded_agent_to_agent_test_dict = unexpanded_agent_to_agent_test_instance.to_dict()
# create an instance of UnexpandedAgentToAgentTest from a dict
unexpanded_agent_to_agent_test_from_dict = UnexpandedAgentToAgentTest.from_dict(unexpanded_agent_to_agent_test_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


