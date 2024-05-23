# Rules


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alert_rules** | [**List[BaseRule]**](BaseRule.md) |  | [optional] 
**links** | [**SelfLinks**](SelfLinks.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.alerts.models.rules import Rules

# TODO update the JSON string below
json = "{}"
# create an instance of Rules from a JSON string
rules_instance = Rules.from_json(json)
# print the JSON string representation of the object
print(Rules.to_json())

# convert the object into a dict
rules_dict = rules_instance.to_dict()
# create an instance of Rules from a dict
rules_from_dict = Rules.from_dict(rules_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


