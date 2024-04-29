# GetPathVisInterfaceGroups200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path_vis_interface_groups** | [**List[InterfaceGroup]**](InterfaceGroup.md) |  | [optional] 
**links** | [**SelfLinksLinks**](SelfLinksLinks.md) |  | [optional] 

## Example

```python
from tests.models.get_path_vis_interface_groups200_response import GetPathVisInterfaceGroups200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetPathVisInterfaceGroups200Response from a JSON string
get_path_vis_interface_groups200_response_instance = GetPathVisInterfaceGroups200Response.from_json(json)
# print the JSON string representation of the object
print(GetPathVisInterfaceGroups200Response.to_json())

# convert the object into a dict
get_path_vis_interface_groups200_response_dict = get_path_vis_interface_groups200_response_instance.to_dict()
# create an instance of GetPathVisInterfaceGroups200Response from a dict
get_path_vis_interface_groups200_response_from_dict = GetPathVisInterfaceGroups200Response.from_dict(get_path_vis_interface_groups200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

