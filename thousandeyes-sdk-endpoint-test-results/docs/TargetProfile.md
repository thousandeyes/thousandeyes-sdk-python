# TargetProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**remote_port** | **int** | The remote port of a network flow towards the target. | [optional] [readonly] 
**remote_ip_address** | **str** | The remote IP address of a network flow towards the target. | [optional] [readonly] 
**protocol** | [**TestProtocol**](TestProtocol.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_test_results.models.target_profile import TargetProfile

# TODO update the JSON string below
json = "{}"
# create an instance of TargetProfile from a JSON string
target_profile_instance = TargetProfile.from_json(json)
# print the JSON string representation of the object
print(TargetProfile.to_json())

# convert the object into a dict
target_profile_dict = target_profile_instance.to_dict()
# create an instance of TargetProfile from a dict
target_profile_from_dict = TargetProfile.from_dict(target_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


