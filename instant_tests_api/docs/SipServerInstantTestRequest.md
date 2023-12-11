# SipServerInstantTestRequest


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
**links** | [**UnexpandedInstantTestLinks**](UnexpandedInstantTestLinks.md) |  | [optional] 
**labels** | **List[str]** | A list of test label identifiers (get &#x60;labelId&#x60; from &#x60;/labels&#x60; endpoint). | [optional] 
**shared_with_accounts** | **List[str]** | A list of account group identifiers that the test is shared with (get &#x60;aid&#x60; from &#x60;/account-groups&#x60; endpoint). | [optional] 
**agents** | [**List[InstantTestRequestAgentsInner]**](InstantTestRequestAgentsInner.md) | A list of objects with &#x60;agentId&#x60; (required) and &#x60;sourceIpAddress&#x60; (optional). | 
**auth_user** | **str** | Username for authentication with SIP server. | [optional] 
**mtu_measurements** | **bool** | Set &#x60;true&#x60; to measure MTU sizes on network from agents to the target. | [optional] 
**network_measurements** | **bool** | Enable or disable network measurements. Set to true to enable or false to disable network measurements. | [optional] [default to True]
**options_regex** | **str** | Options regex, this field does not require escaping. | [optional] 
**password** | **str** | Password for Basic/NTLM authentication. | [optional] 
**path_trace_mode** | [**TestPathTraceMode**](TestPathTraceMode.md) |  | [optional] 
**port** | **int** | Target port. | [default to 49153]
**protocol** | [**SipTestProtocol**](SipTestProtocol.md) |  | [optional] 
**register_enabled** | **bool** | Set to true to perform SIP registration on the test target with the SIP REGISTER command. | [optional] [default to False]
**sip_registrar** | **str** | SIP server to be tested, specified by domain name or IP address. | [optional] 
**sip_target_time** | **int** | Target time for test completion in milliseconds. | [optional] 
**sip_time_limit** | **int** | Time limit in milliseconds. | [optional] [default to 5]
**target_sip_credentials** | [**TestSipCredentials**](TestSipCredentials.md) |  | 
**user** | **str** | Username for SIP registration, should be unique within a ThousandEyes account group. | [optional] 
**fixed_packet_rate** | **int** | Sets packets rate sent to measure the network in packets per second. | [optional] 
**ipv6_policy** | [**TestIpv6Policy**](TestIpv6Policy.md) |  | [optional] 

## Example

```python
from instant_tests_api.models.sip_server_instant_test_request import SipServerInstantTestRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SipServerInstantTestRequest from a JSON string
sip_server_instant_test_request_instance = SipServerInstantTestRequest.from_json(json)
# print the JSON string representation of the object
print SipServerInstantTestRequest.to_json()

# convert the object into a dict
sip_server_instant_test_request_dict = sip_server_instant_test_request_instance.to_dict()
# create an instance of SipServerInstantTestRequest from a dict
sip_server_instant_test_request_form_dict = sip_server_instant_test_request.from_dict(sip_server_instant_test_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


