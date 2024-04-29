# ApiCatalogProviderDetailsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The catalog provider ID. | [optional] 
**provider_name** | **str** | The name of the catalog provider. | [optional] 
**provider_type** | **str** | The type of catalog provider. | [optional] 
**region** | **str** | The catalog provider region. | [optional] 
**data_type** | **str** | The type of data produced by the provider. | [optional] 
**asns** | [**List[ApiAsn]**](ApiAsn.md) | List of ASN&#39;s covered by the Provider. | [optional] 
**locations** | [**List[ApiCatalogProviderDetailsLocationsInner]**](ApiCatalogProviderDetailsLocationsInner.md) | List of locations covered by the Provider. | [optional] 
**links** | [**SelfLinksLinks**](SelfLinksLinks.md) |  | [optional] 

## Example

```python
from internet_insights.models.api_catalog_provider_details_response import ApiCatalogProviderDetailsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApiCatalogProviderDetailsResponse from a JSON string
api_catalog_provider_details_response_instance = ApiCatalogProviderDetailsResponse.from_json(json)
# print the JSON string representation of the object
print(ApiCatalogProviderDetailsResponse.to_json())

# convert the object into a dict
api_catalog_provider_details_response_dict = api_catalog_provider_details_response_instance.to_dict()
# create an instance of ApiCatalogProviderDetailsResponse from a dict
api_catalog_provider_details_response_from_dict = ApiCatalogProviderDetailsResponse.from_dict(api_catalog_provider_details_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


