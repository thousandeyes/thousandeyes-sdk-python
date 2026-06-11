# TestVaultCredential


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**secret_id** | **str** | UUID of the configured secret. | [optional] 
**target** | [**TestVaultCredentialTarget**](TestVaultCredentialTarget.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.tests.models.test_vault_credential import TestVaultCredential

# TODO update the JSON string below
json = "{}"
# create an instance of TestVaultCredential from a JSON string
test_vault_credential_instance = TestVaultCredential.from_json(json)
# print the JSON string representation of the object
print(TestVaultCredential.to_json())

# convert the object into a dict
test_vault_credential_dict = test_vault_credential_instance.to_dict()
# create an instance of TestVaultCredential from a dict
test_vault_credential_from_dict = TestVaultCredential.from_dict(test_vault_credential_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


