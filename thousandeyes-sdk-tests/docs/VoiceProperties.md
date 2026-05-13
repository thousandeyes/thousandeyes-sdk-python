# VoiceProperties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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
**type** | **str** |  | [optional] [readonly] 

## Example

```python
from thousandeyes_sdk.tests.models.voice_properties import VoiceProperties

# TODO update the JSON string below
json = "{}"
# create an instance of VoiceProperties from a JSON string
voice_properties_instance = VoiceProperties.from_json(json)
# print the JSON string representation of the object
print(VoiceProperties.to_json())

# convert the object into a dict
voice_properties_dict = voice_properties_instance.to_dict()
# create an instance of VoiceProperties from a dict
voice_properties_from_dict = VoiceProperties.from_dict(voice_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


