# AppLinks

A links object containing the ThousandEyes App link

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_link** | [**Link**](Link.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.test_results.models.app_links import AppLinks

# TODO update the JSON string below
json = "{}"
# create an instance of AppLinks from a JSON string
app_links_instance = AppLinks.from_json(json)
# print the JSON string representation of the object
print(AppLinks.to_json())

# convert the object into a dict
app_links_dict = app_links_instance.to_dict()
# create an instance of AppLinks from a dict
app_links_from_dict = AppLinks.from_dict(app_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


