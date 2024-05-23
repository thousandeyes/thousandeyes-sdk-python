# ApiErrorIntegrationLimits


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **int** |  | [optional] 
**http_status** | **str** |  | [optional] 
**errors** | **List[str]** |  | [optional] 
**path** | **str** |  | [optional] 

## Example

```python
from thousandeyes_sdk.streaming.models.api_error_integration_limits import ApiErrorIntegrationLimits

# TODO update the JSON string below
json = "{}"
# create an instance of ApiErrorIntegrationLimits from a JSON string
api_error_integration_limits_instance = ApiErrorIntegrationLimits.from_json(json)
# print the JSON string representation of the object
print(ApiErrorIntegrationLimits.to_json())

# convert the object into a dict
api_error_integration_limits_dict = api_error_integration_limits_instance.to_dict()
# create an instance of ApiErrorIntegrationLimits from a dict
api_error_integration_limits_from_dict = ApiErrorIntegrationLimits.from_dict(api_error_integration_limits_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


