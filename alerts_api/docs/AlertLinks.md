# AlertLinks


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**RuleLinksLinks**](RuleLinksLinks.md) |  | [optional] 

## Example

```python
from alerts_api.models.alert_links import AlertLinks

# TODO update the JSON string below
json = "{}"
# create an instance of AlertLinks from a JSON string
alert_links_instance = AlertLinks.from_json(json)
# print the JSON string representation of the object
print AlertLinks.to_json()

# convert the object into a dict
alert_links_dict = alert_links_instance.to_dict()
# create an instance of AlertLinks from a dict
alert_links_form_dict = alert_links.from_dict(alert_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


