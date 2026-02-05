# GenericConnectorAuth


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | 
**password** | **str** |  | 
**type** | [**AuthenticationType**](AuthenticationType.md) |  | 
**token** | **str** |  | 
**refresh_token** | **str** |  | [optional] 
**oauth_client_id** | **str** |  | 
**oauth_auth_url** | **str** |  | 
**oauth_token_url** | **str** |  | 
**oauth_client_secret** | **str** |  | 
**code** | **str** |  | 
**redirect_uri** | **str** |  | 

## Example

```python
from thousandeyes_sdk.connectors.models.generic_connector_auth import GenericConnectorAuth

# TODO update the JSON string below
json = "{}"
# create an instance of GenericConnectorAuth from a JSON string
generic_connector_auth_instance = GenericConnectorAuth.from_json(json)
# print the JSON string representation of the object
print(GenericConnectorAuth.to_json())

# convert the object into a dict
generic_connector_auth_dict = generic_connector_auth_instance.to_dict()
# create an instance of GenericConnectorAuth from a dict
generic_connector_auth_from_dict = GenericConnectorAuth.from_dict(generic_connector_auth_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


