# EthernetProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link_speed** | **int** | Ethernet profile link speed | [optional] [readonly] 

## Example

```python
from thousandeyes_sdk.endpoint_test_results.models.ethernet_profile import EthernetProfile

# TODO update the JSON string below
json = "{}"
# create an instance of EthernetProfile from a JSON string
ethernet_profile_instance = EthernetProfile.from_json(json)
# print the JSON string representation of the object
print(EthernetProfile.to_json())

# convert the object into a dict
ethernet_profile_dict = ethernet_profile_instance.to_dict()
# create an instance of EthernetProfile from a dict
ethernet_profile_from_dict = EthernetProfile.from_dict(ethernet_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


