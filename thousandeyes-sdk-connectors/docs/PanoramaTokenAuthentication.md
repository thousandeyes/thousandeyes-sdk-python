# PanoramaTokenAuthentication

Authentication using an existing Panorama API key.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** | Panorama API key used for authentication. | 
**type** | **str** | Authentication type. | 

## Example

```python
from thousandeyes_sdk.connectors.models.panorama_token_authentication import PanoramaTokenAuthentication

# TODO update the JSON string below
json = "{}"
# create an instance of PanoramaTokenAuthentication from a JSON string
panorama_token_authentication_instance = PanoramaTokenAuthentication.from_json(json)
# print the JSON string representation of the object
print(PanoramaTokenAuthentication.to_json())

# convert the object into a dict
panorama_token_authentication_dict = panorama_token_authentication_instance.to_dict()
# create an instance of PanoramaTokenAuthentication from a dict
panorama_token_authentication_from_dict = PanoramaTokenAuthentication.from_dict(panorama_token_authentication_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


