# NameServerEventGrouping


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**server_name** | **str** | Name server hostname (for name-server events). | [optional] [readonly] 

## Example

```python
from thousandeyes_sdk.event_detection.models.name_server_event_grouping import NameServerEventGrouping

# TODO update the JSON string below
json = "{}"
# create an instance of NameServerEventGrouping from a JSON string
name_server_event_grouping_instance = NameServerEventGrouping.from_json(json)
# print the JSON string representation of the object
print(NameServerEventGrouping.to_json())

# convert the object into a dict
name_server_event_grouping_dict = name_server_event_grouping_instance.to_dict()
# create an instance of NameServerEventGrouping from a dict
name_server_event_grouping_from_dict = NameServerEventGrouping.from_dict(name_server_event_grouping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


