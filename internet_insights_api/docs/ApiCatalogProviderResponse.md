# ApiCatalogProviderResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**SelfLinksLinks**](SelfLinksLinks.md) |  | [optional] 
**providers** | [**List[ApiCatalogProviderResponseAllOfProvidersInner]**](ApiCatalogProviderResponseAllOfProvidersInner.md) | List of catalog providers. | [optional] 

## Example

```python
from internet_insights_api.models.api_catalog_provider_response import ApiCatalogProviderResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApiCatalogProviderResponse from a JSON string
api_catalog_provider_response_instance = ApiCatalogProviderResponse.from_json(json)
# print the JSON string representation of the object
print ApiCatalogProviderResponse.to_json()

# convert the object into a dict
api_catalog_provider_response_dict = api_catalog_provider_response_instance.to_dict()
# create an instance of ApiCatalogProviderResponse from a dict
api_catalog_provider_response_form_dict = api_catalog_provider_response.from_dict(api_catalog_provider_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


