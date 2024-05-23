# Hop


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hop** | **int** | The hop index. | [optional] [readonly] 
**ip_address** | **str** | IP address of the hop. | [optional] [readonly] 
**prefix** | **str** | Prefix of IP address shown in CIDR. | [optional] [readonly] 

## Example

```python
from thousandeyes_sdk.endpoint_test_results.models.hop import Hop

# TODO update the JSON string below
json = "{}"
# create an instance of Hop from a JSON string
hop_instance = Hop.from_json(json)
# print the JSON string representation of the object
print(Hop.to_json())

# convert the object into a dict
hop_dict = hop_instance.to_dict()
# create an instance of Hop from a dict
hop_from_dict = Hop.from_dict(hop_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


