# GetAlertsRules200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alert_rules** | [**List[Rule]**](Rule.md) |  | [optional] 
**links** | [**SelfLinksLinks**](SelfLinksLinks.md) |  | [optional] 

## Example

```python
from alerts.models.get_alerts_rules200_response import GetAlertsRules200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetAlertsRules200Response from a JSON string
get_alerts_rules200_response_instance = GetAlertsRules200Response.from_json(json)
# print the JSON string representation of the object
print(GetAlertsRules200Response.to_json())

# convert the object into a dict
get_alerts_rules200_response_dict = get_alerts_rules200_response_instance.to_dict()
# create an instance of GetAlertsRules200Response from a dict
get_alerts_rules200_response_from_dict = GetAlertsRules200Response.from_dict(get_alerts_rules200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

