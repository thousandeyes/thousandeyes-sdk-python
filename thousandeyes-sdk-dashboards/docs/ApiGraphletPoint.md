# ApiGraphletPoint

A data point on a graphlet.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**x** | **int** | Timestamp of the data point. | [optional] 
**y** | **float** | Value of the data point. | [optional] 

## Example

```python
from thousandeyes_sdk.dashboards.models.api_graphlet_point import ApiGraphletPoint

# TODO update the JSON string below
json = "{}"
# create an instance of ApiGraphletPoint from a JSON string
api_graphlet_point_instance = ApiGraphletPoint.from_json(json)
# print the JSON string representation of the object
print(ApiGraphletPoint.to_json())

# convert the object into a dict
api_graphlet_point_dict = api_graphlet_point_instance.to_dict()
# create an instance of ApiGraphletPoint from a dict
api_graphlet_point_from_dict = ApiGraphletPoint.from_dict(api_graphlet_point_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


