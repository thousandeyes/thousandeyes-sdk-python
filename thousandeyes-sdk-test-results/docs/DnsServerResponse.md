# DnsServerResponse

A DNS response received while resolving the HTTP test target.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | DNS message ID. | [optional] [readonly] 
**qr** | [**DnsQr**](DnsQr.md) |  | [optional] 
**opcode** | [**DnsOpcode**](DnsOpcode.md) |  | [optional] 
**authoritative_answer** | **bool** | DNS header AA flag. | [optional] [readonly] 
**truncation** | **bool** | DNS header TC flag. | [optional] [readonly] 
**recursion_desired** | **bool** | DNS header RD flag. | [optional] [readonly] 
**recursion_available** | **bool** | DNS header RA flag. | [optional] [readonly] 
**zero** | **bool** | DNS header Z flag. Reserved and expected to be false. | [optional] [readonly] 
**authentic_data** | **bool** | DNS header AD flag. | [optional] [readonly] 
**checking_disabled** | **bool** | DNS header CD flag. | [optional] [readonly] 
**response_code** | [**DnsResponseCode**](DnsResponseCode.md) |  | [optional] 
**question** | [**List[DnsResourceRecord]**](DnsResourceRecord.md) | Records in the DNS question section. | [optional] 
**answer** | [**List[DnsResourceRecord]**](DnsResourceRecord.md) | Records in the DNS answer section. | [optional] 
**dns_resolver** | **str** | DNS resolver that returned this response. | [optional] [readonly] 
**timing** | [**DnsTiming**](DnsTiming.md) |  | [optional] 
**protocol** | [**DnsMeasurementProtocol**](DnsMeasurementProtocol.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.test_results.models.dns_server_response import DnsServerResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DnsServerResponse from a JSON string
dns_server_response_instance = DnsServerResponse.from_json(json)
# print the JSON string representation of the object
print(DnsServerResponse.to_json())

# convert the object into a dict
dns_server_response_dict = dns_server_response_instance.to_dict()
# create an instance of DnsServerResponse from a dict
dns_server_response_from_dict = DnsServerResponse.from_dict(dns_server_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


