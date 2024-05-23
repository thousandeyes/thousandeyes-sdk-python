# TcpConnect


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rtt** | **float** | Represents the number of milliseconds required to establish TCP connectivity with the target | [optional] [readonly] 
**error_code** | **str** | Only present when there is an error | [optional] [readonly] 
**error** | **str** | Only present when there is an error | [optional] [readonly] 
**info_flags** | **List[str]** |  | [optional] [readonly] 

## Example

```python
from thousandeyes_sdk.endpoint_test_results.models.tcp_connect import TcpConnect

# TODO update the JSON string below
json = "{}"
# create an instance of TcpConnect from a JSON string
tcp_connect_instance = TcpConnect.from_json(json)
# print the JSON string representation of the object
print(TcpConnect.to_json())

# convert the object into a dict
tcp_connect_dict = tcp_connect_instance.to_dict()
# create an instance of TcpConnect from a dict
tcp_connect_from_dict = TcpConnect.from_dict(tcp_connect_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


