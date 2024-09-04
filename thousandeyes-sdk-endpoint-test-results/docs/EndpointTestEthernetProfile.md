# EndpointTestEthernetProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link_speed** | **int** | Ethernet profile link speed | [optional] [readonly] 

## Example

```python
from thousandeyes_sdk.endpoint_test_results.models.endpoint_test_ethernet_profile import EndpointTestEthernetProfile

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointTestEthernetProfile from a JSON string
endpoint_test_ethernet_profile_instance = EndpointTestEthernetProfile.from_json(json)
# print the JSON string representation of the object
print(EndpointTestEthernetProfile.to_json())

# convert the object into a dict
endpoint_test_ethernet_profile_dict = endpoint_test_ethernet_profile_instance.to_dict()
# create an instance of EndpointTestEthernetProfile from a dict
endpoint_test_ethernet_profile_from_dict = EndpointTestEthernetProfile.from_dict(endpoint_test_ethernet_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


