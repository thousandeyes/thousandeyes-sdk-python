# ProviderLocation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location** | **str** | The location covered by the Provider. | [optional] 
**interfaces_count** | **int** | The number of interfaces covered by the Provider at this location. | [optional] 

## Example

```python
from thousandeyes_sdk.internet_insights.models.provider_location import ProviderLocation

# TODO update the JSON string below
json = "{}"
# create an instance of ProviderLocation from a JSON string
provider_location_instance = ProviderLocation.from_json(json)
# print the JSON string representation of the object
print(ProviderLocation.to_json())

# convert the object into a dict
provider_location_dict = provider_location_instance.to_dict()
# create an instance of ProviderLocation from a dict
provider_location_from_dict = ProviderLocation.from_dict(provider_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


