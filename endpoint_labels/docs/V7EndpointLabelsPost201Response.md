# V7EndpointLabelsPost201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Label identifier. | [optional] [readonly] 
**name** | **str** | The label name. | [optional] 
**color** | **str** | UI color | [optional] 
**match_type** | [**MatchType**](MatchType.md) |  | [optional] 
**filters** | [**List[Filter]**](Filter.md) | The filters combined using the matchType to determine the label&#39;s match. | [optional] 
**links** | [**SelfLinksLinks**](SelfLinksLinks.md) |  | [optional] 

## Example

```python
from endpoint_labels.models.v7_endpoint_labels_post201_response import V7EndpointLabelsPost201Response

# TODO update the JSON string below
json = "{}"
# create an instance of V7EndpointLabelsPost201Response from a JSON string
v7_endpoint_labels_post201_response_instance = V7EndpointLabelsPost201Response.from_json(json)
# print the JSON string representation of the object
print(V7EndpointLabelsPost201Response.to_json())

# convert the object into a dict
v7_endpoint_labels_post201_response_dict = v7_endpoint_labels_post201_response_instance.to_dict()
# create an instance of V7EndpointLabelsPost201Response from a dict
v7_endpoint_labels_post201_response_from_dict = V7EndpointLabelsPost201Response.from_dict(v7_endpoint_labels_post201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


