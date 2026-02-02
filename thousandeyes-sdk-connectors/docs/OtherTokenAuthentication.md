# OtherTokenAuthentication


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** |  | 
**type** | [**AuthenticationType**](AuthenticationType.md) |  | 

## Example

```python
from thousandeyes_sdk.connectors.models.other_token_authentication import OtherTokenAuthentication

# TODO update the JSON string below
json = "{}"
# create an instance of OtherTokenAuthentication from a JSON string
other_token_authentication_instance = OtherTokenAuthentication.from_json(json)
# print the JSON string representation of the object
print(OtherTokenAuthentication.to_json())

# convert the object into a dict
other_token_authentication_dict = other_token_authentication_instance.to_dict()
# create an instance of OtherTokenAuthentication from a dict
other_token_authentication_from_dict = OtherTokenAuthentication.from_dict(other_token_authentication_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


