# ActiveWithin

Timespan in which alerts must have been active to appear in the widget.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **int** | Timespan value. | [optional] 
**unit** | [**LegacyDurationUnit**](LegacyDurationUnit.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.dashboards.models.active_within import ActiveWithin

# TODO update the JSON string below
json = "{}"
# create an instance of ActiveWithin from a JSON string
active_within_instance = ActiveWithin.from_json(json)
# print the JSON string representation of the object
print(ActiveWithin.to_json())

# convert the object into a dict
active_within_dict = active_within_instance.to_dict()
# create an instance of ActiveWithin from a dict
active_within_from_dict = ActiveWithin.from_dict(active_within_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


