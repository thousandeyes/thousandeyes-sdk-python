# ExporterConfigAuthorization

Authentication configuration type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**o_auth2** | [**ExporterConfigOAuth2**](ExporterConfigOAuth2.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.streaming.models.exporter_config_authorization import ExporterConfigAuthorization

# TODO update the JSON string below
json = "{}"
# create an instance of ExporterConfigAuthorization from a JSON string
exporter_config_authorization_instance = ExporterConfigAuthorization.from_json(json)
# print the JSON string representation of the object
print(ExporterConfigAuthorization.to_json())

# convert the object into a dict
exporter_config_authorization_dict = exporter_config_authorization_instance.to_dict()
# create an instance of ExporterConfigAuthorization from a dict
exporter_config_authorization_from_dict = ExporterConfigAuthorization.from_dict(exporter_config_authorization_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


