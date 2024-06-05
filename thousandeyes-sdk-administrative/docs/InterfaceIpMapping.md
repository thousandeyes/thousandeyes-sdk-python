# InterfaceIpMapping


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interface_name** | **str** | Name of the mapping | [optional] [readonly] 
**ip_addresses** | **List[str]** | Array of ipAddress entries | [optional] [readonly] 

## Example

```python
from thousandeyes_sdk.administrative.models.interface_ip_mapping import InterfaceIpMapping

# TODO update the JSON string below
json = "{}"
# create an instance of InterfaceIpMapping from a JSON string
interface_ip_mapping_instance = InterfaceIpMapping.from_json(json)
# print the JSON string representation of the object
print(InterfaceIpMapping.to_json())

# convert the object into a dict
interface_ip_mapping_dict = interface_ip_mapping_instance.to_dict()
# create an instance of InterfaceIpMapping from a dict
interface_ip_mapping_from_dict = InterfaceIpMapping.from_dict(interface_ip_mapping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


