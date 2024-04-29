# AlertLinksLinks

An object containing the alert links.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**test** | [**Link**](Link.md) |  | [optional] 
**rule** | [**Link**](Link.md) |  | [optional] 
**app_link** | [**Link**](Link.md) |  | [optional] 
**var_self** | [**Link**](Link.md) |  | [optional] 

## Example

```python
from alerts.models.alert_links_links import AlertLinksLinks

# TODO update the JSON string below
json = "{}"
# create an instance of AlertLinksLinks from a JSON string
alert_links_links_instance = AlertLinksLinks.from_json(json)
# print the JSON string representation of the object
print(AlertLinksLinks.to_json())

# convert the object into a dict
alert_links_links_dict = alert_links_links_instance.to_dict()
# create an instance of AlertLinksLinks from a dict
alert_links_links_from_dict = AlertLinksLinks.from_dict(alert_links_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


