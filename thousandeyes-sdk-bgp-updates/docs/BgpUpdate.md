# BgpUpdate

BGP update observed by a BGP monitor.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prefix** | **str** | IP prefix in CIDR notation. | 
**origin_as** | **int** | Origin autonomous system (AS) number. Null when the update has no origin AS, including withdrawals. | 
**as_path** | **List[int]** | AS path for the update. Empty when the update does not carry a path, including withdrawals. | 
**communities** | **List[str]** | BGP communities attached to the update. Empty when the update does not carry communities, including withdrawals. | 
**rpki_status** | [**BgpRpkiStatus**](BgpRpkiStatus.md) | RPKI validation status for the update, using the validation states defined in RFC 6811, Section 2. Returns NotAvailable when the update has no RPKI state, including withdrawals. | 
**update_type** | [**BgpUpdateType**](BgpUpdateType.md) | Type of BGP update. | 
**monitor_id** | **str** | BGP monitor ID that observed the update. Returned by default and omitted when &#x60;expand&#x3D;monitor&#x60; is requested. | [optional] 
**monitor** | [**BgpMonitor**](BgpMonitor.md) | BGP monitor that observed the update. Returned when &#x60;expand&#x3D;monitor&#x60; is requested and replaces &#x60;monitorId&#x60;. | [optional] 
**timestamp** | **datetime** | Date and time when the update was observed. | 

## Example

```python
from thousandeyes_sdk.bgp_updates.models.bgp_update import BgpUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of BgpUpdate from a JSON string
bgp_update_instance = BgpUpdate.from_json(json)
# print the JSON string representation of the object
print(BgpUpdate.to_json())

# convert the object into a dict
bgp_update_dict = bgp_update_instance.to_dict()
# create an instance of BgpUpdate from a dict
bgp_update_from_dict = BgpUpdate.from_dict(bgp_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


