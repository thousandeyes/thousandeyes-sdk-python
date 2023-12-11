# UpdatePathVisInterfaceGroup200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aid** | **str** | Account Group Id | [optional] [readonly] 
**group_id** | **str** | Group ID | [optional] [readonly] 
**group_name** | **str** | Name of the path visualization interface group | [optional] 
**ip_addresses** | **List[str]** | Array of IP addresses associated with the interface group | [optional] 
**rdns_regexes** | **List[str]** | Array of RDNS Regexes associated with the interface group | [optional] [readonly] 
**links** | [**SelfLinksLinks**](SelfLinksLinks.md) |  | [optional] 

## Example

```python
from tests_api.models.update_path_vis_interface_group200_response import UpdatePathVisInterfaceGroup200Response

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePathVisInterfaceGroup200Response from a JSON string
update_path_vis_interface_group200_response_instance = UpdatePathVisInterfaceGroup200Response.from_json(json)
# print the JSON string representation of the object
print UpdatePathVisInterfaceGroup200Response.to_json()

# convert the object into a dict
update_path_vis_interface_group200_response_dict = update_path_vis_interface_group200_response_instance.to_dict()
# create an instance of UpdatePathVisInterfaceGroup200Response from a dict
update_path_vis_interface_group200_response_form_dict = update_path_vis_interface_group200_response.from_dict(update_path_vis_interface_group200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


