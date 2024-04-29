# AccessToken


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token_type** | **str** |  | [optional] 
**expires_in** | **int** |  | [optional] 
**access_token** | **str** |  | [optional] 
**scope** | **str** |  | [optional] 

## Example

```python
from oauth2.models.access_token import AccessToken

# TODO update the JSON string below
json = "{}"
# create an instance of AccessToken from a JSON string
access_token_instance = AccessToken.from_json(json)
# print the JSON string representation of the object
print(AccessToken.to_json())

# convert the object into a dict
access_token_dict = access_token_instance.to_dict()
# create an instance of AccessToken from a dict
access_token_from_dict = AccessToken.from_dict(access_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


