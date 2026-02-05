# BearerTokenAuthentication


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** |  | 
**type** | [**AuthenticationType**](AuthenticationType.md) |  | 

## Example

```python
from thousandeyes_sdk.connectors.models.bearer_token_authentication import BearerTokenAuthentication

# TODO update the JSON string below
json = "{}"
# create an instance of BearerTokenAuthentication from a JSON string
bearer_token_authentication_instance = BearerTokenAuthentication.from_json(json)
# print the JSON string representation of the object
print(BearerTokenAuthentication.to_json())

# convert the object into a dict
bearer_token_authentication_dict = bearer_token_authentication_instance.to_dict()
# create an instance of BearerTokenAuthentication from a dict
bearer_token_authentication_from_dict = BearerTokenAuthentication.from_dict(bearer_token_authentication_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


