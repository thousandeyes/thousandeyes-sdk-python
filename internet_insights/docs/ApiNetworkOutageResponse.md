# ApiNetworkOutageResponse


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
**affected_tests** | [**List[ApiAffectedTest]**](ApiAffectedTest.md) | List of affected tests. | [optional] 
**affected_domains** | **List[str]** | List of affected domains. | [optional] 
**affected_agents** | [**List[ApiAffectedAgent]**](ApiAffectedAgent.md) | List of affected agents. | [optional] 
**affected_locations** | [**List[ApiNetworkOutageAffectedLocation]**](ApiNetworkOutageAffectedLocation.md) | List of affected locations. | [optional] 
**links** | [**SelfLinksLinks**](SelfLinksLinks.md) |  | [optional] 

## Example

```python
from internet_insights.models.api_network_outage_response import ApiNetworkOutageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApiNetworkOutageResponse from a JSON string
api_network_outage_response_instance = ApiNetworkOutageResponse.from_json(json)
# print the JSON string representation of the object
print(ApiNetworkOutageResponse.to_json())

# convert the object into a dict
api_network_outage_response_dict = api_network_outage_response_instance.to_dict()
# create an instance of ApiNetworkOutageResponse from a dict
api_network_outage_response_from_dict = ApiNetworkOutageResponse.from_dict(api_network_outage_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


