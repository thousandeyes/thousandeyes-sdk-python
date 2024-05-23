# ApiRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assertions** | [**List[ApiRequestAssertion]**](ApiRequestAssertion.md) | List of assertion objects. | [optional] 
**auth_type** | [**ApiRequestAuthType**](ApiRequestAuthType.md) |  | [optional] 
**bearer_token** | **str** | The bearer token if &#x60;authType &#x3D; bearer-token&#x60;. | [optional] 
**body** | **str** | POST/PUT request body. Must be in JSON format. | [optional] 
**collect_api_response** | **str** | Set to &#x60;true&#x60; if API response body should be collected and saved. Set to &#x60;false&#x60; if API response body should not be saved. | [optional] [default to 'true']
**headers** | [**List[ApiRequestHeader]**](ApiRequestHeader.md) | Array of API Request Header objects. | [optional] 
**method** | [**ApiRequestMethod**](ApiRequestMethod.md) |  | [optional] 
**name** | **str** | API step name, must be unique. | 
**password** | **str** | The password if &#x60;authType &#x3D; basic&#x60;. | [optional] 
**url** | **str** | Request url. Supports variables in the format &#x60;{{variableName}}&#x60;. | 
**username** | **str** | The username if &#x60;authType &#x3D; basic&#x60;. | [optional] 
**variables** | [**List[ApiRequestVariable]**](ApiRequestVariable.md) | Array of API post request variable objects. | [optional] 
**wait_time_ms** | **float** | Post request delay before executing the next API requests, in milliseconds. | [optional] 

## Example

```python
from thousandeyes_sdk.tests.models.api_request import ApiRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiRequest from a JSON string
api_request_instance = ApiRequest.from_json(json)
# print the JSON string representation of the object
print(ApiRequest.to_json())

# convert the object into a dict
api_request_dict = api_request_instance.to_dict()
# create an instance of ApiRequest from a dict
api_request_from_dict = ApiRequest.from_dict(api_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


