# thousandeyes_sdk.endpoint_agents.EndpointAgentsApi

All URIs are relative to *https://api.thousandeyes.com/v7*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_endpoint_agent**](EndpointAgentsApi.md#delete_endpoint_agent) | **DELETE** /endpoint/agents/{agentId} | Delete endpoint agent
[**disable_endpoint_agent**](EndpointAgentsApi.md#disable_endpoint_agent) | **POST** /endpoint/agents/{agentId}/disable | Disable endpoint agent
[**enable_endpoint_agent**](EndpointAgentsApi.md#enable_endpoint_agent) | **POST** /endpoint/agents/{agentId}/enable | Enable endpoint agent
[**filter_endpoint_agents**](EndpointAgentsApi.md#filter_endpoint_agents) | **POST** /endpoint/agents/filter | Filter endpoint agents
[**get_endpoint_agent**](EndpointAgentsApi.md#get_endpoint_agent) | **GET** /endpoint/agents/{agentId} | Retrieve endpoint agent
[**get_endpoint_agents**](EndpointAgentsApi.md#get_endpoint_agents) | **GET** /endpoint/agents | List endpoint agents
[**get_endpoint_agents_connection_string**](EndpointAgentsApi.md#get_endpoint_agents_connection_string) | **GET** /endpoint/agents/connection-string | Get agent connection string
[**update_endpoint_agent**](EndpointAgentsApi.md#update_endpoint_agent) | **PATCH** /endpoint/agents/{agentId} | Update endpoint agent


# **delete_endpoint_agent**
> delete_endpoint_agent(agent_id, aid=aid, expand=expand)

Delete endpoint agent

Deletes the agent with the specified `agent_id`. 

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.endpoint_agents
from thousandeyes_sdk.endpoint_agents.models.expand_endpoint_agent_options import ExpandEndpointAgentOptions
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
    api_instance = thousandeyes_sdk.endpoint_agents.EndpointAgentsApi(api_client)
    agent_id = 'agent_id_example' # str | The identifier of the agent to operate on.
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)
    expand = [thousandeyes_sdk.endpoint_agents.ExpandEndpointAgentOptions()] # List[ExpandEndpointAgentOptions] | This optional parameter allows you to control the expansion of test resources associated with the agent. By default, no expansion occurs when this query parameter is omitted. To expand the \"clients\" resource, include the query parameter `?expand=clients`.  For multiple expansions, you have two options:    * Separate the values with commas. For example, `?expandAgent=clients,tasks`. * Specify the parameter multiple times. For example, `?expandAgent=clients&expandAgent=tasks`.  This parameter offers flexibility for users to customize the expansion of specific resources related to the agent.  (optional)

    try:
        # Delete endpoint agent
        api_instance.delete_endpoint_agent(agent_id, aid=aid, expand=expand)
    except Exception as e:
        print("Exception when calling EndpointAgentsApi->delete_endpoint_agent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **str**| The identifier of the agent to operate on. | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 
 **expand** | [**List[ExpandEndpointAgentOptions]**](ExpandEndpointAgentOptions.md)| This optional parameter allows you to control the expansion of test resources associated with the agent. By default, no expansion occurs when this query parameter is omitted. To expand the \&quot;clients\&quot; resource, include the query parameter &#x60;?expand&#x3D;clients&#x60;.  For multiple expansions, you have two options:    * Separate the values with commas. For example, &#x60;?expandAgent&#x3D;clients,tasks&#x60;. * Specify the parameter multiple times. For example, &#x60;?expandAgent&#x3D;clients&amp;expandAgent&#x3D;tasks&#x60;.  This parameter offers flexibility for users to customize the expansion of specific resources related to the agent.  | [optional] 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_endpoint_agent**
> EndpointAgent disable_endpoint_agent(agent_id, aid=aid)

Disable endpoint agent

Disables an endpoint agent. If it's already disabled, it has no effect (no operation).

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.endpoint_agents
from thousandeyes_sdk.endpoint_agents.models.endpoint_agent import EndpointAgent
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
    api_instance = thousandeyes_sdk.endpoint_agents.EndpointAgentsApi(api_client)
    agent_id = 'agent_id_example' # str | The identifier of the agent to operate on.
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Disable endpoint agent
        api_response = api_instance.disable_endpoint_agent(agent_id, aid=aid)
        print("The response of EndpointAgentsApi->disable_endpoint_agent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointAgentsApi->disable_endpoint_agent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **str**| The identifier of the agent to operate on. | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

[**EndpointAgent**](EndpointAgent.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json, application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The agent&#39;s current state. |  -  |
**401** | Unauthorized |  -  |
**403** | Insufficient permissions to query endpoint |  -  |
**404** | Not found |  -  |
**429** | Exhausted rate limit for the organization |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_endpoint_agent**
> EndpointAgent enable_endpoint_agent(agent_id, aid=aid)

Enable endpoint agent

Enables an endpoint agent. If it's already enabled, it has no effect (no operation).

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.endpoint_agents
from thousandeyes_sdk.endpoint_agents.models.endpoint_agent import EndpointAgent
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
    api_instance = thousandeyes_sdk.endpoint_agents.EndpointAgentsApi(api_client)
    agent_id = 'agent_id_example' # str | The identifier of the agent to operate on.
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Enable endpoint agent
        api_response = api_instance.enable_endpoint_agent(agent_id, aid=aid)
        print("The response of EndpointAgentsApi->enable_endpoint_agent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointAgentsApi->enable_endpoint_agent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **str**| The identifier of the agent to operate on. | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

[**EndpointAgent**](EndpointAgent.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json, application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The agent&#39;s current state. |  -  |
**401** | Unauthorized |  -  |
**403** | Insufficient permissions to query endpoint |  -  |
**404** | Not found |  -  |
**429** | Exhausted rate limit for the organization |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **filter_endpoint_agents**
> FilterEndpointAgentsResponse filter_endpoint_agents(agent_search_request, max=max, cursor=cursor, aid=aid, expand=expand, include_deleted=include_deleted)

Filter endpoint agents

Retrieves a list of endpoint agents within the specified account group that match the specified filters.  If no agents meet the filter criteria, the API returns an empty array. 

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.endpoint_agents
from thousandeyes_sdk.endpoint_agents.models.agent_search_request import AgentSearchRequest
from thousandeyes_sdk.endpoint_agents.models.expand_endpoint_agent_options import ExpandEndpointAgentOptions
from thousandeyes_sdk.endpoint_agents.models.filter_endpoint_agents_response import FilterEndpointAgentsResponse
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
    api_instance = thousandeyes_sdk.endpoint_agents.EndpointAgentsApi(api_client)
    agent_search_request = thousandeyes_sdk.endpoint_agents.AgentSearchRequest() # AgentSearchRequest | The filter options for advanced search filtering for agents.
    max = 5 # int | (Optional) Maximum number of objects to return. (optional)
    cursor = 'cursor_example' # str | (Optional) Opaque cursor used for pagination. Clients should use `next` value from `_links` instead of this parameter. (optional)
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)
    expand = [thousandeyes_sdk.endpoint_agents.ExpandEndpointAgentOptions()] # List[ExpandEndpointAgentOptions] | This optional parameter allows you to control the expansion of test resources associated with the agent. By default, no expansion occurs when this query parameter is omitted. To expand the \"clients\" resource, include the query parameter `?expand=clients`.  For multiple expansions, you have two options:    * Separate the values with commas. For example, `?expandAgent=clients,tasks`. * Specify the parameter multiple times. For example, `?expandAgent=clients&expandAgent=tasks`.  This parameter offers flexibility for users to customize the expansion of specific resources related to the agent.  (optional)
    include_deleted = false # bool | When requesting entities, set to `true` if you want to see deleted entities. (optional)

    try:
        # Filter endpoint agents
        api_response = api_instance.filter_endpoint_agents(agent_search_request, max=max, cursor=cursor, aid=aid, expand=expand, include_deleted=include_deleted)
        print("The response of EndpointAgentsApi->filter_endpoint_agents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointAgentsApi->filter_endpoint_agents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_search_request** | [**AgentSearchRequest**](AgentSearchRequest.md)| The filter options for advanced search filtering for agents. | 
 **max** | **int**| (Optional) Maximum number of objects to return. | [optional] 
 **cursor** | **str**| (Optional) Opaque cursor used for pagination. Clients should use &#x60;next&#x60; value from &#x60;_links&#x60; instead of this parameter. | [optional] 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 
 **expand** | [**List[ExpandEndpointAgentOptions]**](ExpandEndpointAgentOptions.md)| This optional parameter allows you to control the expansion of test resources associated with the agent. By default, no expansion occurs when this query parameter is omitted. To expand the \&quot;clients\&quot; resource, include the query parameter &#x60;?expand&#x3D;clients&#x60;.  For multiple expansions, you have two options:    * Separate the values with commas. For example, &#x60;?expandAgent&#x3D;clients,tasks&#x60;. * Specify the parameter multiple times. For example, &#x60;?expandAgent&#x3D;clients&amp;expandAgent&#x3D;tasks&#x60;.  This parameter offers flexibility for users to customize the expansion of specific resources related to the agent.  | [optional] 
 **include_deleted** | **bool**| When requesting entities, set to &#x60;true&#x60; if you want to see deleted entities. | [optional] 

### Return type

[**FilterEndpointAgentsResponse**](FilterEndpointAgentsResponse.md)

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
**429** | Exhausted rate limit for the organization |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_endpoint_agent**
> EndpointAgent get_endpoint_agent(agent_id, aid=aid, expand=expand, include_deleted=include_deleted)

Retrieve endpoint agent

Retrieves details of an agent with the specified `agent_id`.

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.endpoint_agents
from thousandeyes_sdk.endpoint_agents.models.endpoint_agent import EndpointAgent
from thousandeyes_sdk.endpoint_agents.models.expand_endpoint_agent_options import ExpandEndpointAgentOptions
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
    api_instance = thousandeyes_sdk.endpoint_agents.EndpointAgentsApi(api_client)
    agent_id = 'agent_id_example' # str | The identifier of the agent to operate on.
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)
    expand = [thousandeyes_sdk.endpoint_agents.ExpandEndpointAgentOptions()] # List[ExpandEndpointAgentOptions] | This optional parameter allows you to control the expansion of test resources associated with the agent. By default, no expansion occurs when this query parameter is omitted. To expand the \"clients\" resource, include the query parameter `?expand=clients`.  For multiple expansions, you have two options:    * Separate the values with commas. For example, `?expandAgent=clients,tasks`. * Specify the parameter multiple times. For example, `?expandAgent=clients&expandAgent=tasks`.  This parameter offers flexibility for users to customize the expansion of specific resources related to the agent.  (optional)
    include_deleted = false # bool | When requesting entities, set to `true` if you want to see deleted entities. (optional)

    try:
        # Retrieve endpoint agent
        api_response = api_instance.get_endpoint_agent(agent_id, aid=aid, expand=expand, include_deleted=include_deleted)
        print("The response of EndpointAgentsApi->get_endpoint_agent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointAgentsApi->get_endpoint_agent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **str**| The identifier of the agent to operate on. | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 
 **expand** | [**List[ExpandEndpointAgentOptions]**](ExpandEndpointAgentOptions.md)| This optional parameter allows you to control the expansion of test resources associated with the agent. By default, no expansion occurs when this query parameter is omitted. To expand the \&quot;clients\&quot; resource, include the query parameter &#x60;?expand&#x3D;clients&#x60;.  For multiple expansions, you have two options:    * Separate the values with commas. For example, &#x60;?expandAgent&#x3D;clients,tasks&#x60;. * Specify the parameter multiple times. For example, &#x60;?expandAgent&#x3D;clients&amp;expandAgent&#x3D;tasks&#x60;.  This parameter offers flexibility for users to customize the expansion of specific resources related to the agent.  | [optional] 
 **include_deleted** | **bool**| When requesting entities, set to &#x60;true&#x60; if you want to see deleted entities. | [optional] 

### Return type

[**EndpointAgent**](EndpointAgent.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json, application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The agent&#39;s current state. |  -  |
**401** | Unauthorized |  -  |
**403** | Insufficient permissions to query endpoint |  -  |
**404** | Not found |  -  |
**429** | Exhausted rate limit for the organization |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_endpoint_agents**
> ListEndpointAgentsResponse get_endpoint_agents(max=max, cursor=cursor, aid=aid, expand=expand, include_deleted=include_deleted, use_all_permitted_aids=use_all_permitted_aids, agent_name=agent_name, computer_name=computer_name)

List endpoint agents

Retrieves a list of endpoint agents in a given account group.  If there are no agents in the specified account group, it returns an empty array. 

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.endpoint_agents
from thousandeyes_sdk.endpoint_agents.models.expand_endpoint_agent_options import ExpandEndpointAgentOptions
from thousandeyes_sdk.endpoint_agents.models.list_endpoint_agents_response import ListEndpointAgentsResponse
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
    api_instance = thousandeyes_sdk.endpoint_agents.EndpointAgentsApi(api_client)
    max = 5 # int | (Optional) Maximum number of objects to return. (optional)
    cursor = 'cursor_example' # str | (Optional) Opaque cursor used for pagination. Clients should use `next` value from `_links` instead of this parameter. (optional)
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)
    expand = [thousandeyes_sdk.endpoint_agents.ExpandEndpointAgentOptions()] # List[ExpandEndpointAgentOptions] | This optional parameter allows you to control the expansion of test resources associated with the agent. By default, no expansion occurs when this query parameter is omitted. To expand the \"clients\" resource, include the query parameter `?expand=clients`.  For multiple expansions, you have two options:    * Separate the values with commas. For example, `?expandAgent=clients,tasks`. * Specify the parameter multiple times. For example, `?expandAgent=clients&expandAgent=tasks`.  This parameter offers flexibility for users to customize the expansion of specific resources related to the agent.  (optional)
    include_deleted = false # bool | When requesting entities, set to `true` if you want to see deleted entities. (optional)
    use_all_permitted_aids = False # bool | Set to `true` to load data from all accounts the user has access to. (optional) (default to False)
    agent_name = 'agent_name_example' # str | Returns only agents with the specified name.  This is an exact match only.  (optional)
    computer_name = 'computer_name_example' # str | Returns only agents with the specified computer name. This is an exact match only.  (optional)

    try:
        # List endpoint agents
        api_response = api_instance.get_endpoint_agents(max=max, cursor=cursor, aid=aid, expand=expand, include_deleted=include_deleted, use_all_permitted_aids=use_all_permitted_aids, agent_name=agent_name, computer_name=computer_name)
        print("The response of EndpointAgentsApi->get_endpoint_agents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointAgentsApi->get_endpoint_agents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **max** | **int**| (Optional) Maximum number of objects to return. | [optional] 
 **cursor** | **str**| (Optional) Opaque cursor used for pagination. Clients should use &#x60;next&#x60; value from &#x60;_links&#x60; instead of this parameter. | [optional] 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 
 **expand** | [**List[ExpandEndpointAgentOptions]**](ExpandEndpointAgentOptions.md)| This optional parameter allows you to control the expansion of test resources associated with the agent. By default, no expansion occurs when this query parameter is omitted. To expand the \&quot;clients\&quot; resource, include the query parameter &#x60;?expand&#x3D;clients&#x60;.  For multiple expansions, you have two options:    * Separate the values with commas. For example, &#x60;?expandAgent&#x3D;clients,tasks&#x60;. * Specify the parameter multiple times. For example, &#x60;?expandAgent&#x3D;clients&amp;expandAgent&#x3D;tasks&#x60;.  This parameter offers flexibility for users to customize the expansion of specific resources related to the agent.  | [optional] 
 **include_deleted** | **bool**| When requesting entities, set to &#x60;true&#x60; if you want to see deleted entities. | [optional] 
 **use_all_permitted_aids** | **bool**| Set to &#x60;true&#x60; to load data from all accounts the user has access to. | [optional] [default to False]
 **agent_name** | **str**| Returns only agents with the specified name.  This is an exact match only.  | [optional] 
 **computer_name** | **str**| Returns only agents with the specified computer name. This is an exact match only.  | [optional] 

### Return type

[**ListEndpointAgentsResponse**](ListEndpointAgentsResponse.md)

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
**429** | Exhausted rate limit for the organization |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_endpoint_agents_connection_string**
> ConnectionString get_endpoint_agents_connection_string(aid=aid)

Get agent connection string

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.endpoint_agents
from thousandeyes_sdk.endpoint_agents.models.connection_string import ConnectionString
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
    api_instance = thousandeyes_sdk.endpoint_agents.EndpointAgentsApi(api_client)
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Get agent connection string
        api_response = api_instance.get_endpoint_agents_connection_string(aid=aid)
        print("The response of EndpointAgentsApi->get_endpoint_agents_connection_string:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointAgentsApi->get_endpoint_agents_connection_string: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

[**ConnectionString**](ConnectionString.md)

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
**429** | Exhausted rate limit for the organization |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_endpoint_agent**
> EndpointAgent update_endpoint_agent(agent_id, aid=aid, expand=expand, endpoint_agent_update=endpoint_agent_update)

Update endpoint agent

Updates the agent with the specified `agent_id`. This API supports the modification of the following fields:  * `name`  * `licenseType`  Any attempt to update fields other than those listed above, with a value different from their current value, will result in a 400 Bad Request response. 

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.endpoint_agents
from thousandeyes_sdk.endpoint_agents.models.endpoint_agent import EndpointAgent
from thousandeyes_sdk.endpoint_agents.models.endpoint_agent_update import EndpointAgentUpdate
from thousandeyes_sdk.endpoint_agents.models.expand_endpoint_agent_options import ExpandEndpointAgentOptions
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
    api_instance = thousandeyes_sdk.endpoint_agents.EndpointAgentsApi(api_client)
    agent_id = 'agent_id_example' # str | The identifier of the agent to operate on.
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)
    expand = [thousandeyes_sdk.endpoint_agents.ExpandEndpointAgentOptions()] # List[ExpandEndpointAgentOptions] | This optional parameter allows you to control the expansion of test resources associated with the agent. By default, no expansion occurs when this query parameter is omitted. To expand the \"clients\" resource, include the query parameter `?expand=clients`.  For multiple expansions, you have two options:    * Separate the values with commas. For example, `?expandAgent=clients,tasks`. * Specify the parameter multiple times. For example, `?expandAgent=clients&expandAgent=tasks`.  This parameter offers flexibility for users to customize the expansion of specific resources related to the agent.  (optional)
    endpoint_agent_update = thousandeyes_sdk.endpoint_agents.EndpointAgentUpdate() # EndpointAgentUpdate | Fields to modify on the agent (optional)

    try:
        # Update endpoint agent
        api_response = api_instance.update_endpoint_agent(agent_id, aid=aid, expand=expand, endpoint_agent_update=endpoint_agent_update)
        print("The response of EndpointAgentsApi->update_endpoint_agent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointAgentsApi->update_endpoint_agent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **str**| The identifier of the agent to operate on. | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 
 **expand** | [**List[ExpandEndpointAgentOptions]**](ExpandEndpointAgentOptions.md)| This optional parameter allows you to control the expansion of test resources associated with the agent. By default, no expansion occurs when this query parameter is omitted. To expand the \&quot;clients\&quot; resource, include the query parameter &#x60;?expand&#x3D;clients&#x60;.  For multiple expansions, you have two options:    * Separate the values with commas. For example, &#x60;?expandAgent&#x3D;clients,tasks&#x60;. * Specify the parameter multiple times. For example, &#x60;?expandAgent&#x3D;clients&amp;expandAgent&#x3D;tasks&#x60;.  This parameter offers flexibility for users to customize the expansion of specific resources related to the agent.  | [optional] 
 **endpoint_agent_update** | [**EndpointAgentUpdate**](EndpointAgentUpdate.md)| Fields to modify on the agent | [optional] 

### Return type

[**EndpointAgent**](EndpointAgent.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json, application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The agent&#39;s current state. |  -  |
**401** | Unauthorized |  -  |
**403** | Insufficient permissions to query endpoint |  -  |
**404** | Not found |  -  |
**429** | Exhausted rate limit for the organization |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

