# CredentialVaultOperations


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[CredentialVaultOperation]**](CredentialVaultOperation.md) |  | [optional] 
**links** | [**SelfLinks**](SelfLinks.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.connectors.models.credential_vault_operations import CredentialVaultOperations

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialVaultOperations from a JSON string
credential_vault_operations_instance = CredentialVaultOperations.from_json(json)
# print the JSON string representation of the object
print(CredentialVaultOperations.to_json())

# convert the object into a dict
credential_vault_operations_dict = credential_vault_operations_instance.to_dict()
# create an instance of CredentialVaultOperations from a dict
credential_vault_operations_from_dict = CredentialVaultOperations.from_dict(credential_vault_operations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


