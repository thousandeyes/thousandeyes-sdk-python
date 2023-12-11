# MultiTestIdNetworkTestResults


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[NetworkTestResult]**](NetworkTestResult.md) |  | [optional] 

## Example

```python
from test_results_api.models.multi_test_id_network_test_results import MultiTestIdNetworkTestResults

# TODO update the JSON string below
json = "{}"
# create an instance of MultiTestIdNetworkTestResults from a JSON string
multi_test_id_network_test_results_instance = MultiTestIdNetworkTestResults.from_json(json)
# print the JSON string representation of the object
print MultiTestIdNetworkTestResults.to_json()

# convert the object into a dict
multi_test_id_network_test_results_dict = multi_test_id_network_test_results_instance.to_dict()
# create an instance of MultiTestIdNetworkTestResults from a dict
multi_test_id_network_test_results_form_dict = multi_test_id_network_test_results.from_dict(multi_test_id_network_test_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


