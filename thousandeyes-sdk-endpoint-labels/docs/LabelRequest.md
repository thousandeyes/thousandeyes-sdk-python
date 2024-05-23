# LabelRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Label identifier. | [optional] [readonly] 
**name** | **str** | The label name. | 
**color** | **str** | UI color | [optional] 
**match_type** | [**MatchType**](MatchType.md) |  | 
**filters** | [**List[Filter]**](Filter.md) | The filters combined using the matchType to determine the label&#39;s match. | 

## Example

```python
from thousandeyes_sdk.endpoint_labels.models.label_request import LabelRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LabelRequest from a JSON string
label_request_instance = LabelRequest.from_json(json)
# print the JSON string representation of the object
print(LabelRequest.to_json())

# convert the object into a dict
label_request_dict = label_request_instance.to_dict()
# create an instance of LabelRequest from a dict
label_request_from_dict = LabelRequest.from_dict(label_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


