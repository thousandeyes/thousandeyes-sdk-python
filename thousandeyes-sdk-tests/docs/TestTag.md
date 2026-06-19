# TestTag


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique tag ID. | [optional] 
**key** | **str** | Tag key. For example, \&quot;Location\&quot; or \&quot;Department\&quot;. | [optional] 
**value** | **str** | Tag value. For example, \&quot;San Francisco\&quot; or \&quot;Engineering\&quot;. | [optional] 

## Example

```python
from thousandeyes_sdk.tests.models.test_tag import TestTag

# TODO update the JSON string below
json = "{}"
# create an instance of TestTag from a JSON string
test_tag_instance = TestTag.from_json(json)
# print the JSON string representation of the object
print(TestTag.to_json())

# convert the object into a dict
test_tag_dict = test_tag_instance.to_dict()
# create an instance of TestTag from a dict
test_tag_from_dict = TestTag.from_dict(test_tag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


