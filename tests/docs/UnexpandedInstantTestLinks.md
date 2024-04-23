# UnexpandedInstantTestLinks

A list of links that can be accessed to get more information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | [**UnexpandedInstantTestLinksSelf**](UnexpandedInstantTestLinksSelf.md) |  | [optional] 
**test_results** | [**List[Link]**](Link.md) | Reference to the test results. | [optional] 

## Example

```python
from tests.models.unexpanded_instant_test_links import UnexpandedInstantTestLinks

# TODO update the JSON string below
json = "{}"
# create an instance of UnexpandedInstantTestLinks from a JSON string
unexpanded_instant_test_links_instance = UnexpandedInstantTestLinks.from_json(json)
# print the JSON string representation of the object
print(UnexpandedInstantTestLinks.to_json())

# convert the object into a dict
unexpanded_instant_test_links_dict = unexpanded_instant_test_links_instance.to_dict()
# create an instance of UnexpandedInstantTestLinks from a dict
unexpanded_instant_test_links_from_dict = UnexpandedInstantTestLinks.from_dict(unexpanded_instant_test_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


