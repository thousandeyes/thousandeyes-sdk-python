# ConjurConnectors


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ConjurConnector]**](ConjurConnector.md) |  | [optional] 
**links** | [**SelfLinks**](SelfLinks.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.connectors.models.conjur_connectors import ConjurConnectors

# TODO update the JSON string below
json = "{}"
# create an instance of ConjurConnectors from a JSON string
conjur_connectors_instance = ConjurConnectors.from_json(json)
# print the JSON string representation of the object
print(ConjurConnectors.to_json())

# convert the object into a dict
conjur_connectors_dict = conjur_connectors_instance.to_dict()
# create an instance of ConjurConnectors from a dict
conjur_connectors_from_dict = ConjurConnectors.from_dict(conjur_connectors_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


