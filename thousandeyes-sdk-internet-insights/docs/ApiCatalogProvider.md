# ApiCatalogProvider

Catalog provider

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The catalog provider ID. | [optional] 
**provider_name** | **str** | The name of the catalog provider. | [optional] 
**provider_type** | **str** | The type of catalog provider. | [optional] 
**region** | **str** | The catalog provider region. | [optional] 
**data_type** | **str** | The type of data produced by the provider. | [optional] 
**asns_count** | **int** | The number of ASN&#39;s covered by the provider. | [optional] 
**countries_count** | **int** | The number of countries covered by the provider. | [optional] 
**locations_count** | **int** | The number of locations covered by the provider. | [optional] 
**interfaces_count** | **int** | The number of interfaces covered by the provider. | [optional] 
**included** | **bool** | Indicates whether the catalog provider is included in the licensed packages. | [optional] 
**links** | [**SelfLinks**](SelfLinks.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.internet_insights.models.api_catalog_provider import ApiCatalogProvider

# TODO update the JSON string below
json = "{}"
# create an instance of ApiCatalogProvider from a JSON string
api_catalog_provider_instance = ApiCatalogProvider.from_json(json)
# print the JSON string representation of the object
print(ApiCatalogProvider.to_json())

# convert the object into a dict
api_catalog_provider_dict = api_catalog_provider_instance.to_dict()
# create an instance of ApiCatalogProvider from a dict
api_catalog_provider_from_dict = ApiCatalogProvider.from_dict(api_catalog_provider_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


