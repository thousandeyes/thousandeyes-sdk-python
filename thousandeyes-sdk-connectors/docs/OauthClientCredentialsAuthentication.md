# OauthClientCredentialsAuthentication


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** |  | [optional] 
**oauth_client_id** | **str** |  | 
**oauth_token_url** | **str** |  | 
**oauth_client_secret** | **str** |  | 
**type** | [**AuthenticationType**](AuthenticationType.md) |  | 

## Example

```python
from thousandeyes_sdk.connectors.models.oauth_client_credentials_authentication import OauthClientCredentialsAuthentication

# TODO update the JSON string below
json = "{}"
# create an instance of OauthClientCredentialsAuthentication from a JSON string
oauth_client_credentials_authentication_instance = OauthClientCredentialsAuthentication.from_json(json)
# print the JSON string representation of the object
print(OauthClientCredentialsAuthentication.to_json())

# convert the object into a dict
oauth_client_credentials_authentication_dict = oauth_client_credentials_authentication_instance.to_dict()
# create an instance of OauthClientCredentialsAuthentication from a dict
oauth_client_credentials_authentication_from_dict = OauthClientCredentialsAuthentication.from_dict(oauth_client_credentials_authentication_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


