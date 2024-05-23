# MonitorsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**monitors** | **List[str]** | Contains list of BGP monitor IDs (get &#x60;monitorId&#x60; from &#x60;/monitors&#x60; endpoint) | [optional] 

## Example

```python
from thousandeyes_sdk.tests.models.monitors_request import MonitorsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MonitorsRequest from a JSON string
monitors_request_instance = MonitorsRequest.from_json(json)
# print the JSON string representation of the object
print(MonitorsRequest.to_json())

# convert the object into a dict
monitors_request_dict = monitors_request_instance.to_dict()
# create an instance of MonitorsRequest from a dict
monitors_request_from_dict = MonitorsRequest.from_dict(monitors_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


