# DnsServerTestResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[DnsServerTestResult]**](DnsServerTestResult.md) |  | [optional] 
**test** | [**SimpleTest**](SimpleTest.md) |  | [optional] 
**start_date** | **datetime** | (Optional) When passing &#x60;window&#x60; or &#x60;startDate&#x60; parameter,  the client will also receive the &#x60;startDate&#x60; field indicating the UTC start date of the data&#39;s time range being retrieved  (ISO date-time format). | [optional] [readonly] 
**end_date** | **datetime** | (Optional) When passing &#x60;window&#x60; or &#x60;endDate&#x60; parameter,  the client will also receive the &#x60;endDate&#x60; field indicating the UTC end date of the data&#39;s time range being retrieved  (ISO date-time format). | [optional] [readonly] 
**links** | [**PaginationLinks**](PaginationLinks.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.test_results.models.dns_server_test_results import DnsServerTestResults

# TODO update the JSON string below
json = "{}"
# create an instance of DnsServerTestResults from a JSON string
dns_server_test_results_instance = DnsServerTestResults.from_json(json)
# print the JSON string representation of the object
print(DnsServerTestResults.to_json())

# convert the object into a dict
dns_server_test_results_dict = dns_server_test_results_instance.to_dict()
# create an instance of DnsServerTestResults from a dict
dns_server_test_results_from_dict = DnsServerTestResults.from_dict(dns_server_test_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

