# EndpointWirelessConnectionFailure


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**EndpointWirelessConnectionFailureType**](EndpointWirelessConnectionFailureType.md) |  | [optional] 
**context** | **str** | Additional context for the wireless connection failure. | [optional] [readonly] 
**code** | **int** | Wireless connection failure code. | [optional] [readonly] 

## Example

```python
from thousandeyes_sdk.endpoint_agents.models.endpoint_wireless_connection_failure import EndpointWirelessConnectionFailure

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointWirelessConnectionFailure from a JSON string
endpoint_wireless_connection_failure_instance = EndpointWirelessConnectionFailure.from_json(json)
# print the JSON string representation of the object
print(EndpointWirelessConnectionFailure.to_json())

# convert the object into a dict
endpoint_wireless_connection_failure_dict = endpoint_wireless_connection_failure_instance.to_dict()
# create an instance of EndpointWirelessConnectionFailure from a dict
endpoint_wireless_connection_failure_from_dict = EndpointWirelessConnectionFailure.from_dict(endpoint_wireless_connection_failure_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


