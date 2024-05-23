# EndpointUserProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_name** | **str** |  | 

## Example

```python
from thousandeyes_sdk.endpoint_agents.models.endpoint_user_profile import EndpointUserProfile

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointUserProfile from a JSON string
endpoint_user_profile_instance = EndpointUserProfile.from_json(json)
# print the JSON string representation of the object
print(EndpointUserProfile.to_json())

# convert the object into a dict
endpoint_user_profile_dict = endpoint_user_profile_instance.to_dict()
# create an instance of EndpointUserProfile from a dict
endpoint_user_profile_from_dict = EndpointUserProfile.from_dict(endpoint_user_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


