# BgpUpdates


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**updates** | [**List[BgpUpdate]**](BgpUpdate.md) |  | [optional] 
**links** | [**PaginationLinks**](PaginationLinks.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.bgp_updates.models.bgp_updates import BgpUpdates

# TODO update the JSON string below
json = "{}"
# create an instance of BgpUpdates from a JSON string
bgp_updates_instance = BgpUpdates.from_json(json)
# print the JSON string representation of the object
print(BgpUpdates.to_json())

# convert the object into a dict
bgp_updates_dict = bgp_updates_instance.to_dict()
# create an instance of BgpUpdates from a dict
bgp_updates_from_dict = BgpUpdates.from_dict(bgp_updates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


