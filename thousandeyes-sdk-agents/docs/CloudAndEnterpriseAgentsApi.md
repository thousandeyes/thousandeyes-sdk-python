# thousandeyes_sdk.agents.CloudAndEnterpriseAgentsApi

All URIs are relative to *https://api.thousandeyes.com/v7*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_agent**](CloudAndEnterpriseAgentsApi.md#delete_agent) | **DELETE** /agents/{agentId} | Delete Enterprise Agent
[**get_agent**](CloudAndEnterpriseAgentsApi.md#get_agent) | **GET** /agents/{agentId} | Retrieve Cloud and Enterprise Agent
[**get_agents**](CloudAndEnterpriseAgentsApi.md#get_agents) | **GET** /agents | List Cloud and Enterprise Agents
[**update_agent**](CloudAndEnterpriseAgentsApi.md#update_agent) | **PUT** /agents/{agentId} | Update Enterprise Agent


# **delete_agent**
> delete_agent(agent_id, aid=aid)

Delete Enterprise Agent

Deletes an Enterprise Agent.  Important notes related to agent removal: * If an agent is deleted, the modification date for tests using that agent at the time it was deleted will be changed. * If a deleted agent is the final remaining agent on a test, then the test will be disabled when the agent is removed. * If an agent is removed, it must be re-initialized to use the same machine again in different context. Virtual Appliances can be updated using the Reset State button in the Advanced tab of the agent management interface. Users running packaged versions of Linux will need to remove /var/lib/te-agent/\\*.sqlite in order to reinitialize an agent.

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.agents
from thousandeyes_sdk.agents.rest import ApiException
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
    api_instance = thousandeyes_sdk.agents.CloudAndEnterpriseAgentsApi(api_client)
    agent_id = '281474976710706' # str | Unique ID for the agent.
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Delete Enterprise Agent
        api_instance.delete_agent(agent_id, aid=aid)
    except Exception as e:
        print("Exception when calling CloudAndEnterpriseAgentsApi->delete_agent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **str**| Unique ID for the agent. | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No content |  -  |
**401** | Unauthorized |  -  |
**403** | Insufficient permissions to query endpoint |  -  |
**404** | Not found |  -  |
**429** | Exhausted rate limit for the organization |  -  |
**500** | Internal server error |  -  |
**502** | Bad Gateway |  -  |
**0** | An error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_agent**
> AgentDetails get_agent(agent_id, aid=aid, expand=expand)

Retrieve Cloud and Enterprise Agent

Returns details for an agent, including assigned tests.  For Enterprise Agents, this operation returns additional details, including utilization data, assigned accounts, a list of account groups the agent is assigned to, and utilization details. 

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.agents
from thousandeyes_sdk.agents.models.agent_details import AgentDetails
from thousandeyes_sdk.agents.models.agent_details_expand import AgentDetailsExpand
from thousandeyes_sdk.agents.rest import ApiException
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
    api_instance = thousandeyes_sdk.agents.CloudAndEnterpriseAgentsApi(api_client)
    agent_id = '281474976710706' # str | Unique ID for the agent.
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)
    expand = [thousandeyes_sdk.agents.AgentDetailsExpand()] # List[AgentDetailsExpand] | Optional parameter, off by default. Indicates which agent sub-resource to expand. For example, if you wish to expand the `clusterMembers` sub-resource, pass the `?expand=cluster-member` query. (optional)

    try:
        # Retrieve Cloud and Enterprise Agent
        api_response = api_instance.get_agent(agent_id, aid=aid, expand=expand)
        print("The response of CloudAndEnterpriseAgentsApi->get_agent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudAndEnterpriseAgentsApi->get_agent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **str**| Unique ID for the agent. | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 
 **expand** | [**List[AgentDetailsExpand]**](AgentDetailsExpand.md)| Optional parameter, off by default. Indicates which agent sub-resource to expand. For example, if you wish to expand the &#x60;clusterMembers&#x60; sub-resource, pass the &#x60;?expand&#x3D;cluster-member&#x60; query. | [optional] 

### Return type

[**AgentDetails**](AgentDetails.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json, application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Insufficient permissions to query endpoint |  -  |
**404** | Not found |  -  |
**429** | Exhausted rate limit for the organization |  -  |
**500** | Internal server error |  -  |
**502** | Bad Gateway |  -  |
**0** | An error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_agents**
> CloudEnterpriseAgents get_agents(aid=aid, expand=expand, agent_types=agent_types)

List Cloud and Enterprise Agents

Returns a list of all agents available to your ThousandEyes account, including both Enterprise and Cloud Agents.  If an agent is an Enterprise Agent, this operation returns the agent’s public and private IP addresses, as well as the public network where the agent is located. 

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.agents
from thousandeyes_sdk.agents.models.agent_list_expand import AgentListExpand
from thousandeyes_sdk.agents.models.cloud_enterprise_agent_type import CloudEnterpriseAgentType
from thousandeyes_sdk.agents.models.cloud_enterprise_agents import CloudEnterpriseAgents
from thousandeyes_sdk.agents.rest import ApiException
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
    api_instance = thousandeyes_sdk.agents.CloudAndEnterpriseAgentsApi(api_client)
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)
    expand = [thousandeyes_sdk.agents.AgentListExpand()] # List[AgentListExpand] | Optional parameter, off by default. Indicates which agent sub-resource to expand. For example, if you wish to expand the `clusterMembers` sub-resource, pass the `?expand=cluster-member` query. (optional)
    agent_types = [thousandeyes_sdk.agents.CloudEnterpriseAgentType()] # List[CloudEnterpriseAgentType] | Specifies the type of agent to request. (optional)

    try:
        # List Cloud and Enterprise Agents
        api_response = api_instance.get_agents(aid=aid, expand=expand, agent_types=agent_types)
        print("The response of CloudAndEnterpriseAgentsApi->get_agents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudAndEnterpriseAgentsApi->get_agents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 
 **expand** | [**List[AgentListExpand]**](AgentListExpand.md)| Optional parameter, off by default. Indicates which agent sub-resource to expand. For example, if you wish to expand the &#x60;clusterMembers&#x60; sub-resource, pass the &#x60;?expand&#x3D;cluster-member&#x60; query. | [optional] 
 **agent_types** | [**List[CloudEnterpriseAgentType]**](CloudEnterpriseAgentType.md)| Specifies the type of agent to request. | [optional] 

### Return type

[**CloudEnterpriseAgents**](CloudEnterpriseAgents.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json, application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Insufficient permissions to query endpoint |  -  |
**404** | Not found |  -  |
**429** | Exhausted rate limit for the organization |  -  |
**500** | Internal server error |  -  |
**502** | Bad Gateway |  -  |
**0** | An error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_agent**
> AgentDetails update_agent(agent_id, agent_request, aid=aid, expand=expand)

Update Enterprise Agent

Updates details for an Enterprise Agent. This operation can only be used for Enterprise Agents, and only for users in a role that permits modification of Enterprise Agents.  Important notes related to agent modification on tests: * if an agent is removed from a test, the modification date for tests using that agent at the time it was removed will be changed. * If an agent is removed from an entire account group, then all tests using this agent in the removed account group will be updated to reflect the removed agent. * If a removed agent is the final remaining agent on a test, then the test will be disabled when the agent is removed.  Users can update the following fields: * `agentName`: String representation of an agent. No two agents can have the same display name. * `enabled`: Boolean representation of agent state. * `accountGroups`: An array of account group ids. See `v7/account-groups` to pull a list of account IDs. * `tests`: An array of test Is. See `v7/tests` to retrieve a list tests available in the current account context. * `ipv6Policy`: Enum representation of the IP version policy. * `keepBrowserCache`: Boolean representation of the Keep browser cache state. * `targetForTests`: String representation of the target IP address or domain name. This represents the test destination when agent is acting as a test target in an agent-to-agent test. * `localResolutionPrefixes`: This array of strings represents the public IP ranges where the Enterprise Agent performs rDNS (Reverse DNS) lookups. The range should be in CIDR notation, such as `10.1.1.0/24`. Please note that a maximum of 5 prefixes is allowed. This only applies to Enterprise Agents and Enterprise Agent clusters.

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.agents
from thousandeyes_sdk.agents.models.agent_details import AgentDetails
from thousandeyes_sdk.agents.models.agent_details_expand import AgentDetailsExpand
from thousandeyes_sdk.agents.models.agent_request import AgentRequest
from thousandeyes_sdk.agents.rest import ApiException
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
    api_instance = thousandeyes_sdk.agents.CloudAndEnterpriseAgentsApi(api_client)
    agent_id = '281474976710706' # str | Unique ID for the agent.
    agent_request = thousandeyes_sdk.agents.AgentRequest() # AgentRequest | 
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)
    expand = [thousandeyes_sdk.agents.AgentDetailsExpand()] # List[AgentDetailsExpand] | Optional parameter, off by default. Indicates which agent sub-resource to expand. For example, if you wish to expand the `clusterMembers` sub-resource, pass the `?expand=cluster-member` query. (optional)

    try:
        # Update Enterprise Agent
        api_response = api_instance.update_agent(agent_id, agent_request, aid=aid, expand=expand)
        print("The response of CloudAndEnterpriseAgentsApi->update_agent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudAndEnterpriseAgentsApi->update_agent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **str**| Unique ID for the agent. | 
 **agent_request** | [**AgentRequest**](AgentRequest.md)|  | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 
 **expand** | [**List[AgentDetailsExpand]**](AgentDetailsExpand.md)| Optional parameter, off by default. Indicates which agent sub-resource to expand. For example, if you wish to expand the &#x60;clusterMembers&#x60; sub-resource, pass the &#x60;?expand&#x3D;cluster-member&#x60; query. | [optional] 

### Return type

[**AgentDetails**](AgentDetails.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json, application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Insufficient permissions to query endpoint |  -  |
**404** | Not found |  -  |
**429** | Exhausted rate limit for the organization |  -  |
**500** | Internal server error |  -  |
**502** | Bad Gateway |  -  |
**0** | An error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

