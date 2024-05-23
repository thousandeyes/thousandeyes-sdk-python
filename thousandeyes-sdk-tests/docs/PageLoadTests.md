# PageLoadTests


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tests** | [**List[UnexpandedPageLoadTest]**](UnexpandedPageLoadTest.md) |  | [optional] 
**links** | [**SelfLinks**](SelfLinks.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.tests.models.page_load_tests import PageLoadTests

# TODO update the JSON string below
json = "{}"
# create an instance of PageLoadTests from a JSON string
page_load_tests_instance = PageLoadTests.from_json(json)
# print the JSON string representation of the object
print(PageLoadTests.to_json())

# convert the object into a dict
page_load_tests_dict = page_load_tests_instance.to_dict()
# create an instance of PageLoadTests from a dict
page_load_tests_from_dict = PageLoadTests.from_dict(page_load_tests_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


