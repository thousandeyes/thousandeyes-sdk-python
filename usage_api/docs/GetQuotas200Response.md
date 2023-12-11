# GetQuotas200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quotas** | [**List[QuotasQuotasInner]**](QuotasQuotasInner.md) |  | [optional] 
**links** | [**SelfLinksLinks**](SelfLinksLinks.md) |  | [optional] 

## Example

```python
from usage_api.models.get_quotas200_response import GetQuotas200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetQuotas200Response from a JSON string
get_quotas200_response_instance = GetQuotas200Response.from_json(json)
# print the JSON string representation of the object
print GetQuotas200Response.to_json()

# convert the object into a dict
get_quotas200_response_dict = get_quotas200_response_instance.to_dict()
# create an instance of GetQuotas200Response from a dict
get_quotas200_response_form_dict = get_quotas200_response.from_dict(get_quotas200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


