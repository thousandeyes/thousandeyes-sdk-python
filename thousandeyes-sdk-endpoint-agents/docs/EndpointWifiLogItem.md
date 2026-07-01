# EndpointWifiLogItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**log_item_type** | [**EndpointWifiLogItemType**](EndpointWifiLogItemType.md) |  | [optional] 
**ssid** | **str** | Wireless network SSID. | [optional] [readonly] 
**bssid** | **str** | Wireless access point BSSID. | [optional] [readonly] 
**bssid_from** | **str** | Previous wireless access point BSSID. | [optional] [readonly] 
**channel** | **str** | Wireless channel. | [optional] [readonly] 
**channel_from** | **str** | Previous wireless channel. | [optional] [readonly] 
**physical_mode** | **str** | Wireless physical mode. | [optional] [readonly] 
**physical_mode_from** | **str** | Previous wireless physical mode. | [optional] [readonly] 
**failure** | [**EndpointWirelessConnectionFailure**](EndpointWirelessConnectionFailure.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_agents.models.endpoint_wifi_log_item import EndpointWifiLogItem

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointWifiLogItem from a JSON string
endpoint_wifi_log_item_instance = EndpointWifiLogItem.from_json(json)
# print the JSON string representation of the object
print(EndpointWifiLogItem.to_json())

# convert the object into a dict
endpoint_wifi_log_item_dict = endpoint_wifi_log_item_instance.to_dict()
# create an instance of EndpointWifiLogItem from a dict
endpoint_wifi_log_item_from_dict = EndpointWifiLogItem.from_dict(endpoint_wifi_log_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


