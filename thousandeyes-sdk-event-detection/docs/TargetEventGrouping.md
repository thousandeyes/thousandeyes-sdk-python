# TargetEventGrouping


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target** | **str** | Target name (for target events). | [optional] [readonly] 

## Example

```python
from thousandeyes_sdk.event_detection.models.target_event_grouping import TargetEventGrouping

# TODO update the JSON string below
json = "{}"
# create an instance of TargetEventGrouping from a JSON string
target_event_grouping_instance = TargetEventGrouping.from_json(json)
# print the JSON string representation of the object
print(TargetEventGrouping.to_json())

# convert the object into a dict
target_event_grouping_dict = target_event_grouping_instance.to_dict()
# create an instance of TargetEventGrouping from a dict
target_event_grouping_from_dict = TargetEventGrouping.from_dict(target_event_grouping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


