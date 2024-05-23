# Repeat

Repeat options.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**RepeatType**](RepeatType.md) |  | [optional] 
**interval_type** | [**IntervalType**](IntervalType.md) |  | [optional] 
**interval_length** | **int** | Number of &#x60;intervalTypes&#x60; to wait before reactivating the alert suppression window. | [optional] 
**days_of_week** | [**List[DaysOfWeek]**](DaysOfWeek.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.alerts.models.repeat import Repeat

# TODO update the JSON string below
json = "{}"
# create an instance of Repeat from a JSON string
repeat_instance = Repeat.from_json(json)
# print the JSON string representation of the object
print(Repeat.to_json())

# convert the object into a dict
repeat_dict = repeat_instance.to_dict()
# create an instance of Repeat from a dict
repeat_from_dict = Repeat.from_dict(repeat_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


