# ApiAsn


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ASN (Autonomous Systems Number) | [optional] 
**name** | **str** | ASN (Autonomous Systems Number) name | [optional] 

## Example

```python
from thousandeyes_sdk.internet_insights.models.api_asn import ApiAsn

# TODO update the JSON string below
json = "{}"
# create an instance of ApiAsn from a JSON string
api_asn_instance = ApiAsn.from_json(json)
# print the JSON string representation of the object
print(ApiAsn.to_json())

# convert the object into a dict
api_asn_dict = api_asn_instance.to_dict()
# create an instance of ApiAsn from a dict
api_asn_from_dict = ApiAsn.from_dict(api_asn_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


