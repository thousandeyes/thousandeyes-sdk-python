# EndpointHttpTestUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interval** | [**TestInterval**](TestInterval.md) |  | [optional] 
**test_name** | **str** | Name of the test. | [optional] 
**protocol** | [**EndpointTestProtocol**](EndpointTestProtocol.md) |  | [optional] 
**is_enabled** | **bool** | Indicates if test is enabled. | [optional] [default to True]
**tcp_probe_mode** | [**TestProbeMode**](TestProbeMode.md) |  | [optional] 
**url** | **str** | The test target URL. You can optionally specify the protocol (&#x60;http&#x60; or &#x60;https&#x60;).   - **Default Protocol:** If no protocol is specified, &#x60;https&#x60; is used by default.  - **Port Number:** To specify a port, append it to the URL with a colon after the hostname or IP address (e.g., &#x60;https://example.com:443&#x60;).      - If no port is specified in the URL, the &#x60;port&#x60; is determined by the default for protocol (HTTP: 80, HTTPS: 443).  | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_tests.models.endpoint_http_test_update import EndpointHttpTestUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointHttpTestUpdate from a JSON string
endpoint_http_test_update_instance = EndpointHttpTestUpdate.from_json(json)
# print the JSON string representation of the object
print(EndpointHttpTestUpdate.to_json())

# convert the object into a dict
endpoint_http_test_update_dict = endpoint_http_test_update_instance.to_dict()
# create an instance of EndpointHttpTestUpdate from a dict
endpoint_http_test_update_from_dict = EndpointHttpTestUpdate.from_dict(endpoint_http_test_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


