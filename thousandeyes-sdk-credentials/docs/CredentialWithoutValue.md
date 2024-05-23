# CredentialWithoutValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique ID of the credential. | [optional] 
**name** | **str** | The name of the credential. | [optional] 
**links** | [**SelfLinks**](SelfLinks.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.credentials.models.credential_without_value import CredentialWithoutValue

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialWithoutValue from a JSON string
credential_without_value_instance = CredentialWithoutValue.from_json(json)
# print the JSON string representation of the object
print(CredentialWithoutValue.to_json())

# convert the object into a dict
credential_without_value_dict = credential_without_value_instance.to_dict()
# create an instance of CredentialWithoutValue from a dict
credential_without_value_from_dict = CredentialWithoutValue.from_dict(credential_without_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


