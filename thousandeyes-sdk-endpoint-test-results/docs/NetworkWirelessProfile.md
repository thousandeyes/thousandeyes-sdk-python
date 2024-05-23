# NetworkWirelessProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ssid** | **str** | Wireless network SSID. | [optional] [readonly] 
**bssid** | **str** | Wireless network BSSID. | [optional] [readonly] 
**channel** | **int** | Wireless network channel. | [optional] [readonly] 
**phy_mode** | **str** | Wireless network PHY mode. | [optional] [readonly] 
**rssi** | **int** | Wireless network RSSI. | [optional] [readonly] 
**noise** | **int** | Wireless network noise. | [optional] [readonly] 
**quality** | **int** | Wireless network quality. | [optional] [readonly] 
**tx_rate** | **int** | Wireless network transmitted rate. | [optional] [readonly] 
**vendor** | **str** | Wireless network device vendor. | [optional] [readonly] 

## Example

```python
from thousandeyes_sdk.endpoint_test_results.models.network_wireless_profile import NetworkWirelessProfile

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkWirelessProfile from a JSON string
network_wireless_profile_instance = NetworkWirelessProfile.from_json(json)
# print the JSON string representation of the object
print(NetworkWirelessProfile.to_json())

# convert the object into a dict
network_wireless_profile_dict = network_wireless_profile_instance.to_dict()
# create an instance of NetworkWirelessProfile from a dict
network_wireless_profile_from_dict = NetworkWirelessProfile.from_dict(network_wireless_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


