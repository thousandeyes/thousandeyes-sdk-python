# PanoramaConnectorAuth

Authentication configuration for the Panorama connector.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** | Panorama API key used for authentication. | 
**type** | **str** | Authentication type. | 
**username** | **str** | Username used to generate the Panorama API key. | 
**password** | **str** | Password used to generate the Panorama API key. | 
**key_ttl** | **int** | Time to live for the generated Panorama API key, in minutes. | 

## Example

```python
from thousandeyes_sdk.connectors.models.panorama_connector_auth import PanoramaConnectorAuth

# TODO update the JSON string below
json = "{}"
# create an instance of PanoramaConnectorAuth from a JSON string
panorama_connector_auth_instance = PanoramaConnectorAuth.from_json(json)
# print the JSON string representation of the object
print(PanoramaConnectorAuth.to_json())

# convert the object into a dict
panorama_connector_auth_dict = panorama_connector_auth_instance.to_dict()
# create an instance of PanoramaConnectorAuth from a dict
panorama_connector_auth_from_dict = PanoramaConnectorAuth.from_dict(panorama_connector_auth_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


