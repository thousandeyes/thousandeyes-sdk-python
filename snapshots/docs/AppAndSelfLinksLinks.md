# AppAndSelfLinksLinks

A links object containing the ThousandEyes App link

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_link** | [**Link**](Link.md) |  | [optional] 
**var_self** | [**Link**](Link.md) |  | [optional] 

## Example

```python
from snapshots.models.app_and_self_links_links import AppAndSelfLinksLinks

# TODO update the JSON string below
json = "{}"
# create an instance of AppAndSelfLinksLinks from a JSON string
app_and_self_links_links_instance = AppAndSelfLinksLinks.from_json(json)
# print the JSON string representation of the object
print(AppAndSelfLinksLinks.to_json())

# convert the object into a dict
app_and_self_links_links_dict = app_and_self_links_links_instance.to_dict()
# create an instance of AppAndSelfLinksLinks from a dict
app_and_self_links_links_from_dict = AppAndSelfLinksLinks.from_dict(app_and_self_links_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


