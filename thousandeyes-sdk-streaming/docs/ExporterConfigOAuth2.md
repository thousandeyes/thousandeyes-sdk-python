# ExporterConfigOAuth2

OAuth2 authentication configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** | The OAuth2 client ID. | [optional] 
**client_secret** | **str** | The OAuth2 client secret. | [optional] 
**token_url** | **str** | The OAuth2 token URL. | [optional] 
**scopes** | **List[str]** | The OAuth2 scopes. | [optional] 

## Example

```python
from thousandeyes_sdk.streaming.models.exporter_config_o_auth2 import ExporterConfigOAuth2

# TODO update the JSON string below
json = "{}"
# create an instance of ExporterConfigOAuth2 from a JSON string
exporter_config_o_auth2_instance = ExporterConfigOAuth2.from_json(json)
# print the JSON string representation of the object
print(ExporterConfigOAuth2.to_json())

# convert the object into a dict
exporter_config_o_auth2_dict = exporter_config_o_auth2_instance.to_dict()
# create an instance of ExporterConfigOAuth2 from a dict
exporter_config_o_auth2_from_dict = ExporterConfigOAuth2.from_dict(exporter_config_o_auth2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


