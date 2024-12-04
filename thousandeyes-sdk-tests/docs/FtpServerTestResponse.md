# FtpServerTestResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interval** | [**TestInterval**](TestInterval.md) |  | 
**alerts_enabled** | **bool** | Indicates if alerts are enabled. | [optional] 
**enabled** | **bool** | Test is enabled. | [optional] [default to True]
**alert_rules** | [**List[AlertRule]**](AlertRule.md) | Contains list of enabled alert rule objects. | [optional] 
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
**download_limit** | **int** | Specify maximum number of bytes to download from the target object. | [optional] 
**ftp_target_time** | **int** | Target time for operation completion; specified in milliseconds. | [optional] 
**ftp_time_limit** | **int** | Set the time limit for the test in seconds. | [optional] [default to 10]
**mtu_measurements** | **bool** | Set &#x60;true&#x60; to measure MTU sizes on network from agents to the target. | [optional] 
**network_measurements** | **bool** | Enable or disable network measurements. Set to true to enable or false to disable network measurements. | [optional] [default to True]
**num_path_traces** | **int** | Number of path traces executed by the agent. | [optional] [default to 3]
**password** | **str** | Password for Basic/NTLM authentication. | 
**path_trace_mode** | [**TestPathTraceMode**](TestPathTraceMode.md) |  | [optional] 
**probe_mode** | [**TestProbeMode**](TestProbeMode.md) |  | [optional] 
**protocol** | [**TestProtocol**](TestProtocol.md) |  | [optional] 
**randomized_start_time** | **bool** | Indicates whether agents should randomize the start time in each test round. | [optional] [default to False]
**request_type** | [**FtpServerRequestType**](FtpServerRequestType.md) |  | 
**url** | **str** | Target for the test. | 
**use_active_ftp** | **bool** | Explicitly set the flag to use active FTP. | [optional] [default to False]
**use_explicit_ftps** | **bool** | Use explicit FTPS (ftp over SSL). By default, tests will autodetect when it is appropriate to use FTPS. | [optional] 
**username** | **str** | Username for Basic/NTLM authentication. | 
**fixed_packet_rate** | **int** | Sets packets rate sent to measure the network in packets per second. | [optional] 
**ipv6_policy** | [**TestIpv6Policy**](TestIpv6Policy.md) |  | [optional] 
**bgp_measurements** | **bool** | Set to &#x60;true&#x60; to enable bgp measurements. | [optional] [default to True]
**use_public_bgp** | **bool** | Indicate if all available public BGP monitors should be used, when ommited defaults to &#x60;bgpMeasurements&#x60; value. | [optional] [default to True]
**monitors** | [**List[Monitor]**](Monitor.md) | Contains list of enabled BGP monitors. | [optional] [readonly] 
**agents** | [**List[AgentResponse]**](AgentResponse.md) | Contains list of agents. | [optional] 

## Example

```python
from thousandeyes_sdk.tests.models.ftp_server_test_response import FtpServerTestResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FtpServerTestResponse from a JSON string
ftp_server_test_response_instance = FtpServerTestResponse.from_json(json)
# print the JSON string representation of the object
print(FtpServerTestResponse.to_json())

# convert the object into a dict
ftp_server_test_response_dict = ftp_server_test_response_instance.to_dict()
# create an instance of FtpServerTestResponse from a dict
ftp_server_test_response_from_dict = FtpServerTestResponse.from_dict(ftp_server_test_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


