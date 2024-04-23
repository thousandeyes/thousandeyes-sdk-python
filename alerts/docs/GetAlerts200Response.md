# GetAlerts200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alerts** | [**List[Alert]**](Alert.md) |  | [optional] 
**links** | [**PaginationLinksLinks**](PaginationLinksLinks.md) |  | [optional] 

## Example

```python
from alerts.models.get_alerts200_response import GetAlerts200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetAlerts200Response from a JSON string
get_alerts200_response_instance = GetAlerts200Response.from_json(json)
# print the JSON string representation of the object
print(GetAlerts200Response.to_json())

# convert the object into a dict
get_alerts200_response_dict = get_alerts200_response_instance.to_dict()
# create an instance of GetAlerts200Response from a dict
get_alerts200_response_from_dict = GetAlerts200Response.from_dict(get_alerts200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


