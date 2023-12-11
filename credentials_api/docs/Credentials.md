# Credentials


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credentials** | [**List[Credential]**](Credential.md) |  | [optional] 

## Example

```python
from credentials_api.models.credentials import Credentials

# TODO update the JSON string below
json = "{}"
# create an instance of Credentials from a JSON string
credentials_instance = Credentials.from_json(json)
# print the JSON string representation of the object
print Credentials.to_json()

# convert the object into a dict
credentials_dict = credentials_instance.to_dict()
# create an instance of Credentials from a dict
credentials_form_dict = credentials.from_dict(credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


