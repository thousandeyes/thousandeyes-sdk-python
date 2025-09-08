# ExternalMetadataItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | ID of the device that has the Cisco Secure Client deployed with the Internet Security module. | [optional] 
**value** | **str** | Value of the external metadata property. | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_agents.models.external_metadata_item import ExternalMetadataItem

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalMetadataItem from a JSON string
external_metadata_item_instance = ExternalMetadataItem.from_json(json)
# print the JSON string representation of the object
print(ExternalMetadataItem.to_json())

# convert the object into a dict
external_metadata_item_dict = external_metadata_item_instance.to_dict()
# create an instance of ExternalMetadataItem from a dict
external_metadata_item_from_dict = ExternalMetadataItem.from_dict(external_metadata_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


