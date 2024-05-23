# EndRepeat

End repeat options.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**EndRepeatType**](EndRepeatType.md) |  | [optional] 
**count** | **int** | End repeat after number of occurrences, only valid with count type option. | [optional] 
**var_date** | **date** | End repeat after specific date, only valid with date type option (ISO date format). | [optional] 

## Example

```python
from thousandeyes_sdk.alerts.models.end_repeat import EndRepeat

# TODO update the JSON string below
json = "{}"
# create an instance of EndRepeat from a JSON string
end_repeat_instance = EndRepeat.from_json(json)
# print the JSON string representation of the object
print(EndRepeat.to_json())

# convert the object into a dict
end_repeat_dict = end_repeat_instance.to_dict()
# create an instance of EndRepeat from a dict
end_repeat_from_dict = EndRepeat.from_dict(end_repeat_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


