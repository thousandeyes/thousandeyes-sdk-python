# ConjurConnector


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**type** | [**ConnectorType**](ConnectorType.md) |  | 
**name** | **str** |  | 
**target** | **str** |  | 
**last_modified_date** | **int** | The date when the connector was last modified (Unix timestamp in milliseconds). | [optional] [readonly] 
**account** | **str** |  | 
**authentication** | [**ConjurHostAuthentication**](ConjurHostAuthentication.md) |  | 
**links** | [**SelfLinks**](SelfLinks.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.connectors.models.conjur_connector import ConjurConnector

# TODO update the JSON string below
json = "{}"
# create an instance of ConjurConnector from a JSON string
conjur_connector_instance = ConjurConnector.from_json(json)
# print the JSON string representation of the object
print(ConjurConnector.to_json())

# convert the object into a dict
conjur_connector_dict = conjur_connector_instance.to_dict()
# create an instance of ConjurConnector from a dict
conjur_connector_from_dict = ConjurConnector.from_dict(conjur_connector_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


