# UnexpandedVoiceTest


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
**saved_event** | **bool** | Indicates if the test is a saved event.  **Note**: **Saved Events** are now called **Private Snapshots** in the user interface. This change does not affect API.  | [optional] [readonly] 
**test_id** | **str** | Each test is assigned an unique ID; this is used to access test information and results from other endpoints. | [optional] [readonly] 
**test_name** | **str** | The name of the test. Test name must be unique. | [optional] 
**type** | **str** |  | [optional] [readonly] 
**links** | [**TestLinks**](TestLinks.md) |  | [optional] 
**codec** | **str** | Codec label | [optional] [readonly] 
**codec_id** | **str** | Codec identifier for the RTP stream. Valid values:  * &#x60;0&#x60;: G.711 @ 64 Kbps * &#x60;1&#x60;: G.722.1 @ 24 Kbps (WB) * &#x60;2&#x60;: G.722.1 @ 32 Kbps (WB) * &#x60;3&#x60;: G.726 @ 32 Kbps * &#x60;4&#x60;: G.723.1 @ 6.4 Kbps * &#x60;5&#x60;: G.729a @ 8 Kbps * &#x60;6&#x60;: RTAudio @ 45 Kbps (WB) * &#x60;7&#x60;: RTAudio @ 27.8 Kbps * &#x60;8&#x60;: SILK @ 36 Kbps (WB) * &#x60;9&#x60;: G.722 @ 64 Kbps (WB)  | [optional] 
**dscp** | **str** | DSCP label. | [optional] [readonly] 
**dscp_id** | [**TestDscpId**](TestDscpId.md) |  | [optional] 
**duration** | **int** | Duration of the test in seconds. | [optional] [default to 5]
**jitter_buffer** | **int** | De-jitter buffer size in seconds. | [optional] [default to 40]
**num_path_traces** | **int** | Number of path traces executed by the agent. | [optional] [default to 3]
**port** | **int** | Port number for the chosen protocol. | [optional] 
**randomized_start_time** | **bool** | Indicates whether agents should randomize the start time in each test round. | [optional] [default to False]
**target_agent_id** | **str** | Agent ID of the target agent for the test. | 
**bgp_measurements** | **bool** | Set to &#x60;true&#x60; to enable bgp measurements. | [optional] [default to True]
**use_public_bgp** | **bool** | Indicate if all available public BGP monitors should be used, when ommited defaults to &#x60;bgpMeasurements&#x60; value. | [optional] [default to True]

## Example

```python
from thousandeyes_sdk.tests.models.unexpanded_voice_test import UnexpandedVoiceTest

# TODO update the JSON string below
json = "{}"
# create an instance of UnexpandedVoiceTest from a JSON string
unexpanded_voice_test_instance = UnexpandedVoiceTest.from_json(json)
# print the JSON string representation of the object
print(UnexpandedVoiceTest.to_json())

# convert the object into a dict
unexpanded_voice_test_dict = unexpanded_voice_test_instance.to_dict()
# create an instance of UnexpandedVoiceTest from a dict
unexpanded_voice_test_from_dict = UnexpandedVoiceTest.from_dict(unexpanded_voice_test_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


