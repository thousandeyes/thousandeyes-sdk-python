# BgpHop


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asn** | **int** | ASN of transit autonomous system | [optional] [readonly] 
**as_name** | **str** | Name of autonomous system. | [optional] [readonly] 

## Example

```python
from thousandeyes_sdk.test_results.models.bgp_hop import BgpHop

# TODO update the JSON string below
json = "{}"
# create an instance of BgpHop from a JSON string
bgp_hop_instance = BgpHop.from_json(json)
# print the JSON string representation of the object
print(BgpHop.to_json())

# convert the object into a dict
bgp_hop_dict = bgp_hop_instance.to_dict()
# create an instance of BgpHop from a dict
bgp_hop_from_dict = BgpHop.from_dict(bgp_hop_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


