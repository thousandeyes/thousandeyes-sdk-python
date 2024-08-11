# TestLinks

A links object containing the self link.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**test** | [**Link**](Link.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.event_detection.models.test_links import TestLinks

# TODO update the JSON string below
json = "{}"
# create an instance of TestLinks from a JSON string
test_links_instance = TestLinks.from_json(json)
# print the JSON string representation of the object
print(TestLinks.to_json())

# convert the object into a dict
test_links_dict = test_links_instance.to_dict()
# create an instance of TestLinks from a dict
test_links_from_dict = TestLinks.from_dict(test_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


