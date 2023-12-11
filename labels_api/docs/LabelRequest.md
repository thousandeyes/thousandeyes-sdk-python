# LabelRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the new label - this must be unique. | [optional] 
**ids** | **List[str]** | Array of agent/test/dashboard ids the label should be assigned to, depending on the type of label | [optional] 

## Example

```python
from labels_api.models.label_request import LabelRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LabelRequest from a JSON string
label_request_instance = LabelRequest.from_json(json)
# print the JSON string representation of the object
print LabelRequest.to_json()

# convert the object into a dict
label_request_dict = label_request_instance.to_dict()
# create an instance of LabelRequest from a dict
label_request_form_dict = label_request.from_dict(label_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


