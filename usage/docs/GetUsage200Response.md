# GetUsage200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**usage** | [**UsageUsage**](UsageUsage.md) |  | [optional] 
**links** | [**SelfLinksLinks**](SelfLinksLinks.md) |  | [optional] 

## Example

```python
from usage.models.get_usage200_response import GetUsage200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetUsage200Response from a JSON string
get_usage200_response_instance = GetUsage200Response.from_json(json)
# print the JSON string representation of the object
print(GetUsage200Response.to_json())

# convert the object into a dict
get_usage200_response_dict = get_usage200_response_instance.to_dict()
# create an instance of GetUsage200Response from a dict
get_usage200_response_from_dict = GetUsage200Response.from_dict(get_usage200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

