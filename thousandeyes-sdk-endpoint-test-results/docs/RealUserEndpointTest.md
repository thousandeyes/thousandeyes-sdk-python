# RealUserEndpointTest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_id** | **str** | Unique ID of endpoint agent, from &#x60;/endpoint/agents&#x60; endpoint. | [optional] [readonly] 
**committed** | **datetime** | UTC date when endpoint real user test was committed to the controller (ISO date-time format). | [optional] [readonly] 
**var_date** | **datetime** | UTC date when endpoint real user test took place (ISO date-time format). | [optional] [readonly] 
**experience_score** | **float** | Score rating a user’s experience when loading a particular page, from 0 (the worst) to 1 (the best). [More details](https://docs.thousandeyes.com/product-documentation/end-user-monitoring/viewing-data/endpoint-agent-views-reference#user-experience-score). | [optional] [readonly] 
**number_of_pages** | **int** | Number of web pages visited on target website. | [optional] [readonly] 
**organization_name** | **str** | Name of the AS organization &#x60;sourceAddress&#x60; belongs to. | [optional] [readonly] 
**port** | **int** | Port used to visit target website. | [optional] [readonly] 
**protocol** | **str** | Protocol used to visit target website. | [optional] [readonly] 
**round_id** | **int** | Epoch time (seconds) indicating the start time of the round. | [optional] [readonly] 
**source_address** | **str** | Public IP address of the endpoint agent during the session. | [optional] [readonly] 
**id** | **str** | Endpoint real user test ID. Each endpoint real user test occurrence has a unique ID. | [optional] [readonly] 
**visited_site** | **str** | Domain used to visit target website. | [optional] [readonly] 
**page_id** | **str** | Web page ID. The page ID is unique only within an endpoint real user test. | [optional] [readonly] 

## Example

```python
from thousandeyes_sdk.endpoint_test_results.models.real_user_endpoint_test import RealUserEndpointTest

# TODO update the JSON string below
json = "{}"
# create an instance of RealUserEndpointTest from a JSON string
real_user_endpoint_test_instance = RealUserEndpointTest.from_json(json)
# print the JSON string representation of the object
print(RealUserEndpointTest.to_json())

# convert the object into a dict
real_user_endpoint_test_dict = real_user_endpoint_test_instance.to_dict()
# create an instance of RealUserEndpointTest from a dict
real_user_endpoint_test_from_dict = RealUserEndpointTest.from_dict(real_user_endpoint_test_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


