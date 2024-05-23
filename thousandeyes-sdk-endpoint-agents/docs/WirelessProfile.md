# WirelessProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bssid** | **str** |  | [optional] 
**ssid** | **str** |  | [optional] 
**rssi** | **int** |  | [optional] 
**channel** | **int** |  | [optional] 
**phy_mode** | **str** |  | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_agents.models.wireless_profile import WirelessProfile

# TODO update the JSON string below
json = "{}"
# create an instance of WirelessProfile from a JSON string
wireless_profile_instance = WirelessProfile.from_json(json)
# print the JSON string representation of the object
print(WirelessProfile.to_json())

# convert the object into a dict
wireless_profile_dict = wireless_profile_instance.to_dict()
# create an instance of WirelessProfile from a dict
wireless_profile_from_dict = WirelessProfile.from_dict(wireless_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


