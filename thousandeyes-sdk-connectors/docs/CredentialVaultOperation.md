# CredentialVaultOperation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**name** | **str** |  | 
**secrets** | [**List[CredentialVaultSecret]**](CredentialVaultSecret.md) |  | 
**type** | [**OperationType**](OperationType.md) |  | [optional] 
**status** | [**OperationStatus**](OperationStatus.md) |  | [optional] 
**links** | [**SelfLinks**](SelfLinks.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.connectors.models.credential_vault_operation import CredentialVaultOperation

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialVaultOperation from a JSON string
credential_vault_operation_instance = CredentialVaultOperation.from_json(json)
# print the JSON string representation of the object
print(CredentialVaultOperation.to_json())

# convert the object into a dict
credential_vault_operation_dict = credential_vault_operation_instance.to_dict()
# create an instance of CredentialVaultOperation from a dict
credential_vault_operation_from_dict = CredentialVaultOperation.from_dict(credential_vault_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


