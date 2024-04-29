# Label


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label_id** | **str** | Unique ID of the label; this number is negative for built-in labels. Query &#x60;/v7/labels/{type}/{id}&#x60; endpoint to see the list of agent/test/dashboard ids with this label.  | [optional] 
**is_built_in** | **bool** | &#x60;true&#x60; for built-in labels, and &#x60;false&#x60; for user-created labels. Note that built-in labels are read-only.  | [optional] 
**name** | **str** | The name of the new label - this must be unique. | [optional] 
**type** | [**LabelType**](LabelType.md) |  | [optional] 

## Example

```python
from labels.models.label import Label

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


