# DnsTiming

Timing metrics for a DNS lookup.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_time_us** | **str** | Unix epoch timestamp in microseconds when the DNS query started. | [optional] [readonly] 
**total_time_us** | **int** | Total DNS lookup time in microseconds. | [optional] [readonly] 

## Example

```python
from thousandeyes_sdk.test_results.models.dns_timing import DnsTiming

# TODO update the JSON string below
json = "{}"
# create an instance of DnsTiming from a JSON string
dns_timing_instance = DnsTiming.from_json(json)
# print the JSON string representation of the object
print(DnsTiming.to_json())

# convert the object into a dict
dns_timing_dict = dns_timing_instance.to_dict()
# create an instance of DnsTiming from a dict
dns_timing_from_dict = DnsTiming.from_dict(dns_timing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


