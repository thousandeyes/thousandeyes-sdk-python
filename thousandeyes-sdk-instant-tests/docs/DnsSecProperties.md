# DnsSecProperties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | The target record for the test, with the record type suffixed. If no record type is specified, the test defaults to an ANY record. | 
**dns_query_class** | [**DnsQueryClass**](DnsQueryClass.md) |  | [optional] 
**randomized_start_time** | **bool** | Indicates whether agents should randomize the start time in each test round. | [optional] [default to False]
**type** | **str** |  | [optional] [readonly] 

## Example

```python
from thousandeyes_sdk.instant_tests.models.dns_sec_properties import DnsSecProperties

# TODO update the JSON string below
json = "{}"
# create an instance of DnsSecProperties from a JSON string
dns_sec_properties_instance = DnsSecProperties.from_json(json)
# print the JSON string representation of the object
print(DnsSecProperties.to_json())

# convert the object into a dict
dns_sec_properties_dict = dns_sec_properties_instance.to_dict()
# create an instance of DnsSecProperties from a dict
dns_sec_properties_from_dict = DnsSecProperties.from_dict(dns_sec_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


