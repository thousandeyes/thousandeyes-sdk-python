# EndpointVpnLogItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**log_item_type** | [**EndpointVpnLogItemType**](EndpointVpnLogItemType.md) |  | [optional] 
**vpn_type** | [**EndpointVpnType**](EndpointVpnType.md) |  | [optional] 
**vpn_server_name** | **str** | VPN server name. | [optional] [readonly] 
**vpn_server_address** | **str** | VPN server address. | [optional] [readonly] 

## Example

```python
from thousandeyes_sdk.endpoint_agents.models.endpoint_vpn_log_item import EndpointVpnLogItem

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointVpnLogItem from a JSON string
endpoint_vpn_log_item_instance = EndpointVpnLogItem.from_json(json)
# print the JSON string representation of the object
print(EndpointVpnLogItem.to_json())

# convert the object into a dict
endpoint_vpn_log_item_dict = endpoint_vpn_log_item_instance.to_dict()
# create an instance of EndpointVpnLogItem from a dict
endpoint_vpn_log_item_from_dict = EndpointVpnLogItem.from_dict(endpoint_vpn_log_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


