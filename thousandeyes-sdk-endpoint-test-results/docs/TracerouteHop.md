# TracerouteHop


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hop** | **int** | The hop index. | [optional] [readonly] 
**ip_address** | **str** | IP address of the hop. | [optional] [readonly] 
**prefix** | **str** | Prefix of IP address shown in CIDR. | [optional] [readonly] 
**asn** | **int** | Unique number assigned to an organization (also referred to as service provider). | [optional] [readonly] 
**delay** | **int** | Hop delay | [optional] [readonly] 
**mpls** | **List[str]** | Hop Multiprotocol Label Switching. | [optional] [readonly] 
**name** | **str** | The hop name. | [optional] [readonly] 

## Example

```python
from thousandeyes_sdk.endpoint_test_results.models.traceroute_hop import TracerouteHop

# TODO update the JSON string below
json = "{}"
# create an instance of TracerouteHop from a JSON string
traceroute_hop_instance = TracerouteHop.from_json(json)
# print the JSON string representation of the object
print(TracerouteHop.to_json())

# convert the object into a dict
traceroute_hop_dict = traceroute_hop_instance.to_dict()
# create an instance of TracerouteHop from a dict
traceroute_hop_from_dict = TracerouteHop.from_dict(traceroute_hop_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


