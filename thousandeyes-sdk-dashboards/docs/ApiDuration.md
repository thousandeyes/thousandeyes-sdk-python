# ApiDuration

Specifies a fixed timespan for data aggregation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **int** | Timespan value. | [optional] 
**unit** | [**LegacyDurationUnit**](LegacyDurationUnit.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.dashboards.models.api_duration import ApiDuration

# TODO update the JSON string below
json = "{}"
# create an instance of ApiDuration from a JSON string
api_duration_instance = ApiDuration.from_json(json)
# print the JSON string representation of the object
print(ApiDuration.to_json())

# convert the object into a dict
api_duration_dict = api_duration_instance.to_dict()
# create an instance of ApiDuration from a dict
api_duration_from_dict = ApiDuration.from_dict(api_duration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


