# EndpointBrowserExtension


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**browser** | [**BrowserType**](BrowserType.md) |  | [optional] 
**profile** | **str** | Name of the browser profile where this extension is stored. | [optional] 
**version** | **str** | Endpoint agent browser extension version. | [optional] 
**enabled** | **bool** | Indicates if the extension is disabled or enabled in the web browser. | [optional] 
**active** | **bool** | Flag indicating if there is communication between the extension and ThousandEyes portal.  | [optional] 
**error** | **str** | Contains any errors encountered while getting extension status. | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_agents.models.endpoint_browser_extension import EndpointBrowserExtension

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointBrowserExtension from a JSON string
endpoint_browser_extension_instance = EndpointBrowserExtension.from_json(json)
# print the JSON string representation of the object
print(EndpointBrowserExtension.to_json())

# convert the object into a dict
endpoint_browser_extension_dict = endpoint_browser_extension_instance.to_dict()
# create an instance of EndpointBrowserExtension from a dict
endpoint_browser_extension_from_dict = EndpointBrowserExtension.from_dict(endpoint_browser_extension_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


