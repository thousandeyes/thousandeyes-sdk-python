# RuleLinksLinks

An object containing the alert rule links.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rule** | [**Link**](Link.md) |  | [optional] 

## Example

```python
from alerts_api.models.rule_links_links import RuleLinksLinks

# TODO update the JSON string below
json = "{}"
# create an instance of RuleLinksLinks from a JSON string
rule_links_links_instance = RuleLinksLinks.from_json(json)
# print the JSON string representation of the object
print RuleLinksLinks.to_json()

# convert the object into a dict
rule_links_links_dict = rule_links_links_instance.to_dict()
# create an instance of RuleLinksLinks from a dict
rule_links_links_form_dict = rule_links_links.from_dict(rule_links_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


