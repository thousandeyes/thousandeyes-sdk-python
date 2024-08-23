# ApiApplicationOutageDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the outage. | [optional] 
**provider_name** | **str** | The name of the affected provider. | [optional] 
**provider_type** | **str** | The type of the affected provider. | [optional] 
**application_name** | **str** | The name of the affected application. | [optional] 
**start_date** | **str** | Date and time when the outage started. | [optional] 
**start_round_id** | **int** | Epoch time (seconds) when the outage started. | [optional] 
**end_date** | **str** | Date and time when the outage ended. | [optional] 
**end_round_id** | **int** | Epoch time (seconds) when the outage ended. | [optional] 
**duration** | **int** | Duration of the outage in seconds. | [optional] 
**affected_tests** | [**List[InternetInsightsApiAffectedTest]**](InternetInsightsApiAffectedTest.md) | List of affected tests. | [optional] 
**affected_domains** | **List[str]** | List of affected domains. | [optional] 
**affected_agents** | [**List[InternetInsightsApiAffectedAgent]**](InternetInsightsApiAffectedAgent.md) | List of affected agents. | [optional] 
**errors** | **List[str]** | List of errors. | [optional] 
**affected_locations** | [**List[ApiApplicationOutageAffectedLocation]**](ApiApplicationOutageAffectedLocation.md) | List of affected locations. | [optional] 
**links** | [**SelfLinks**](SelfLinks.md) |  | [optional] 

## Example

```python
from thousandeyes_sdk.internet_insights.models.api_application_outage_details import ApiApplicationOutageDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ApiApplicationOutageDetails from a JSON string
api_application_outage_details_instance = ApiApplicationOutageDetails.from_json(json)
# print the JSON string representation of the object
print(ApiApplicationOutageDetails.to_json())

# convert the object into a dict
api_application_outage_details_dict = api_application_outage_details_instance.to_dict()
# create an instance of ApiApplicationOutageDetails from a dict
api_application_outage_details_from_dict = ApiApplicationOutageDetails.from_dict(api_application_outage_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


