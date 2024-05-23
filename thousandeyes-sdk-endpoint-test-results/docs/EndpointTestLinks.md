# EndpointTestLinks

A list of links that can be accessed to get more information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | [**EndpointTestSelfLink**](EndpointTestSelfLink.md) |  | [optional] 
**test_results** | [**List[Link]**](Link.md) | Reference to the test results. | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_test_results.models.endpoint_test_links import EndpointTestLinks

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointTestLinks from a JSON string
endpoint_test_links_instance = EndpointTestLinks.from_json(json)
# print the JSON string representation of the object
print(EndpointTestLinks.to_json())

# convert the object into a dict
endpoint_test_links_dict = endpoint_test_links_instance.to_dict()
# create an instance of EndpointTestLinks from a dict
endpoint_test_links_from_dict = EndpointTestLinks.from_dict(endpoint_test_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


