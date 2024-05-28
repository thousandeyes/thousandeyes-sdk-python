# EndpointRealUserTestResultRequestFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location** | **List[str]** | Location of the endpoint agent. | [optional] 
**connection** | [**List[InterfaceHardwareType]**](InterfaceHardwareType.md) |  | [optional] 
**platform** | [**List[Platform]**](Platform.md) |  | [optional] 
**gateway** | **List[str]** | Endpoint agent default gateway IP address. | [optional] 
**proxy_target** | **List[str]** | Endpoint agent proxy IP address. | [optional] 
**vpn_target** | **List[str]** | Endpoint agent VPN endpoint IP address. | [optional] 
**agent_id** | **List[str]** | Endpoint agent ID. | [optional] 
**network_id** | **List[str]** | Network ID. | [optional] 
**ssid** | **List[str]** | WiFi SSID. | [optional] 
**bssid** | **List[str]** | WiFi BSSID. | [optional] 
**destination_ip** | **List[str]** | Web site destination IP address. | [optional] 
**domain** | **List[str]** | Web site base domain visited during the session. | [optional] 
**trigger** | [**List[Trigger]**](Trigger.md) | Real user test trigger. | [optional] 
**visited_site** | **List[str]** | Web site domain visited during the session. | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_test_results.models.endpoint_real_user_test_result_request_filter import EndpointRealUserTestResultRequestFilter

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointRealUserTestResultRequestFilter from a JSON string
endpoint_real_user_test_result_request_filter_instance = EndpointRealUserTestResultRequestFilter.from_json(json)
# print the JSON string representation of the object
print(EndpointRealUserTestResultRequestFilter.to_json())

# convert the object into a dict
endpoint_real_user_test_result_request_filter_dict = endpoint_real_user_test_result_request_filter_instance.to_dict()
# create an instance of EndpointRealUserTestResultRequestFilter from a dict
endpoint_real_user_test_result_request_filter_from_dict = EndpointRealUserTestResultRequestFilter.from_dict(endpoint_real_user_test_result_request_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

