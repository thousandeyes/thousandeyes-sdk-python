# HttpServerTests


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tests** | [**List[HttpServerTest]**](HttpServerTest.md) |  | [optional] 

## Example

```python
from tests_api.models.http_server_tests import HttpServerTests

# TODO update the JSON string below
json = "{}"
# create an instance of HttpServerTests from a JSON string
http_server_tests_instance = HttpServerTests.from_json(json)
# print the JSON string representation of the object
print HttpServerTests.to_json()

# convert the object into a dict
http_server_tests_dict = http_server_tests_instance.to_dict()
# create an instance of HttpServerTests from a dict
http_server_tests_form_dict = http_server_tests.from_dict(http_server_tests_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


