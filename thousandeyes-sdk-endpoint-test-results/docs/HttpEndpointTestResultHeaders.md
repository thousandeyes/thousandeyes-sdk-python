# HttpEndpointTestResultHeaders

Expandable object containing both request and response headers.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_headers** | **str** | CRLF-delimited list of request headers in &#x60;header: value&#x60; format. | [optional] [readonly] 
**response_headers** | **str** | CRLF-delimited list of response headers in &#x60;header: value&#x60; format. | [optional] [readonly] 

## Example

```python
from thousandeyes_sdk.endpoint_test_results.models.http_endpoint_test_result_headers import HttpEndpointTestResultHeaders

# TODO update the JSON string below
json = "{}"
# create an instance of HttpEndpointTestResultHeaders from a JSON string
http_endpoint_test_result_headers_instance = HttpEndpointTestResultHeaders.from_json(json)
# print the JSON string representation of the object
print(HttpEndpointTestResultHeaders.to_json())

# convert the object into a dict
http_endpoint_test_result_headers_dict = http_endpoint_test_result_headers_instance.to_dict()
# create an instance of HttpEndpointTestResultHeaders from a dict
http_endpoint_test_result_headers_from_dict = HttpEndpointTestResultHeaders.from_dict(http_endpoint_test_result_headers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


