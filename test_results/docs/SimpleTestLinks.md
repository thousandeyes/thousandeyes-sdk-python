# SimpleTestLinks

A list of links that can be accessed to get more information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | [**SimpleTestLinksSelf**](SimpleTestLinksSelf.md) |  | [optional] 
**test_results** | [**List[Link]**](Link.md) | Reference to the test results. | [optional] 

## Example

```python
from test_results.models.simple_test_links import SimpleTestLinks

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleTestLinks from a JSON string
simple_test_links_instance = SimpleTestLinks.from_json(json)
# print the JSON string representation of the object
print(SimpleTestLinks.to_json())

# convert the object into a dict
simple_test_links_dict = simple_test_links_instance.to_dict()
# create an instance of SimpleTestLinks from a dict
simple_test_links_from_dict = SimpleTestLinks.from_dict(simple_test_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


