# ApiNetworkOutageDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the outage. | [optional] 
**provider_name** | **str** | The name of the affected provider. | [optional] 
**provider_type** | **str** | The type of the affected provider. | [optional] 
**network_name** | **str** | The affected network. | [optional] 
**asn** | **int** | ASN number | [optional] 
**start_date** | **str** | Date and time when the outage started. | [optional] 
**start_round_id** | **int** | Epoch time (seconds) when the outage started. | [optional] 
**end_date** | **str** | Date and time when the outage ended. | [optional] 
**end_round_id** | **int** | Epoch time (seconds) when the outage ended. | [optional] 
**duration** | **int** | Duration of the outage in seconds. | [optional] 
**affected_tests** | [**List[InternetInsightsApiAffectedTest]**](InternetInsightsApiAffectedTest.md) | List of affected tests. | [optional] 
**affected_domains** | **List[str]** | List of affected domains. | [optional] 
**affected_agents** | [**List[InternetInsightsApiAffectedAgent]**](InternetInsightsApiAffectedAgent.md) | List of affected agents. | [optional] 
**affected_locations** | [**List[ApiNetworkOutageAffectedLocation]**](ApiNetworkOutageAffectedLocation.md) | List of affected locations. | [optional] 
**links** | [**SelfLinks**](SelfLinks.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.internet_insights.models.api_network_outage_details import ApiNetworkOutageDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ApiNetworkOutageDetails from a JSON string
api_network_outage_details_instance = ApiNetworkOutageDetails.from_json(json)
# print the JSON string representation of the object
print(ApiNetworkOutageDetails.to_json())

# convert the object into a dict
api_network_outage_details_dict = api_network_outage_details_instance.to_dict()
# create an instance of ApiNetworkOutageDetails from a dict
api_network_outage_details_from_dict = ApiNetworkOutageDetails.from_dict(api_network_outage_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


