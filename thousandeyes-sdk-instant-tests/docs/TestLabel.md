# TestLabel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label_id** | **str** | Label ID. | [optional] 
**name** | **str** | Name of the label. | [optional] 
**is_builtin** | **bool** | Value indicating if the label in question is BuiltIn (Account Admin, Organization Admin, Regular User). | [optional] 

## Example

```python
from thousandeyes_sdk.instant_tests.models.test_label import TestLabel

# TODO update the JSON string below
json = "{}"
# create an instance of TestLabel from a JSON string
test_label_instance = TestLabel.from_json(json)
# print the JSON string representation of the object
print(TestLabel.to_json())

# convert the object into a dict
test_label_dict = test_label_instance.to_dict()
# create an instance of TestLabel from a dict
test_label_from_dict = TestLabel.from_dict(test_label_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


