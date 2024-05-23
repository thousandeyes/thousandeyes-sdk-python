# DynamicTestLinks

A list of links that can be accessed to get more information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | [**DynamicTestSelfLink**](DynamicTestSelfLink.md) |  | [optional] 
**test_results** | [**List[Link]**](Link.md) | Reference to the test results. | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_test_results.models.dynamic_test_links import DynamicTestLinks

# TODO update the JSON string below
json = "{}"
# create an instance of DynamicTestLinks from a JSON string
dynamic_test_links_instance = DynamicTestLinks.from_json(json)
# print the JSON string representation of the object
print(DynamicTestLinks.to_json())

# convert the object into a dict
dynamic_test_links_dict = dynamic_test_links_instance.to_dict()
# create an instance of DynamicTestLinks from a dict
dynamic_test_links_from_dict = DynamicTestLinks.from_dict(dynamic_test_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


