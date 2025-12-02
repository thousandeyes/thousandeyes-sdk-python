# Coordinates

Geographic coordinates for agent location.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**latitude** | **float** | The latitude of the agent location in decimal degrees | [optional] [readonly] 
**longitude** | **float** | The longitude of the agent location in decimal degrees | [optional] [readonly] 

## Example

```python
from thousandeyes_sdk.agents.models.coordinates import Coordinates

# TODO update the JSON string below
json = "{}"
# create an instance of Coordinates from a JSON string
coordinates_instance = Coordinates.from_json(json)
# print the JSON string representation of the object
print(Coordinates.to_json())

# convert the object into a dict
coordinates_dict = coordinates_instance.to_dict()
# create an instance of Coordinates from a dict
coordinates_from_dict = Coordinates.from_dict(coordinates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


