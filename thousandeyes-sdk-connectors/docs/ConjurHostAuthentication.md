# ConjurHostAuthentication


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host_id** | **str** |  | 
**api_key** | **str** |  | 
**type** | [**AuthenticationType**](AuthenticationType.md) |  | 

## Example

```python
from thousandeyes_sdk.connectors.models.conjur_host_authentication import ConjurHostAuthentication

# TODO update the JSON string below
json = "{}"
# create an instance of ConjurHostAuthentication from a JSON string
conjur_host_authentication_instance = ConjurHostAuthentication.from_json(json)
# print the JSON string representation of the object
print(ConjurHostAuthentication.to_json())

# convert the object into a dict
conjur_host_authentication_dict = conjur_host_authentication_instance.to_dict()
# create an instance of ConjurHostAuthentication from a dict
conjur_host_authentication_from_dict = ConjurHostAuthentication.from_dict(conjur_host_authentication_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


