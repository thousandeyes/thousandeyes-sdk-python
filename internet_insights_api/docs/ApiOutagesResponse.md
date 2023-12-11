# ApiOutagesResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**SelfLinksLinks**](SelfLinksLinks.md) |  | [optional] 
**outages** | [**List[ApiOutagesResponseAllOfOutagesInner]**](ApiOutagesResponseAllOfOutagesInner.md) | List of application outages. | [optional] 

## Example

```python
from internet_insights_api.models.api_outages_response import ApiOutagesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApiOutagesResponse from a JSON string
api_outages_response_instance = ApiOutagesResponse.from_json(json)
# print the JSON string representation of the object
print ApiOutagesResponse.to_json()

# convert the object into a dict
api_outages_response_dict = api_outages_response_instance.to_dict()
# create an instance of ApiOutagesResponse from a dict
api_outages_response_form_dict = api_outages_response.from_dict(api_outages_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


