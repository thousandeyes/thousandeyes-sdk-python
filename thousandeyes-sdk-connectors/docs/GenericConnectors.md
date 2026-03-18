# GenericConnectors


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[GenericConnector]**](GenericConnector.md) |  | [optional] 
**links** | [**SelfLinks**](SelfLinks.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.connectors.models.generic_connectors import GenericConnectors

# TODO update the JSON string below
json = "{}"
# create an instance of GenericConnectors from a JSON string
generic_connectors_instance = GenericConnectors.from_json(json)
# print the JSON string representation of the object
print(GenericConnectors.to_json())

# convert the object into a dict
generic_connectors_dict = generic_connectors_instance.to_dict()
# create an instance of GenericConnectors from a dict
generic_connectors_from_dict = GenericConnectors.from_dict(generic_connectors_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


