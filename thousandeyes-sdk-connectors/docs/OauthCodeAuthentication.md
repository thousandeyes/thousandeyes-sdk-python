# OauthCodeAuthentication


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** |  | [optional] 
**refresh_token** | **str** |  | [optional] 
**oauth_client_id** | **str** |  | 
**oauth_auth_url** | **str** |  | 
**oauth_token_url** | **str** |  | 
**oauth_client_secret** | **str** |  | 
**code** | **str** |  | 
**redirect_uri** | **str** |  | 
**type** | [**AuthenticationType**](AuthenticationType.md) |  | 

## Example

```python
from thousandeyes_sdk.connectors.models.oauth_code_authentication import OauthCodeAuthentication

# TODO update the JSON string below
json = "{}"
# create an instance of OauthCodeAuthentication from a JSON string
oauth_code_authentication_instance = OauthCodeAuthentication.from_json(json)
# print the JSON string representation of the object
print(OauthCodeAuthentication.to_json())

# convert the object into a dict
oauth_code_authentication_dict = oauth_code_authentication_instance.to_dict()
# create an instance of OauthCodeAuthentication from a dict
oauth_code_authentication_from_dict = OauthCodeAuthentication.from_dict(oauth_code_authentication_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


