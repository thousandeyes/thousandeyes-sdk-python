# AffectedCount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** | The total number affected. | [optional] [readonly] 
**in_account_group** | **int** | Indicates if in the affected account group. | [optional] [readonly] 

## Example

```python
from thousandeyes_sdk.event_detection.models.affected_count import AffectedCount

# TODO update the JSON string below
json = "{}"
# create an instance of AffectedCount from a JSON string
affected_count_instance = AffectedCount.from_json(json)
# print the JSON string representation of the object
print(AffectedCount.to_json())

# convert the object into a dict
affected_count_dict = affected_count_instance.to_dict()
# create an instance of AffectedCount from a dict
affected_count_from_dict = AffectedCount.from_dict(affected_count_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


