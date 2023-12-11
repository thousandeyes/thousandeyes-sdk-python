# EndpointLabelsList200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**labels** | [**List[LabelsLabelsInner]**](LabelsLabelsInner.md) |  | [optional] 
**links** | [**SelfLinksLinks**](SelfLinksLinks.md) |  | [optional] 

## Example

```python
from labels_api.models.endpoint_labels_list200_response import EndpointLabelsList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointLabelsList200Response from a JSON string
endpoint_labels_list200_response_instance = EndpointLabelsList200Response.from_json(json)
# print the JSON string representation of the object
print EndpointLabelsList200Response.to_json()

# convert the object into a dict
endpoint_labels_list200_response_dict = endpoint_labels_list200_response_instance.to_dict()
# create an instance of EndpointLabelsList200Response from a dict
endpoint_labels_list200_response_form_dict = endpoint_labels_list200_response.from_dict(endpoint_labels_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


