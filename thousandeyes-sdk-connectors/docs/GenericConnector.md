# GenericConnector


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**type** | [**ConnectorType**](ConnectorType.md) |  | 
**name** | **str** |  | 
**target** | **str** |  | 
**authentication** | [**GenericConnectorAuth**](GenericConnectorAuth.md) |  | [optional] 
**last_modified_date** | **datetime** | The date when the connector was last modified. | [optional] [readonly] 
**headers** | [**List[Header]**](Header.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.connectors.models.generic_connector import GenericConnector

# TODO update the JSON string below
json = "{}"
# create an instance of GenericConnector from a JSON string
generic_connector_instance = GenericConnector.from_json(json)
# print the JSON string representation of the object
print(GenericConnector.to_json())

# convert the object into a dict
generic_connector_dict = generic_connector_instance.to_dict()
# create an instance of GenericConnector from a dict
generic_connector_from_dict = GenericConnector.from_dict(generic_connector_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


