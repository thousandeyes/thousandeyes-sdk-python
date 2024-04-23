# V7EndpointLabelsPostRequest


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
from endpoint_labels.models.v7_endpoint_labels_post_request import V7EndpointLabelsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V7EndpointLabelsPostRequest from a JSON string
v7_endpoint_labels_post_request_instance = V7EndpointLabelsPostRequest.from_json(json)
# print the JSON string representation of the object
print(V7EndpointLabelsPostRequest.to_json())

# convert the object into a dict
v7_endpoint_labels_post_request_dict = v7_endpoint_labels_post_request_instance.to_dict()
# create an instance of V7EndpointLabelsPostRequest from a dict
v7_endpoint_labels_post_request_from_dict = V7EndpointLabelsPostRequest.from_dict(v7_endpoint_labels_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


