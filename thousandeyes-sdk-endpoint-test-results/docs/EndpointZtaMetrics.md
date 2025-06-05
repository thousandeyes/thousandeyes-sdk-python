# EndpointZtaMetrics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**loss** | **float** | Percentage of packets that failed to reach the destination. | [optional] 
**avg_latency** | **int** | Average latency in milliseconds. | [optional] 
**jitter** | **int** | Standard deviation of latency in milliseconds. | [optional] 
**error_message** | **str** | Error message if an error occurred. | [optional] 
**type** | [**EndpointZtaSegmentType**](EndpointZtaSegmentType.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_test_results.models.endpoint_zta_metrics import EndpointZtaMetrics

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointZtaMetrics from a JSON string
endpoint_zta_metrics_instance = EndpointZtaMetrics.from_json(json)
# print the JSON string representation of the object
print(EndpointZtaMetrics.to_json())

# convert the object into a dict
endpoint_zta_metrics_dict = endpoint_zta_metrics_instance.to_dict()
# create an instance of EndpointZtaMetrics from a dict
endpoint_zta_metrics_from_dict = EndpointZtaMetrics.from_dict(endpoint_zta_metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


