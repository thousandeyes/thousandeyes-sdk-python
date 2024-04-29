# TestLabelsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label_id** | **str** | Label ID. | [optional] 
**name** | **str** | Name of the label. | [optional] 
**is_builtin** | **bool** | Value indicating if the label in question is BuiltIn (Account Admin, Organization Admin, Regular User). | [optional] 

## Example

```python
from endpoint_instant_tests.models.test_labels_inner import TestLabelsInner

# TODO update the JSON string below
json = "{}"
# create an instance of TestLabelsInner from a JSON string
test_labels_inner_instance = TestLabelsInner.from_json(json)
# print the JSON string representation of the object
print(TestLabelsInner.to_json())

# convert the object into a dict
test_labels_inner_dict = test_labels_inner_instance.to_dict()
# create an instance of TestLabelsInner from a dict
test_labels_inner_from_dict = TestLabelsInner.from_dict(test_labels_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


