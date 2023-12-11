# GetSuppressionWindows200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alert_suppression_windows** | [**List[AlertSuppressionWindowsAlertSuppressionWindowsInner]**](AlertSuppressionWindowsAlertSuppressionWindowsInner.md) |  | [optional] 
**links** | [**SelfLinksLinks**](SelfLinksLinks.md) |  | [optional] 

## Example

```python
from alerts_api.models.get_suppression_windows200_response import GetSuppressionWindows200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetSuppressionWindows200Response from a JSON string
get_suppression_windows200_response_instance = GetSuppressionWindows200Response.from_json(json)
# print the JSON string representation of the object
print GetSuppressionWindows200Response.to_json()

# convert the object into a dict
get_suppression_windows200_response_dict = get_suppression_windows200_response_instance.to_dict()
# create an instance of GetSuppressionWindows200Response from a dict
get_suppression_windows200_response_form_dict = get_suppression_windows200_response.from_dict(get_suppression_windows200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


