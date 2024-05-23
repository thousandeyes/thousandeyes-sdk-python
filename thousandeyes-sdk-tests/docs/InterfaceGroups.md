# InterfaceGroups


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path_vis_interface_groups** | [**List[InterfaceGroup]**](InterfaceGroup.md) |  | [optional] 
**links** | [**SelfLinks**](SelfLinks.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.tests.models.interface_groups import InterfaceGroups

# TODO update the JSON string below
json = "{}"
# create an instance of InterfaceGroups from a JSON string
interface_groups_instance = InterfaceGroups.from_json(json)
# print the JSON string representation of the object
print(InterfaceGroups.to_json())

# convert the object into a dict
interface_groups_dict = interface_groups_instance.to_dict()
# create an instance of InterfaceGroups from a dict
interface_groups_from_dict = InterfaceGroups.from_dict(interface_groups_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


