# ApplicationEventGrouping


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fqdn** | **str** | Fully qualified domain name of the application (for application events). | [optional] [readonly] 

## Example

```python
from thousandeyes_sdk.event_detection.models.application_event_grouping import ApplicationEventGrouping

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationEventGrouping from a JSON string
application_event_grouping_instance = ApplicationEventGrouping.from_json(json)
# print the JSON string representation of the object
print(ApplicationEventGrouping.to_json())

# convert the object into a dict
application_event_grouping_dict = application_event_grouping_instance.to_dict()
# create an instance of ApplicationEventGrouping from a dict
application_event_grouping_from_dict = ApplicationEventGrouping.from_dict(application_event_grouping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


