# ExporterConfig

Capability to set exporter configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**splunk_hec** | [**ExporterConfigSplunkHec**](ExporterConfigSplunkHec.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.streaming.models.exporter_config import ExporterConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ExporterConfig from a JSON string
exporter_config_instance = ExporterConfig.from_json(json)
# print the JSON string representation of the object
print(ExporterConfig.to_json())

# convert the object into a dict
exporter_config_dict = exporter_config_instance.to_dict()
# create an instance of ExporterConfig from a dict
exporter_config_from_dict = ExporterConfig.from_dict(exporter_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


