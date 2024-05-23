# ApiOutage

List of outages.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the outage. | [optional] 
**type** | **str** | The type of outage e.g. app. | [optional] 
**provider_name** | **str** | The name of the affected provider. | [optional] 
**provider_type** | **str** | The type of the affected provider. | [optional] 
**name** | **str** | The name of the affected application. | [optional] 
**start_date** | **str** | Date and time when the outage started. | [optional] 
**start_round_id** | **int** | Epoch time (seconds) when the outage started. | [optional] 
**end_date** | **str** | Date and time when the outage ended. | [optional] 
**end_round_id** | **int** | Epoch time (seconds) when the outage ended. | [optional] 
**duration** | **int** | Duration of the outage (seconds) | [optional] 
**affected_tests_count** | **int** | The number of affected tests | [optional] 
**affected_servers_count** | **int** | The number of affected servers | [optional] 
**affected_locations_count** | **int** | The number of affected locations. | [optional] 
**affected_interfaces_count** | **int** | The number of affected interfaces. | [optional] 
**asn** | **int** | ASN number. | [optional] 
**links** | [**SelfLinks**](SelfLinks.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.internet_insights.models.api_outage import ApiOutage

# TODO update the JSON string below
json = "{}"
# create an instance of ApiOutage from a JSON string
api_outage_instance = ApiOutage.from_json(json)
# print the JSON string representation of the object
print(ApiOutage.to_json())

# convert the object into a dict
api_outage_dict = api_outage_instance.to_dict()
# create an instance of ApiOutage from a dict
api_outage_from_dict = ApiOutage.from_dict(api_outage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


