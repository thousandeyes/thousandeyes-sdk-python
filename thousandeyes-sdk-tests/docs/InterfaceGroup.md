# InterfaceGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aid** | **str** | Account Group Id | [optional] [readonly] 
**group_id** | **str** | Group ID | [optional] [readonly] 
**group_name** | **str** | Name of the path visualization interface group | [optional] 
**ip_addresses** | **List[str]** | Array of IP addresses associated with the interface group | [optional] 
**rdns_regexes** | **List[str]** | Array of RDNS Regexes associated with the interface group | [optional] [readonly] 

## Example

```python
from thousandeyes_sdk.tests.models.interface_group import InterfaceGroup

# TODO update the JSON string below
json = "{}"
# create an instance of InterfaceGroup from a JSON string
interface_group_instance = InterfaceGroup.from_json(json)
# print the JSON string representation of the object
print(InterfaceGroup.to_json())

# convert the object into a dict
interface_group_dict = interface_group_instance.to_dict()
# create an instance of InterfaceGroup from a dict
interface_group_from_dict = InterfaceGroup.from_dict(interface_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


