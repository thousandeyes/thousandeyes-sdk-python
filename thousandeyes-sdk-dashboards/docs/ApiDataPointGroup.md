# ApiDataPointGroup

Group of data points.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_property** | **str** | Defines the criterion used to aggregate data points under specific group values. | [optional] 
**group_value** | **str** | The value of a group. | [optional] 

## Example

```python
from thousandeyes_sdk.dashboards.models.api_data_point_group import ApiDataPointGroup

# TODO update the JSON string below
json = "{}"
# create an instance of ApiDataPointGroup from a JSON string
api_data_point_group_instance = ApiDataPointGroup.from_json(json)
# print the JSON string representation of the object
print(ApiDataPointGroup.to_json())

# convert the object into a dict
api_data_point_group_dict = api_data_point_group_instance.to_dict()
# create an instance of ApiDataPointGroup from a dict
api_data_point_group_from_dict = ApiDataPointGroup.from_dict(api_data_point_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


