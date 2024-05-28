# SelfLinks

A links object containing the self link.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | [**Link**](Link.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.usage.models.self_links import SelfLinks

# TODO update the JSON string below
json = "{}"
# create an instance of SelfLinks from a JSON string
self_links_instance = SelfLinks.from_json(json)
# print the JSON string representation of the object
print(SelfLinks.to_json())

# convert the object into a dict
self_links_dict = self_links_instance.to_dict()
# create an instance of SelfLinks from a dict
self_links_from_dict = SelfLinks.from_dict(self_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

