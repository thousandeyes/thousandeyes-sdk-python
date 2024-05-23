# Traceroute


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination** | **str** | The target IP address. | [optional] [readonly] 
**error** | **str** | Only present when there is an error | [optional] [readonly] 
**info_flags** | **List[str]** |  | [optional] [readonly] 
**internal_errors** | **List[str]** |  | [optional] [readonly] 
**hops** | [**List[TracerouteHop]**](TracerouteHop.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_test_results.models.traceroute import Traceroute

# TODO update the JSON string below
json = "{}"
# create an instance of Traceroute from a JSON string
traceroute_instance = Traceroute.from_json(json)
# print the JSON string representation of the object
print(Traceroute.to_json())

# convert the object into a dict
traceroute_dict = traceroute_instance.to_dict()
# create an instance of Traceroute from a dict
traceroute_from_dict = Traceroute.from_dict(traceroute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


