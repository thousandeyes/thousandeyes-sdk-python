# BadRequestError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **int** |  | [optional] 
**http_status** | **str** |  | [optional] 
**errors** | **List[str]** |  | [optional] 
**path** | **str** |  | [optional] 

## Example

```python
from thousandeyes_sdk.streaming.models.bad_request_error import BadRequestError

# TODO update the JSON string below
json = "{}"
# create an instance of BadRequestError from a JSON string
bad_request_error_instance = BadRequestError.from_json(json)
# print the JSON string representation of the object
print(BadRequestError.to_json())

# convert the object into a dict
bad_request_error_dict = bad_request_error_instance.to_dict()
# create an instance of BadRequestError from a dict
bad_request_error_from_dict = BadRequestError.from_dict(bad_request_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


