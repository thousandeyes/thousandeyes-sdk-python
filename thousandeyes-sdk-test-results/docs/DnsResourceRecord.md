# DnsResourceRecord

A DNS resource record from the question or answer section.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Record name. | [optional] [readonly] 
**type** | [**DnsResourceRecordType**](DnsResourceRecordType.md) |  | [optional] 
**var_class** | [**DnsResourceRecordClass**](DnsResourceRecordClass.md) |  | [optional] 
**ttl** | **int** | Time to live in seconds. | [optional] [readonly] 
**data** | **str** | Record data (RDATA). | [optional] [readonly] 

## Example

```python
from thousandeyes_sdk.test_results.models.dns_resource_record import DnsResourceRecord

# TODO update the JSON string below
json = "{}"
# create an instance of DnsResourceRecord from a JSON string
dns_resource_record_instance = DnsResourceRecord.from_json(json)
# print the JSON string representation of the object
print(DnsResourceRecord.to_json())

# convert the object into a dict
dns_resource_record_dict = dns_resource_record_instance.to_dict()
# create an instance of DnsResourceRecord from a dict
dns_resource_record_from_dict = DnsResourceRecord.from_dict(dns_resource_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


