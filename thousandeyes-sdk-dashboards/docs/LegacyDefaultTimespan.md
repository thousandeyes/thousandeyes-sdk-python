# LegacyDefaultTimespan


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timespan_duration** | **int** | Relative timespan in seconds. | [optional] 
**timespan_start** | **str** | UTC start date of the timespan range. | [optional] 
**timespan_end** | **str** | UTC end date of the timespan range. | [optional] 

## Example

```python
from thousandeyes_sdk.dashboards.models.legacy_default_timespan import LegacyDefaultTimespan

# TODO update the JSON string below
json = "{}"
# create an instance of LegacyDefaultTimespan from a JSON string
legacy_default_timespan_instance = LegacyDefaultTimespan.from_json(json)
# print the JSON string representation of the object
print(LegacyDefaultTimespan.to_json())

# convert the object into a dict
legacy_default_timespan_dict = legacy_default_timespan_instance.to_dict()
# create an instance of LegacyDefaultTimespan from a dict
legacy_default_timespan_from_dict = LegacyDefaultTimespan.from_dict(legacy_default_timespan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


