# VoiceInstantTestRequest


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
**labels** | **List[str]** | A list of test label identifiers (get &#x60;labelId&#x60; from &#x60;/labels&#x60; endpoint). | [optional] 
**shared_with_accounts** | **List[str]** | A list of account group identifiers that the test is shared with (get &#x60;aid&#x60; from &#x60;/account-groups&#x60; endpoint). | [optional] 
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
**agents** | [**List[TestAgent]**](TestAgent.md) | A list of objects with &#x60;agentId&#x60; (required) and &#x60;sourceIpAddress&#x60; (optional). | 

## Example

```python
from thousandeyes_sdk.instant_tests.models.voice_instant_test_request import VoiceInstantTestRequest

# TODO update the JSON string below
json = "{}"
# create an instance of VoiceInstantTestRequest from a JSON string
voice_instant_test_request_instance = VoiceInstantTestRequest.from_json(json)
# print the JSON string representation of the object
print(VoiceInstantTestRequest.to_json())

# convert the object into a dict
voice_instant_test_request_dict = voice_instant_test_request_instance.to_dict()
# create an instance of VoiceInstantTestRequest from a dict
voice_instant_test_request_from_dict = VoiceInstantTestRequest.from_dict(voice_instant_test_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


