# EndpointAsnDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**as_number** | **int** | Autonomous system number. | 
**as_name** | **str** | Name of autonomous system. | [optional] 

## Example

```python
from thousandeyes_sdk.endpoint_agents.models.endpoint_asn_details import EndpointAsnDetails

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointAsnDetails from a JSON string
endpoint_asn_details_instance = EndpointAsnDetails.from_json(json)
# print the JSON string representation of the object
print(EndpointAsnDetails.to_json())

# convert the object into a dict
endpoint_asn_details_dict = endpoint_asn_details_instance.to_dict()
# create an instance of EndpointAsnDetails from a dict
endpoint_asn_details_from_dict = EndpointAsnDetails.from_dict(endpoint_asn_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


