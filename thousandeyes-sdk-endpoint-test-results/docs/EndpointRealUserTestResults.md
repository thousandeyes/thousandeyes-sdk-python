# EndpointRealUserTestResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[EndpointRealUserTest]**](EndpointRealUserTest.md) |  | [optional] 
**start_date** | **datetime** | (Optional) When passing &#x60;window&#x60; or &#x60;startDate&#x60; parameter,  the client will also receive the &#x60;startDate&#x60; field indicating the UTC start date of the data&#39;s time range being retrieved  (ISO date-time format). | [optional] [readonly] 
**end_date** | **datetime** | (Optional) When passing &#x60;window&#x60; or &#x60;endDate&#x60; parameter,  the client will also receive the &#x60;endDate&#x60; field indicating the UTC end date of the data&#39;s time range being retrieved  (ISO date-time format). | [optional] [readonly] 
**links** | [**PaginationNextLink**](PaginationNextLink.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_test_results.models.endpoint_real_user_test_results import EndpointRealUserTestResults

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointRealUserTestResults from a JSON string
endpoint_real_user_test_results_instance = EndpointRealUserTestResults.from_json(json)
# print the JSON string representation of the object
print(EndpointRealUserTestResults.to_json())

# convert the object into a dict
endpoint_real_user_test_results_dict = endpoint_real_user_test_results_instance.to_dict()
# create an instance of EndpointRealUserTestResults from a dict
endpoint_real_user_test_results_from_dict = EndpointRealUserTestResults.from_dict(endpoint_real_user_test_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

