# Label

A label definition.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Label identifier. | [optional] [readonly] 
**name** | **str** | The label name. | [optional] 
**color** | **str** | UI color | [optional] 
**match_type** | [**MatchType**](MatchType.md) |  | [optional] 
**filters** | [**List[Filter]**](Filter.md) | The filters combined using the matchType to determine the label&#39;s match. | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_labels.models.label import Label

# TODO update the JSON string below
json = "{}"
# create an instance of Label from a JSON string
label_instance = Label.from_json(json)
# print the JSON string representation of the object
print(Label.to_json())

# convert the object into a dict
label_dict = label_instance.to_dict()
# create an instance of Label from a dict
label_from_dict = Label.from_dict(label_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


