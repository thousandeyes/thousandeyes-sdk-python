# EndpointMonitoringSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**monitoring_settings_id** | **str** | Unique ID of the monitoring settings. | [optional] [readonly] 
**monitoring_settings_type** | [**EndpointMonitoringSettingsType**](EndpointMonitoringSettingsType.md) |  | 
**agent_ids** | **List[str]** | Endpoint Agent IDs selected by the monitoring settings. | [optional] 
**tag_ids** | **List[str]** | Endpoint Agent tag IDs selected by the monitoring settings. | [optional] 
**label_ids** | **List[str]** | Legacy Endpoint Agent label IDs selected by the monitoring settings. | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_tests.models.endpoint_monitoring_settings import EndpointMonitoringSettings

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointMonitoringSettings from a JSON string
endpoint_monitoring_settings_instance = EndpointMonitoringSettings.from_json(json)
# print the JSON string representation of the object
print(EndpointMonitoringSettings.to_json())

# convert the object into a dict
endpoint_monitoring_settings_dict = endpoint_monitoring_settings_instance.to_dict()
# create an instance of EndpointMonitoringSettings from a dict
endpoint_monitoring_settings_from_dict = EndpointMonitoringSettings.from_dict(endpoint_monitoring_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


