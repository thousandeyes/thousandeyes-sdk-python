# WirelessEventGrouping


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ssid** | **str** | Wireless network SSID (for wireless events). | [optional] [readonly] 
**bssid** | **str** | Wireless network BSSID (for wireless events). | [optional] [readonly] 

## Example

```python
from thousandeyes_sdk.event_detection.models.wireless_event_grouping import WirelessEventGrouping

# TODO update the JSON string below
json = "{}"
# create an instance of WirelessEventGrouping from a JSON string
wireless_event_grouping_instance = WirelessEventGrouping.from_json(json)
# print the JSON string representation of the object
print(WirelessEventGrouping.to_json())

# convert the object into a dict
wireless_event_grouping_dict = wireless_event_grouping_instance.to_dict()
# create an instance of WirelessEventGrouping from a dict
wireless_event_grouping_from_dict = WirelessEventGrouping.from_dict(wireless_event_grouping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


