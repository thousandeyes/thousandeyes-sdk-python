# ApiCatalogProviderDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The catalog provider ID. | [optional] 
**provider_name** | **str** | The name of the catalog provider. | [optional] 
**provider_type** | **str** | The type of catalog provider. | [optional] 
**region** | **str** | The catalog provider region. | [optional] 
**data_type** | **str** | The type of data produced by the provider. | [optional] 
**asns** | [**List[ApiAsn]**](ApiAsn.md) | List of ASN&#39;s covered by the Provider. | [optional] 
**locations** | [**List[ProviderLocation]**](ProviderLocation.md) | List of locations covered by the Provider. | [optional] 
**links** | [**SelfLinks**](SelfLinks.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.internet_insights.models.api_catalog_provider_details import ApiCatalogProviderDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ApiCatalogProviderDetails from a JSON string
api_catalog_provider_details_instance = ApiCatalogProviderDetails.from_json(json)
# print the JSON string representation of the object
print(ApiCatalogProviderDetails.to_json())

# convert the object into a dict
api_catalog_provider_details_dict = api_catalog_provider_details_instance.to_dict()
# create an instance of ApiCatalogProviderDetails from a dict
api_catalog_provider_details_from_dict = ApiCatalogProviderDetails.from_dict(api_catalog_provider_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


