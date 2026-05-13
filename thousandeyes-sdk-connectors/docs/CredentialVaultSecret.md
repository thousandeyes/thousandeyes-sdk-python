# CredentialVaultSecret


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | 
**secret_key** | **str** |  | 

## Example

```python
from thousandeyes_sdk.connectors.models.credential_vault_secret import CredentialVaultSecret

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialVaultSecret from a JSON string
credential_vault_secret_instance = CredentialVaultSecret.from_json(json)
# print the JSON string representation of the object
print(CredentialVaultSecret.to_json())

# convert the object into a dict
credential_vault_secret_dict = credential_vault_secret_instance.to_dict()
# create an instance of CredentialVaultSecret from a dict
credential_vault_secret_from_dict = CredentialVaultSecret.from_dict(credential_vault_secret_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


