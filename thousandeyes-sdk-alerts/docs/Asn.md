# Asn

Autonomous System Number (ASN) information for network outage alerts.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ASN identifier. | [optional] 
**name** | **str** | Autonomous system name. | [optional] 
**type** | **str** | Resource type. | [optional] 

## Example

```python
from thousandeyes_sdk.alerts.models.asn import Asn

# TODO update the JSON string below
json = "{}"
# create an instance of Asn from a JSON string
asn_instance = Asn.from_json(json)
# print the JSON string representation of the object
print(Asn.to_json())

# convert the object into a dict
asn_dict = asn_instance.to_dict()
# create an instance of Asn from a dict
asn_from_dict = Asn.from_dict(asn_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


