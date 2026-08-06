# PanoramaKeyGenAuthentication

Authentication using credentials to generate a Panorama API key.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** | Username used to generate the Panorama API key. | 
**password** | **str** | Password used to generate the Panorama API key. | 
**key_ttl** | **int** | Time to live for the generated Panorama API key, in minutes. | 
**type** | **str** |  | 

## Example

```python
from thousandeyes_sdk.connectors.models.panorama_key_gen_authentication import PanoramaKeyGenAuthentication

# TODO update the JSON string below
json = "{}"
# create an instance of PanoramaKeyGenAuthentication from a JSON string
panorama_key_gen_authentication_instance = PanoramaKeyGenAuthentication.from_json(json)
# print the JSON string representation of the object
print(PanoramaKeyGenAuthentication.to_json())

# convert the object into a dict
panorama_key_gen_authentication_dict = panorama_key_gen_authentication_instance.to_dict()
# create an instance of PanoramaKeyGenAuthentication from a dict
panorama_key_gen_authentication_from_dict = PanoramaKeyGenAuthentication.from_dict(panorama_key_gen_authentication_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


