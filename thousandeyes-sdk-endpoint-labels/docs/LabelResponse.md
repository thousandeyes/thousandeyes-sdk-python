# LabelResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Label identifier. | [optional] [readonly] 
**name** | **str** | The label name. | [optional] 
**color** | **str** | UI color | [optional] 
**match_type** | [**MatchType**](MatchType.md) |  | [optional] 
**filters** | [**List[Filter]**](Filter.md) | The filters combined using the matchType to determine the label&#39;s match. | [optional] 
**links** | [**SelfLinks**](SelfLinks.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_labels.models.label_response import LabelResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LabelResponse from a JSON string
label_response_instance = LabelResponse.from_json(json)
# print the JSON string representation of the object
print(LabelResponse.to_json())

# convert the object into a dict
label_response_dict = label_response_instance.to_dict()
# create an instance of LabelResponse from a dict
label_response_from_dict = LabelResponse.from_dict(label_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


