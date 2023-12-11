# LabelsLabelsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**SelfLinksLinks**](SelfLinksLinks.md) |  | [optional] 
**id** | **str** | Label identifier. | [optional] [readonly] 
**name** | **str** | The label name. | [optional] 
**color** | **str** | UI color | [optional] 
**match_type** | [**MatchType**](MatchType.md) |  | [optional] 
**filters** | [**List[Filter]**](Filter.md) | The filters combined using the matchType to determine the label&#39;s match. | [optional] 

## Example

```python
from labels_api.models.labels_labels_inner import LabelsLabelsInner

# TODO update the JSON string below
json = "{}"
# create an instance of LabelsLabelsInner from a JSON string
labels_labels_inner_instance = LabelsLabelsInner.from_json(json)
# print the JSON string representation of the object
print LabelsLabelsInner.to_json()

# convert the object into a dict
labels_labels_inner_dict = labels_labels_inner_instance.to_dict()
# create an instance of LabelsLabelsInner from a dict
labels_labels_inner_form_dict = labels_labels_inner.from_dict(labels_labels_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


