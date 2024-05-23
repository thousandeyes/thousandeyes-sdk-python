# Quotas


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quotas** | [**List[Quota]**](Quota.md) |  | [optional] 
**links** | [**SelfLinks**](SelfLinks.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.usage.models.quotas import Quotas

# TODO update the JSON string below
json = "{}"
# create an instance of Quotas from a JSON string
quotas_instance = Quotas.from_json(json)
# print the JSON string representation of the object
print(Quotas.to_json())

# convert the object into a dict
quotas_dict = quotas_instance.to_dict()
# create an instance of Quotas from a dict
quotas_from_dict = Quotas.from_dict(quotas_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


