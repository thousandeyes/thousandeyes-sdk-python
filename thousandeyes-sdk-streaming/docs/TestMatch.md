# TestMatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the test to match. | [optional] 
**domain** | [**TestMatchDomain**](TestMatchDomain.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.streaming.models.test_match import TestMatch

# TODO update the JSON string below
json = "{}"
# create an instance of TestMatch from a JSON string
test_match_instance = TestMatch.from_json(json)
# print the JSON string representation of the object
print(TestMatch.to_json())

# convert the object into a dict
test_match_dict = test_match_instance.to_dict()
# create an instance of TestMatch from a dict
test_match_from_dict = TestMatch.from_dict(test_match_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


