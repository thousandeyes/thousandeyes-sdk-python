# GatewayEventGrouping


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip_address** | **str** | Gateway IP address (for gateway events). | [optional] [readonly] 
**mac_address** | **str** | Gateway MAC address (for gateway events). | [optional] [readonly] 

## Example

```python
from thousandeyes_sdk.event_detection.models.gateway_event_grouping import GatewayEventGrouping

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayEventGrouping from a JSON string
gateway_event_grouping_instance = GatewayEventGrouping.from_json(json)
# print the JSON string representation of the object
print(GatewayEventGrouping.to_json())

# convert the object into a dict
gateway_event_grouping_dict = gateway_event_grouping_instance.to_dict()
# create an instance of GatewayEventGrouping from a dict
gateway_event_grouping_from_dict = GatewayEventGrouping.from_dict(gateway_event_grouping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


