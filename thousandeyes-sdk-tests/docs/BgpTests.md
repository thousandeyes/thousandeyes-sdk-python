# BgpTests


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tests** | [**List[UnexpandedBgpTest]**](UnexpandedBgpTest.md) |  | [optional] 
**links** | [**SelfLinks**](SelfLinks.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.tests.models.bgp_tests import BgpTests

# TODO update the JSON string below
json = "{}"
# create an instance of BgpTests from a JSON string
bgp_tests_instance = BgpTests.from_json(json)
# print the JSON string representation of the object
print(BgpTests.to_json())

# convert the object into a dict
bgp_tests_dict = bgp_tests_instance.to_dict()
# create an instance of BgpTests from a dict
bgp_tests_from_dict = BgpTests.from_dict(bgp_tests_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


