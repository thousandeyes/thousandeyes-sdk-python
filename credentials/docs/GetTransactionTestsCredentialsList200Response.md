# GetTransactionTestsCredentialsList200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credentials** | [**List[Credential]**](Credential.md) |  | [optional] 
**links** | [**SelfLinksLinks**](SelfLinksLinks.md) |  | [optional] 

## Example

```python
from credentials.models.get_transaction_tests_credentials_list200_response import GetTransactionTestsCredentialsList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetTransactionTestsCredentialsList200Response from a JSON string
get_transaction_tests_credentials_list200_response_instance = GetTransactionTestsCredentialsList200Response.from_json(json)
# print the JSON string representation of the object
print(GetTransactionTestsCredentialsList200Response.to_json())

# convert the object into a dict
get_transaction_tests_credentials_list200_response_dict = get_transaction_tests_credentials_list200_response_instance.to_dict()
# create an instance of GetTransactionTestsCredentialsList200Response from a dict
get_transaction_tests_credentials_list200_response_from_dict = GetTransactionTestsCredentialsList200Response.from_dict(get_transaction_tests_credentials_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


