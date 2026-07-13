# EndpointProxy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**proxy_id** | **str** | Unique ID of the proxy setting. | [optional] [readonly] 
**name** | **str** | Proxy setting name. | [optional] [readonly] 
**type** | [**EndpointProxyType**](EndpointProxyType.md) |  | [optional] 
**host** | **str** | Static proxy host name or IP address. | [optional] [readonly] 
**port** | **int** | Static proxy port. | [optional] [readonly] 
**pac** | **str** | PAC URL or PAC script location. | [optional] [readonly] 
**user_name** | **str** | Proxy authentication user name. | [optional] [readonly] 
**bypass_list** | **str** | Comma-separated proxy bypass list. | [optional] [readonly] 
**auth_type** | [**EndpointProxyAuthType**](EndpointProxyAuthType.md) |  | [optional] 
**agent_ids** | **List[str]** | Endpoint Agent IDs assigned to the proxy setting. | [optional] 
**test_ids** | **List[str]** | Endpoint scheduled test IDs assigned to the proxy setting. | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_agents.models.endpoint_proxy import EndpointProxy

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointProxy from a JSON string
endpoint_proxy_instance = EndpointProxy.from_json(json)
# print the JSON string representation of the object
print(EndpointProxy.to_json())

# convert the object into a dict
endpoint_proxy_dict = endpoint_proxy_instance.to_dict()
# create an instance of EndpointProxy from a dict
endpoint_proxy_from_dict = EndpointProxy.from_dict(endpoint_proxy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


