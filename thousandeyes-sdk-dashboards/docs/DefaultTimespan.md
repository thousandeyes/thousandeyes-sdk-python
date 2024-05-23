# DefaultTimespan


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timespan_duration** | **int** | Relative timespan in seconds. | [optional] 
**timespan_start** | **str** | UTC start date of the timespan range. | [optional] 
**timespan_end** | **str** | UTC end date of the timespan range. | [optional] 
**duration** | **int** | Relative timespan in seconds. | [optional] 
**start** | **datetime** | UTC start date of the timespan range (ISO date-time format). | [optional] 
**end** | **datetime** | UTC end date of the timespan range (ISO date-time format). | [optional] 

## Example

```python
from thousandeyes_sdk.dashboards.models.default_timespan import DefaultTimespan

# TODO update the JSON string below
json = "{}"
# create an instance of DefaultTimespan from a JSON string
default_timespan_instance = DefaultTimespan.from_json(json)
# print the JSON string representation of the object
print(DefaultTimespan.to_json())

# convert the object into a dict
default_timespan_dict = default_timespan_instance.to_dict()
# create an instance of DefaultTimespan from a dict
default_timespan_from_dict = DefaultTimespan.from_dict(default_timespan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


