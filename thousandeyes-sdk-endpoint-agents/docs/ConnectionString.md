# ConnectionString


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_string** | **str** | The connection string is used for some integrations and other client types.  | [optional] 
**links** | [**SelfLinks**](SelfLinks.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_agents.models.connection_string import ConnectionString

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectionString from a JSON string
connection_string_instance = ConnectionString.from_json(json)
# print the JSON string representation of the object
print(ConnectionString.to_json())

# convert the object into a dict
connection_string_dict = connection_string_instance.to_dict()
# create an instance of ConnectionString from a dict
connection_string_from_dict = ConnectionString.from_dict(connection_string_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


