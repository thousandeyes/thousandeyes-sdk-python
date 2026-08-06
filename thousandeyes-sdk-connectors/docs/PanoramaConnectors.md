# PanoramaConnectors

Collection of Panorama connectors.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[PanoramaConnector]**](PanoramaConnector.md) |  | [optional] 
**links** | [**SelfLinks**](SelfLinks.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.connectors.models.panorama_connectors import PanoramaConnectors

# TODO update the JSON string below
json = "{}"
# create an instance of PanoramaConnectors from a JSON string
panorama_connectors_instance = PanoramaConnectors.from_json(json)
# print the JSON string representation of the object
print(PanoramaConnectors.to_json())

# convert the object into a dict
panorama_connectors_dict = panorama_connectors_instance.to_dict()
# create an instance of PanoramaConnectors from a dict
panorama_connectors_from_dict = PanoramaConnectors.from_dict(panorama_connectors_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


