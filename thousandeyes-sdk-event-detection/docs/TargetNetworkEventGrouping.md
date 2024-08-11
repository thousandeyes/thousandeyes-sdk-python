# TargetNetworkEventGrouping


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prefix** | **str** | Prefix value for target-network events. | [optional] [readonly] 

## Example

```python
from thousandeyes_sdk.event_detection.models.target_network_event_grouping import TargetNetworkEventGrouping

# TODO update the JSON string below
json = "{}"
# create an instance of TargetNetworkEventGrouping from a JSON string
target_network_event_grouping_instance = TargetNetworkEventGrouping.from_json(json)
# print the JSON string representation of the object
print(TargetNetworkEventGrouping.to_json())

# convert the object into a dict
target_network_event_grouping_dict = target_network_event_grouping_instance.to_dict()
# create an instance of TargetNetworkEventGrouping from a dict
target_network_event_grouping_from_dict = TargetNetworkEventGrouping.from_dict(target_network_event_grouping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


