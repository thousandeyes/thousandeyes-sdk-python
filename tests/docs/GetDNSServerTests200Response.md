# GetDNSServerTests200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tests** | [**List[UnexpandedDnsServerTest]**](UnexpandedDnsServerTest.md) |  | [optional] 
**links** | [**SelfLinksLinks**](SelfLinksLinks.md) |  | [optional] 

## Example

```python
from tests.models.get_dns_server_tests200_response import GetDNSServerTests200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetDNSServerTests200Response from a JSON string
get_dns_server_tests200_response_instance = GetDNSServerTests200Response.from_json(json)
# print the JSON string representation of the object
print(GetDNSServerTests200Response.to_json())

# convert the object into a dict
get_dns_server_tests200_response_dict = get_dns_server_tests200_response_instance.to_dict()
# create an instance of GetDNSServerTests200Response from a dict
get_dns_server_tests200_response_from_dict = GetDNSServerTests200Response.from_dict(get_dns_server_tests200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

