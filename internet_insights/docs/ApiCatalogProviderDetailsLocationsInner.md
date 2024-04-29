# ApiCatalogProviderDetailsLocationsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location** | **str** | The location covered by the Provider. | [optional] 
**interfaces_count** | **int** | The number of interfaces covered by the Provider at this location. | [optional] 

## Example

```python
from internet_insights.models.api_catalog_provider_details_locations_inner import ApiCatalogProviderDetailsLocationsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiCatalogProviderDetailsLocationsInner from a JSON string
api_catalog_provider_details_locations_inner_instance = ApiCatalogProviderDetailsLocationsInner.from_json(json)
# print the JSON string representation of the object
print(ApiCatalogProviderDetailsLocationsInner.to_json())

# convert the object into a dict
api_catalog_provider_details_locations_inner_dict = api_catalog_provider_details_locations_inner_instance.to_dict()
# create an instance of ApiCatalogProviderDetailsLocationsInner from a dict
api_catalog_provider_details_locations_inner_from_dict = ApiCatalogProviderDetailsLocationsInner.from_dict(api_catalog_provider_details_locations_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


