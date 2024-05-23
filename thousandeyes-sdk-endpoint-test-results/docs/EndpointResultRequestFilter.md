# EndpointResultRequestFilter


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

## Example

```python
from thousandeyes_sdk.endpoint_test_results.models.endpoint_result_request_filter import EndpointResultRequestFilter

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointResultRequestFilter from a JSON string
endpoint_result_request_filter_instance = EndpointResultRequestFilter.from_json(json)
# print the JSON string representation of the object
print(EndpointResultRequestFilter.to_json())

# convert the object into a dict
endpoint_result_request_filter_dict = endpoint_result_request_filter_instance.to_dict()
# create an instance of EndpointResultRequestFilter from a dict
endpoint_result_request_filter_from_dict = EndpointResultRequestFilter.from_dict(endpoint_result_request_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


