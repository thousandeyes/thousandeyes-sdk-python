# EndpointRealUserTest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile_id** | **str** | Unique ID of the monitoring profile. | [readonly] 
**aid** | **str** | A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. | 
**name** | **str** | Monitoring profile name. | [readonly] 
**included_domains** | **List[str]** | Domains included in real user monitoring. | 
**excluded_domains** | **List[str]** | Domains excluded from real user monitoring. | 
**monitoring_settings** | [**EndpointMonitoringSettings**](EndpointMonitoringSettings.md) |  | 

## Example

```python
from thousandeyes_sdk.endpoint_tests.models.endpoint_real_user_test import EndpointRealUserTest

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointRealUserTest from a JSON string
endpoint_real_user_test_instance = EndpointRealUserTest.from_json(json)
# print the JSON string representation of the object
print(EndpointRealUserTest.to_json())

# convert the object into a dict
endpoint_real_user_test_dict = endpoint_real_user_test_instance.to_dict()
# create an instance of EndpointRealUserTest from a dict
endpoint_real_user_test_from_dict = EndpointRealUserTest.from_dict(endpoint_real_user_test_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


