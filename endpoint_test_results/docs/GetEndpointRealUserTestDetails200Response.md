# GetEndpointRealUserTestDetails200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[EndpointRealUserTestDetail]**](EndpointRealUserTestDetail.md) |  | [optional] 
**links** | [**SelfLinksLinks**](SelfLinksLinks.md) |  | [optional] 

## Example

```python
from endpoint_test_results.models.get_endpoint_real_user_test_details200_response import GetEndpointRealUserTestDetails200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetEndpointRealUserTestDetails200Response from a JSON string
get_endpoint_real_user_test_details200_response_instance = GetEndpointRealUserTestDetails200Response.from_json(json)
# print the JSON string representation of the object
print(GetEndpointRealUserTestDetails200Response.to_json())

# convert the object into a dict
get_endpoint_real_user_test_details200_response_dict = get_endpoint_real_user_test_details200_response_instance.to_dict()
# create an instance of GetEndpointRealUserTestDetails200Response from a dict
get_endpoint_real_user_test_details200_response_from_dict = GetEndpointRealUserTestDetails200Response.from_dict(get_endpoint_real_user_test_details200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


