# ApiDefaultTimespan


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**duration** | **int** | Relative timespan in seconds. | [optional] 
**start** | **datetime** | UTC start date of the timespan range (ISO date-time format). | [optional] 
**end** | **datetime** | UTC end date of the timespan range (ISO date-time format). | [optional] 

## Example

```python
from thousandeyes_sdk.dashboards.models.api_default_timespan import ApiDefaultTimespan

# TODO update the JSON string below
json = "{}"
# create an instance of ApiDefaultTimespan from a JSON string
api_default_timespan_instance = ApiDefaultTimespan.from_json(json)
# print the JSON string representation of the object
print(ApiDefaultTimespan.to_json())

# convert the object into a dict
api_default_timespan_dict = api_default_timespan_instance.to_dict()
# create an instance of ApiDefaultTimespan from a dict
api_default_timespan_from_dict = ApiDefaultTimespan.from_dict(api_default_timespan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


