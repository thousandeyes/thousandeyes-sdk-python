# VpnEventGrouping


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vpn_type** | **str** | VPN type (for vpn events). | [optional] [readonly] 
**vpn_server_ip_address** | **str** | VPN server IP address (for vpn events). | [optional] [readonly] 

## Example

```python
from thousandeyes_sdk.event_detection.models.vpn_event_grouping import VpnEventGrouping

# TODO update the JSON string below
json = "{}"
# create an instance of VpnEventGrouping from a JSON string
vpn_event_grouping_instance = VpnEventGrouping.from_json(json)
# print the JSON string representation of the object
print(VpnEventGrouping.to_json())

# convert the object into a dict
vpn_event_grouping_dict = vpn_event_grouping_instance.to_dict()
# create an instance of VpnEventGrouping from a dict
vpn_event_grouping_from_dict = VpnEventGrouping.from_dict(vpn_event_grouping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


