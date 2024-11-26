# VoiceProperties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**codec** | **str** | Codec label | [optional] [readonly] 
**codec_id** | **str** | Coded ID, [see the list of acceptable values](https://docs.thousandeyes.com/product-documentation/internet-and-wan-monitoring/tests/working-with-test-settings#rtp-stream-advanced-settings-tab) | [optional] 
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
from thousandeyes_sdk.instant_tests.models.voice_properties import VoiceProperties

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


