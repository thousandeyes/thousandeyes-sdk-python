# EndpointTestLinks

A list of links that can be accessed to get more information.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | [**EndpointTestLinksSelf**](EndpointTestLinksSelf.md) |  | [optional] 
**test_results** | [**EndpointTestLinksTestResults**](EndpointTestLinksTestResults.md) |  | [optional] 

## Example

```python
from test_results_api.models.endpoint_test_links import EndpointTestLinks

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointTestLinks from a JSON string
endpoint_test_links_instance = EndpointTestLinks.from_json(json)
# print the JSON string representation of the object
print EndpointTestLinks.to_json()

# convert the object into a dict
endpoint_test_links_dict = endpoint_test_links_instance.to_dict()
# create an instance of EndpointTestLinks from a dict
endpoint_test_links_form_dict = endpoint_test_links.from_dict(endpoint_test_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


