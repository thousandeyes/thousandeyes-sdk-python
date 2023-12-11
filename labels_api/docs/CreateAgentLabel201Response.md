# CreateAgentLabel201Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label_id** | **str** | Unique ID of the label; this number is negative for built-in labels. Query &#x60;/v7/labels/{type}/{id}&#x60; endpoint to see the list of agent/test/dashboard ids with this label.  | [optional] 
**is_built_in** | **bool** | &#x60;true&#x60; for built-in labels, and &#x60;false&#x60; for user-created labels. Note that built-in labels are read-only.  | [optional] 
**name** | **str** | The name of the new label - this must be unique. | [optional] 
**type** | [**LabelType**](LabelType.md) |  | [optional] 
**ids** | **List[str]** | Array of agent/test/dashboard IDs the label is assigned to, depending on the type of label. | [optional] 
**links** | [**SelfLinksLinks**](SelfLinksLinks.md) |  | [optional] 

## Example

```python
from labels_api.models.create_agent_label201_response import CreateAgentLabel201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAgentLabel201Response from a JSON string
create_agent_label201_response_instance = CreateAgentLabel201Response.from_json(json)
# print the JSON string representation of the object
print CreateAgentLabel201Response.to_json()

# convert the object into a dict
create_agent_label201_response_dict = create_agent_label201_response_instance.to_dict()
# create an instance of CreateAgentLabel201Response from a dict
create_agent_label201_response_form_dict = create_agent_label201_response.from_dict(create_agent_label201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


