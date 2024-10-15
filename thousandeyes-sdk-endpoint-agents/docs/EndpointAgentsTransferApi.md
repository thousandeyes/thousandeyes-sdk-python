# thousandeyes_sdk.endpoint_agents.EndpointAgentsTransferApi

All URIs are relative to *https://api.thousandeyes.com/v7*

Method | HTTP request | Description
------------- | ------------- | -------------
[**transfer_endpoint_agent**](EndpointAgentsTransferApi.md#transfer_endpoint_agent) | **POST** /endpoint/agents/{agentId}/transfer | Transfer endpoint agent
[**transfer_endpoint_agents**](EndpointAgentsTransferApi.md#transfer_endpoint_agents) | **POST** /endpoint/agents/transfer/bulk | Bulk transfer agents


# **transfer_endpoint_agent**
> transfer_endpoint_agent(agent_id, agent_transfer_request, aid=aid)

Transfer endpoint agent

Initiates the transfer of an agent from its current account, which must correspond to the provided aid, to the target account.  **Note:** It is essential to ensure that the `aid` parameter matches the current account of the agent for this operation to succeed. 

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.endpoint_agents
from thousandeyes_sdk.endpoint_agents.models.agent_transfer_request import AgentTransferRequest
from thousandeyes_sdk.endpoint_agents.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.thousandeyes.com/v7
# See configuration.py for a list of all supported configuration parameters.
configuration = thousandeyes_sdk.core.Configuration(
    host = "https://api.thousandeyes.com/v7"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = thousandeyes_sdk.core.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with thousandeyes_sdk.core.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = thousandeyes_sdk.endpoint_agents.EndpointAgentsTransferApi(api_client)
    agent_id = 'agent_id_example' # str | The identifier of the agent to operate on.
    agent_transfer_request = thousandeyes_sdk.endpoint_agents.AgentTransferRequest() # AgentTransferRequest | The request to move an agent between accounts.
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Transfer endpoint agent
        api_instance.transfer_endpoint_agent(agent_id, agent_transfer_request, aid=aid)
    except Exception as e:
        print("Exception when calling EndpointAgentsTransferApi->transfer_endpoint_agent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **str**| The identifier of the agent to operate on. | 
 **agent_transfer_request** | [**AgentTransferRequest**](AgentTransferRequest.md)| The request to move an agent between accounts. | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Transfer initiated |  -  |
**401** | Unauthorized |  -  |
**403** | Insufficient permissions to query endpoint |  -  |
**404** | Not found |  -  |
**429** | Exhausted rate limit for the organization |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transfer_endpoint_agents**
> BulkAgentTransferResponse transfer_endpoint_agents(aid=aid, bulk_agent_transfer_request=bulk_agent_transfer_request)

Bulk transfer agents

Initiates the transfer of multiple agents between accounts. The following conditions apply:  * The requester must possess 'write' permissions for both the 'from' and 'to' accounts involved in each transfer.  * Multiple transfers may involve a mix of different source and destination accounts. * For each transfer request, the 'from' account must match the current account of the respective agent. * Transfers are executed asynchronously. * Progress tracking is not intended, but users can monitor the progress by periodically polling the 'get agent' endpoint. * Each transfer request is individually validated and completed; this operation is not atomic, meaning transfers can succeed or fail individually. * The API response provides the status of each transfer request. 

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.endpoint_agents
from thousandeyes_sdk.endpoint_agents.models.bulk_agent_transfer_request import BulkAgentTransferRequest
from thousandeyes_sdk.endpoint_agents.models.bulk_agent_transfer_response import BulkAgentTransferResponse
from thousandeyes_sdk.endpoint_agents.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.thousandeyes.com/v7
# See configuration.py for a list of all supported configuration parameters.
configuration = thousandeyes_sdk.core.Configuration(
    host = "https://api.thousandeyes.com/v7"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = thousandeyes_sdk.core.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with thousandeyes_sdk.core.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = thousandeyes_sdk.endpoint_agents.EndpointAgentsTransferApi(api_client)
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)
    bulk_agent_transfer_request = thousandeyes_sdk.endpoint_agents.BulkAgentTransferRequest() # BulkAgentTransferRequest | A collection of `AgentTransfers`. (optional)

    try:
        # Bulk transfer agents
        api_response = api_instance.transfer_endpoint_agents(aid=aid, bulk_agent_transfer_request=bulk_agent_transfer_request)
        print("The response of EndpointAgentsTransferApi->transfer_endpoint_agents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointAgentsTransferApi->transfer_endpoint_agents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 
 **bulk_agent_transfer_request** | [**BulkAgentTransferRequest**](BulkAgentTransferRequest.md)| A collection of &#x60;AgentTransfers&#x60;. | [optional] 

### Return type

[**BulkAgentTransferResponse**](BulkAgentTransferResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, text/plain
 - **Accept**: application/hal+json, application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**207** | Transfer initiated |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Insufficient permissions to query endpoint |  -  |
**404** | Not found |  -  |
**429** | Exhausted rate limit for the organization |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

