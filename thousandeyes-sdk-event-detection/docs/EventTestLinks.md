# EventTestLinks

A links object containing the self link.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**test** | [**Link**](Link.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.event_detection.models.event_test_links import EventTestLinks

# TODO update the JSON string below
json = "{}"
# create an instance of EventTestLinks from a JSON string
event_test_links_instance = EventTestLinks.from_json(json)
# print the JSON string representation of the object
print(EventTestLinks.to_json())

# convert the object into a dict
event_test_links_dict = event_test_links_instance.to_dict()
# create an instance of EventTestLinks from a dict
event_test_links_from_dict = EventTestLinks.from_dict(event_test_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


