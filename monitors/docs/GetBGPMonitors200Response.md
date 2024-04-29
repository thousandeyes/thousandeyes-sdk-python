# GetBGPMonitors200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**monitors** | [**List[Monitor]**](Monitor.md) |  | [optional] 
**links** | [**SelfLinksLinks**](SelfLinksLinks.md) |  | [optional] 

## Example

```python
from monitors.models.get_bgp_monitors200_response import GetBGPMonitors200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetBGPMonitors200Response from a JSON string
get_bgp_monitors200_response_instance = GetBGPMonitors200Response.from_json(json)
# print the JSON string representation of the object
print(GetBGPMonitors200Response.to_json())

# convert the object into a dict
get_bgp_monitors200_response_dict = get_bgp_monitors200_response_instance.to_dict()
# create an instance of GetBGPMonitors200Response from a dict
get_bgp_monitors200_response_from_dict = GetBGPMonitors200Response.from_dict(get_bgp_monitors200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

