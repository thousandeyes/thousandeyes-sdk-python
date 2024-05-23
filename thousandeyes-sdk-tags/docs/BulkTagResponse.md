# BulkTagResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tags** | [**List[Tag]**](Tag.md) |  | [optional] 
**errors** | [**List[TagBulkCreateError]**](TagBulkCreateError.md) |  | [optional] [readonly] 

## Example

```python
from thousandeyes_sdk.tags.models.bulk_tag_response import BulkTagResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BulkTagResponse from a JSON string
bulk_tag_response_instance = BulkTagResponse.from_json(json)
# print the JSON string representation of the object
print(BulkTagResponse.to_json())

# convert the object into a dict
bulk_tag_response_dict = bulk_tag_response_instance.to_dict()
# create an instance of BulkTagResponse from a dict
bulk_tag_response_from_dict = BulkTagResponse.from_dict(bulk_tag_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


