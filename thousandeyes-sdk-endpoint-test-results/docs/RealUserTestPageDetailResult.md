# RealUserTestPageDetailResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**har** | **object** | A HAR object according to the [HTTP Archive 1.2 specifications](http://www.softwareishard.com/blog/har-12-spec/), with an additional &#x60;systemMetrics&#x60; property. | [optional] 
**links** | [**SelfLinks**](SelfLinks.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_test_results.models.real_user_test_page_detail_result import RealUserTestPageDetailResult

# TODO update the JSON string below
json = "{}"
# create an instance of RealUserTestPageDetailResult from a JSON string
real_user_test_page_detail_result_instance = RealUserTestPageDetailResult.from_json(json)
# print the JSON string representation of the object
print(RealUserTestPageDetailResult.to_json())

# convert the object into a dict
real_user_test_page_detail_result_dict = real_user_test_page_detail_result_instance.to_dict()
# create an instance of RealUserTestPageDetailResult from a dict
real_user_test_page_detail_result_from_dict = RealUserTestPageDetailResult.from_dict(real_user_test_page_detail_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


