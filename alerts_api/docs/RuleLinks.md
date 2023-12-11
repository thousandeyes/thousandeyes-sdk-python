# RuleLinks


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**RuleLinksLinks**](RuleLinksLinks.md) |  | [optional] 

## Example

```python
from alerts_api.models.rule_links import RuleLinks

# TODO update the JSON string below
json = "{}"
# create an instance of RuleLinks from a JSON string
rule_links_instance = RuleLinks.from_json(json)
# print the JSON string representation of the object
print RuleLinks.to_json()

# convert the object into a dict
rule_links_dict = rule_links_instance.to_dict()
# create an instance of RuleLinks from a dict
rule_links_form_dict = rule_links.from_dict(rule_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


