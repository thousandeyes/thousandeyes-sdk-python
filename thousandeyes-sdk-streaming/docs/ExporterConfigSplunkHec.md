# ExporterConfigSplunkHec

Splunk HEC configuration. This can only be configured when the `type` is `splunk-hec`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** | The Splunk HEC &#x60;token&#x60;. This is a required field. | [optional] 
**source** | **str** | The Splunk HEC &#x60;source&#x60;. This field is optional. | [optional] [default to 'ThousandEyesOTel']
**source_type** | **str** | The Splunk HEC &#x60;sourceType&#x60;. This field is optional. | [optional] [default to 'ThousandEyesOTel']
**index** | **str** | The name of the Splunk HEC index where the event data will be stored.  This field is optional. | [optional] 

## Example

```python
from thousandeyes_sdk.streaming.models.exporter_config_splunk_hec import ExporterConfigSplunkHec

# TODO update the JSON string below
json = "{}"
# create an instance of ExporterConfigSplunkHec from a JSON string
exporter_config_splunk_hec_instance = ExporterConfigSplunkHec.from_json(json)
# print the JSON string representation of the object
print(ExporterConfigSplunkHec.to_json())

# convert the object into a dict
exporter_config_splunk_hec_dict = exporter_config_splunk_hec_instance.to_dict()
# create an instance of ExporterConfigSplunkHec from a dict
exporter_config_splunk_hec_from_dict = ExporterConfigSplunkHec.from_dict(exporter_config_splunk_hec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


