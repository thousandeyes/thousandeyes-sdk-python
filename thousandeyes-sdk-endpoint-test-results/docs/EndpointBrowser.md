# EndpointBrowser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Browser name. | [optional] [readonly] 
**version** | **str** | Browser version. | [optional] [readonly] 

## Example

```python
from thousandeyes_sdk.endpoint_test_results.models.endpoint_browser import EndpointBrowser

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointBrowser from a JSON string
endpoint_browser_instance = EndpointBrowser.from_json(json)
# print the JSON string representation of the object
print(EndpointBrowser.to_json())

# convert the object into a dict
endpoint_browser_dict = endpoint_browser_instance.to_dict()
# create an instance of EndpointBrowser from a dict
endpoint_browser_from_dict = EndpointBrowser.from_dict(endpoint_browser_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


