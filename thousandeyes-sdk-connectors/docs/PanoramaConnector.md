# PanoramaConnector

Palo Alto Networks Panorama connector configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique ID of the Panorama connector. | [optional] [readonly] 
**type** | **str** | Connector type. | 
**name** | **str** | Name of the Panorama connector. | 
**target** | **str** | URL of the Panorama instance. | 
**last_modified_date** | **int** | Time when the connector was last modified, in milliseconds since the Unix epoch. | [optional] [readonly] 
**authentication** | [**PanoramaConnectorAuth**](PanoramaConnectorAuth.md) |  | 
**links** | [**SelfLinks**](SelfLinks.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.connectors.models.panorama_connector import PanoramaConnector

# TODO update the JSON string below
json = "{}"
# create an instance of PanoramaConnector from a JSON string
panorama_connector_instance = PanoramaConnector.from_json(json)
# print the JSON string representation of the object
print(PanoramaConnector.to_json())

# convert the object into a dict
panorama_connector_dict = panorama_connector_instance.to_dict()
# create an instance of PanoramaConnector from a dict
panorama_connector_from_dict = PanoramaConnector.from_dict(panorama_connector_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


