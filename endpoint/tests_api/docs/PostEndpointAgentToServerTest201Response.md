# PostEndpointAgentToServerTest201Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**SelfLinksLinks**](SelfLinksLinks.md) |  | [optional] 
**agent_selector_config** | [**EndpointAgentSelectorConfig**](EndpointAgentSelectorConfig.md) |  | [optional] 
**created_date** | **datetime** | UTC created date (ISO date-time format). | [optional] [readonly] 
**interval** | [**TestInterval**](TestInterval.md) |  | [optional] 
**is_enabled** | **bool** | Indicates if test is enabled. | [optional] [readonly] [default to True]
**is_saved_event** | **bool** | Indicates if the test is a saved event. | [optional] [readonly] 
**has_path_trace_in_session** | **bool** | Enables \&quot;in session\&quot; path trace. When enabled, this option initiates a TCP session with the target server and sends path trace packets within the established TCP session. | [optional] 
**modified_date** | **datetime** | UTC last modification date (ISO date-time format). | [optional] [readonly] 
**network_measurements** | **bool** | Enable or disable network measurements. Set to true to enable or false to disable network measurements. | [optional] [default to True]
**port** | **int** | Port number, if not specified, the port is selected based on a protocol (HTTP 80, HTTPS 443). | [optional] 
**protocol** | [**EndpointTestProtocol**](EndpointTestProtocol.md) |  | [optional] 
**server** | **str** | Target domain name or IP address. | [optional] 
**test_id** | **str** | Each test is assigned a unique ID to access test data from other endpoints. | [optional] [readonly] 
**aid** | [**EndpointTestAid**](EndpointTestAid.md) |  | [optional] 
**test_name** | **str** | Name of the test. | [optional] 
**type** | [**EndpointAgentToServerType**](EndpointAgentToServerType.md) |  | [optional] 

## Example

```python
from tests_api.models.post_endpoint_agent_to_server_test201_response import PostEndpointAgentToServerTest201Response

# TODO update the JSON string below
json = "{}"
# create an instance of PostEndpointAgentToServerTest201Response from a JSON string
post_endpoint_agent_to_server_test201_response_instance = PostEndpointAgentToServerTest201Response.from_json(json)
# print the JSON string representation of the object
print PostEndpointAgentToServerTest201Response.to_json()

# convert the object into a dict
post_endpoint_agent_to_server_test201_response_dict = post_endpoint_agent_to_server_test201_response_instance.to_dict()
# create an instance of PostEndpointAgentToServerTest201Response from a dict
post_endpoint_agent_to_server_test201_response_form_dict = post_endpoint_agent_to_server_test201_response.from_dict(post_endpoint_agent_to_server_test201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


