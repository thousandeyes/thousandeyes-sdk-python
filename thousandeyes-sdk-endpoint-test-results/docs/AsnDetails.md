# AsnDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**as_name** | **str** | Name of the provider. | [optional] [readonly] 
**as_number** | **int** | Unique number assigned to an organization (also referred to as service provider). | [optional] [readonly] 

## Example

```python
from thousandeyes_sdk.endpoint_test_results.models.asn_details import AsnDetails

# TODO update the JSON string below
json = "{}"
# create an instance of AsnDetails from a JSON string
asn_details_instance = AsnDetails.from_json(json)
# print the JSON string representation of the object
print(AsnDetails.to_json())

# convert the object into a dict
asn_details_dict = asn_details_instance.to_dict()
# create an instance of AsnDetails from a dict
asn_details_from_dict = AsnDetails.from_dict(asn_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


