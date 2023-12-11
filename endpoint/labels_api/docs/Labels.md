# Labels

A list of Labels.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**labels** | [**List[LabelsLabelsInner]**](LabelsLabelsInner.md) |  | [optional] 

## Example

```python
from labels_api.models.labels import Labels

# TODO update the JSON string below
json = "{}"
# create an instance of Labels from a JSON string
labels_instance = Labels.from_json(json)
# print the JSON string representation of the object
print Labels.to_json()

# convert the object into a dict
labels_dict = labels_instance.to_dict()
# create an instance of Labels from a dict
labels_form_dict = labels.from_dict(labels_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


