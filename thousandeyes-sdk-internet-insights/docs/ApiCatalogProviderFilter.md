# ApiCatalogProviderFilter

Advanced filter query used to filter the response. The provider name, location, asn can be partial names. Can filter on: - Provider name - Provider type - Region - Location - ASN - included

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider_name** | **str** | The name of the catalog provider. | [optional] 
**provider_type** | **str** | The type of catalog provider. | [optional] 
**region** | **str** | The catalog provider region. | [optional] 
**location** | **str** | Location of the catalog provider. | [optional] 
**asn** | **str** | Name of the ASN (Autonomous Systems Number) covered by providers. | [optional] 
**included** | **bool** | Indicates whether the catalog provider is included in the licensed packages. true returns providers covered by licensed packages, false returns providers not covered by licensed packages. | [optional] 

## Example

```python
from thousandeyes_sdk.internet_insights.models.api_catalog_provider_filter import ApiCatalogProviderFilter

# TODO update the JSON string below
json = "{}"
# create an instance of ApiCatalogProviderFilter from a JSON string
api_catalog_provider_filter_instance = ApiCatalogProviderFilter.from_json(json)
# print the JSON string representation of the object
print(ApiCatalogProviderFilter.to_json())

# convert the object into a dict
api_catalog_provider_filter_dict = api_catalog_provider_filter_instance.to_dict()
# create an instance of ApiCatalogProviderFilter from a dict
api_catalog_provider_filter_from_dict = ApiCatalogProviderFilter.from_dict(api_catalog_provider_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


