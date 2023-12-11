# CredentialWithoutValue


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**SelfLinksLinks**](SelfLinksLinks.md) |  | [optional] 
**id** | **str** | Unique ID of the credential. | [optional] 
**name** | **str** | The name of the credential. | [optional] 

## Example

```python
from credentials_api.models.credential_without_value import CredentialWithoutValue

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialWithoutValue from a JSON string
credential_without_value_instance = CredentialWithoutValue.from_json(json)
# print the JSON string representation of the object
print CredentialWithoutValue.to_json()

# convert the object into a dict
credential_without_value_dict = credential_without_value_instance.to_dict()
# create an instance of CredentialWithoutValue from a dict
credential_without_value_form_dict = credential_without_value.from_dict(credential_without_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


