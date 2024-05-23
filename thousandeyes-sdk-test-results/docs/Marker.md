# Marker


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name assigned to marker in transaction script | [optional] [readonly] 
**duration** | **int** | Total time recorded by marker in milliseconds | [optional] [readonly] 

## Example

```python
from thousandeyes_sdk.test_results.models.marker import Marker

# TODO update the JSON string below
json = "{}"
# create an instance of Marker from a JSON string
marker_instance = Marker.from_json(json)
# print the JSON string representation of the object
print(Marker.to_json())

# convert the object into a dict
marker_dict = marker_instance.to_dict()
# create an instance of Marker from a dict
marker_from_dict = Marker.from_dict(marker_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


