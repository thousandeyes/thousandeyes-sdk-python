# HttpTestResultHeaders

Expandable object containing both request and response headers

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_headers** | **str** | Crlf-delimited list of request headers in header: value format | [optional] 
**response_headers** | **str** | crlf-delimited list of response headers in header: value format | [optional] 

## Example

```python
from thousandeyes_sdk.test_results.models.http_test_result_headers import HttpTestResultHeaders

# TODO update the JSON string below
json = "{}"
# create an instance of HttpTestResultHeaders from a JSON string
http_test_result_headers_instance = HttpTestResultHeaders.from_json(json)
# print the JSON string representation of the object
print(HttpTestResultHeaders.to_json())

# convert the object into a dict
http_test_result_headers_dict = http_test_result_headers_instance.to_dict()
# create an instance of HttpTestResultHeaders from a dict
http_test_result_headers_from_dict = HttpTestResultHeaders.from_dict(http_test_result_headers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


