# ApiRequestHeader


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Request header key. | [optional] 
**value** | **str** | Request header value. Supports variables &#x60;{{variableName}}&#x60;. | [optional] 

## Example

```python
from thousandeyes_sdk.tests.models.api_request_header import ApiRequestHeader

# TODO update the JSON string below
json = "{}"
# create an instance of ApiRequestHeader from a JSON string
api_request_header_instance = ApiRequestHeader.from_json(json)
# print the JSON string representation of the object
print(ApiRequestHeader.to_json())

# convert the object into a dict
api_request_header_dict = api_request_header_instance.to_dict()
# create an instance of ApiRequestHeader from a dict
api_request_header_from_dict = ApiRequestHeader.from_dict(api_request_header_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


