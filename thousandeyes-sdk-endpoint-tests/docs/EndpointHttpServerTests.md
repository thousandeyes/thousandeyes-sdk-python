# EndpointHttpServerTests


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tests** | [**List[EndpointHttpServerTest]**](EndpointHttpServerTest.md) |  | [optional] 
**links** | [**SelfLinks**](SelfLinks.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_tests.models.endpoint_http_server_tests import EndpointHttpServerTests

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointHttpServerTests from a JSON string
endpoint_http_server_tests_instance = EndpointHttpServerTests.from_json(json)
# print the JSON string representation of the object
print(EndpointHttpServerTests.to_json())

# convert the object into a dict
endpoint_http_server_tests_dict = endpoint_http_server_tests_instance.to_dict()
# create an instance of EndpointHttpServerTests from a dict
endpoint_http_server_tests_from_dict = EndpointHttpServerTests.from_dict(endpoint_http_server_tests_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


