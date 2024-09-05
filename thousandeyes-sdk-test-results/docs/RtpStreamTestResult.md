# RtpStreamTestResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **datetime** | Data point date UTC (ISO date-time format). | [optional] [readonly] 
**round_id** | **int** | Epoch time (seconds) indicating the start time of the round | [optional] [readonly] 
**links** | [**TestResultAppLinks**](TestResultAppLinks.md) |  | [optional] 
**start_time** | **int** | Epoch time (seconds) indicating the start time of the round | [optional] [readonly] 
**end_time** | **int** | Epoch time (seconds) indicating the end time of the round | [optional] [readonly] 
**agent** | [**TestResultAgent**](TestResultAgent.md) |  | [optional] 
**server_ip** | **str** | Target agent IP address | [optional] [readonly] 
**dscp** | **str** | DSCP value received by the server from the agent | [optional] [readonly] 
**dscp_name** | **str** | Name of DSCP value received by the server from the agent | [optional] [readonly] 
**mos** | **float** | Mean opinion score for agent’s stream | [optional] [readonly] 
**codec_name** | **str** | Name of codec used by agen | [optional] [readonly] 
**codec_max_mos** | **float** | Maximum value of Mean Opinion Score based on codec selection | [optional] [readonly] 
**loss** | **float** | Percentage value of packets sent from agent not received by server | [optional] [readonly] 
**discards** | **float** | Percentage of packets discarded | [optional] [readonly] 
**latency** | **int** | Time to send packets from source to server in milliseconds | [optional] [readonly] 
**pdv** | **int** | Variation in packet delay in milliseconds | [optional] [readonly] 
**error_detail** | **str** | Error details, if an error was encountered | [optional] [readonly] 

## Example

```python
from thousandeyes_sdk.test_results.models.rtp_stream_test_result import RtpStreamTestResult

# TODO update the JSON string below
json = "{}"
# create an instance of RtpStreamTestResult from a JSON string
rtp_stream_test_result_instance = RtpStreamTestResult.from_json(json)
# print the JSON string representation of the object
print(RtpStreamTestResult.to_json())

# convert the object into a dict
rtp_stream_test_result_dict = rtp_stream_test_result_instance.to_dict()
# create an instance of RtpStreamTestResult from a dict
rtp_stream_test_result_from_dict = RtpStreamTestResult.from_dict(rtp_stream_test_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


