# endpoint_agents.ManageAgentsApi

All URIs are relative to *https://api.thousandeyes.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**endpoint_agent_delete**](ManageAgentsApi.md#endpoint_agent_delete) | **DELETE** /v7/endpoint/agents/{agentId} | Delete endpoint agent
[**endpoint_agent_disable**](ManageAgentsApi.md#endpoint_agent_disable) | **POST** /v7/endpoint/agents/{agentId}/disable | Disable endpoint agent
[**endpoint_agent_enable**](ManageAgentsApi.md#endpoint_agent_enable) | **POST** /v7/endpoint/agents/{agentId}/enable | Enable endpoint agent
[**endpoint_agent_get**](ManageAgentsApi.md#endpoint_agent_get) | **GET** /v7/endpoint/agents/{agentId} | Retrieve endpoint agent
[**endpoint_agent_update**](ManageAgentsApi.md#endpoint_agent_update) | **PATCH** /v7/endpoint/agents/{agentId} | Update endpoint agent
[**endpoint_agents_list**](ManageAgentsApi.md#endpoint_agents_list) | **GET** /v7/endpoint/agents | List endpoint agents
[**endpoint_agents_search**](ManageAgentsApi.md#endpoint_agents_search) | **POST** /v7/endpoint/agents/filter | Filter endpoint agents


# **endpoint_agent_delete**
> endpoint_agent_delete(agent_id, aid=aid, expand=expand)

Delete endpoint agent

Deletes the agent with the specified `agent_id`. 

### Example

* Bearer Authentication (BearerAuth):

```python
import endpoint_agents
from endpoint_agents.models.expand import Expand
from endpoint_agents.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.thousandeyes.com
# See configuration.py for a list of all supported configuration parameters.
configuration = endpoint_agents.Configuration(
    host = "https://api.thousandeyes.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = endpoint_agents.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with endpoint_agents.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = endpoint_agents.ManageAgentsApi(api_client)
    agent_id = 'agent_id_example' # str | The identifier of the agent to operate on.
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)
    expand = [endpoint_agents.Expand()] # List[Expand] | This optional parameter allows you to control the expansion of test resources associated with the agent. By default, no expansion occurs when this query parameter is omitted. To expand the \"clients\" resource, include the query parameter `?expand=clients`.  For multiple expansions, you have two options:    * Separate the values with commas. For example, `?expandAgent=clients,tasks`. * Specify the parameter multiple times. For example, `?expandAgent=clients&expandAgent=tasks`.  This parameter offers flexibility for users to customize the expansion of specific resources related to the agent.  (optional)

    try:
        # Delete endpoint agent
        api_instance.endpoint_agent_delete(agent_id, aid=aid, expand=expand)
    except Exception as e:
        print("Exception when calling ManageAgentsApi->endpoint_agent_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **str**| The identifier of the agent to operate on. | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 
 **expand** | [**List[Expand]**](Expand.md)| This optional parameter allows you to control the expansion of test resources associated with the agent. By default, no expansion occurs when this query parameter is omitted. To expand the \&quot;clients\&quot; resource, include the query parameter &#x60;?expand&#x3D;clients&#x60;.  For multiple expansions, you have two options:    * Separate the values with commas. For example, &#x60;?expandAgent&#x3D;clients,tasks&#x60;. * Specify the parameter multiple times. For example, &#x60;?expandAgent&#x3D;clients&amp;expandAgent&#x3D;tasks&#x60;.  This parameter offers flexibility for users to customize the expansion of specific resources related to the agent.  | [optional] 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No content |  -  |
**401** | Unauthorized |  -  |
**403** | Insufficient permissions to query endpoint |  -  |
**404** | Not found |  -  |
**429** | Exhausted rate limit for the organization |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoint_agent_disable**
> EndpointAgentGet200Response endpoint_agent_disable(agent_id, aid=aid)

Disable endpoint agent

Disables an endpoint agent. If it's already disabled, it has no effect (no operation).

### Example

* Bearer Authentication (BearerAuth):

```python
import endpoint_agents
from endpoint_agents.models.endpoint_agent_get200_response import EndpointAgentGet200Response
from endpoint_agents.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.thousandeyes.com
# See configuration.py for a list of all supported configuration parameters.
configuration = endpoint_agents.Configuration(
    host = "https://api.thousandeyes.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = endpoint_agents.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with endpoint_agents.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = endpoint_agents.ManageAgentsApi(api_client)
    agent_id = 'agent_id_example' # str | The identifier of the agent to operate on.
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Disable endpoint agent
        api_response = api_instance.endpoint_agent_disable(agent_id, aid=aid)
        print("The response of ManageAgentsApi->endpoint_agent_disable:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManageAgentsApi->endpoint_agent_disable: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **str**| The identifier of the agent to operate on. | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

[**EndpointAgentGet200Response**](EndpointAgentGet200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The agent&#39;s current state. |  -  |
**401** | Unauthorized |  -  |
**403** | Insufficient permissions to query endpoint |  -  |
**404** | Not found |  -  |
**429** | Exhausted rate limit for the organization |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoint_agent_enable**
> EndpointAgentGet200Response endpoint_agent_enable(agent_id, aid=aid)

Enable endpoint agent

Enables an endpoint agent. If it's already enabled, it has no effect (no operation).

### Example

* Bearer Authentication (BearerAuth):

```python
import endpoint_agents
from endpoint_agents.models.endpoint_agent_get200_response import EndpointAgentGet200Response
from endpoint_agents.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.thousandeyes.com
# See configuration.py for a list of all supported configuration parameters.
configuration = endpoint_agents.Configuration(
    host = "https://api.thousandeyes.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = endpoint_agents.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with endpoint_agents.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = endpoint_agents.ManageAgentsApi(api_client)
    agent_id = 'agent_id_example' # str | The identifier of the agent to operate on.
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Enable endpoint agent
        api_response = api_instance.endpoint_agent_enable(agent_id, aid=aid)
        print("The response of ManageAgentsApi->endpoint_agent_enable:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManageAgentsApi->endpoint_agent_enable: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **str**| The identifier of the agent to operate on. | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

[**EndpointAgentGet200Response**](EndpointAgentGet200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The agent&#39;s current state. |  -  |
**401** | Unauthorized |  -  |
**403** | Insufficient permissions to query endpoint |  -  |
**404** | Not found |  -  |
**429** | Exhausted rate limit for the organization |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoint_agent_get**
> EndpointAgentGet200Response endpoint_agent_get(agent_id, aid=aid, expand=expand, include_deleted=include_deleted)

Retrieve endpoint agent

Retrieves details of an agent with the specified `agent_id`.

### Example

* Bearer Authentication (BearerAuth):

```python
import endpoint_agents
from endpoint_agents.models.endpoint_agent_get200_response import EndpointAgentGet200Response
from endpoint_agents.models.expand import Expand
from endpoint_agents.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.thousandeyes.com
# See configuration.py for a list of all supported configuration parameters.
configuration = endpoint_agents.Configuration(
    host = "https://api.thousandeyes.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = endpoint_agents.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with endpoint_agents.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = endpoint_agents.ManageAgentsApi(api_client)
    agent_id = 'agent_id_example' # str | The identifier of the agent to operate on.
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)
    expand = [endpoint_agents.Expand()] # List[Expand] | This optional parameter allows you to control the expansion of test resources associated with the agent. By default, no expansion occurs when this query parameter is omitted. To expand the \"clients\" resource, include the query parameter `?expand=clients`.  For multiple expansions, you have two options:    * Separate the values with commas. For example, `?expandAgent=clients,tasks`. * Specify the parameter multiple times. For example, `?expandAgent=clients&expandAgent=tasks`.  This parameter offers flexibility for users to customize the expansion of specific resources related to the agent.  (optional)
    include_deleted = false # bool | When requesting entities, set to `true` if you want to see deleted entities. (optional)

    try:
        # Retrieve endpoint agent
        api_response = api_instance.endpoint_agent_get(agent_id, aid=aid, expand=expand, include_deleted=include_deleted)
        print("The response of ManageAgentsApi->endpoint_agent_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManageAgentsApi->endpoint_agent_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **str**| The identifier of the agent to operate on. | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 
 **expand** | [**List[Expand]**](Expand.md)| This optional parameter allows you to control the expansion of test resources associated with the agent. By default, no expansion occurs when this query parameter is omitted. To expand the \&quot;clients\&quot; resource, include the query parameter &#x60;?expand&#x3D;clients&#x60;.  For multiple expansions, you have two options:    * Separate the values with commas. For example, &#x60;?expandAgent&#x3D;clients,tasks&#x60;. * Specify the parameter multiple times. For example, &#x60;?expandAgent&#x3D;clients&amp;expandAgent&#x3D;tasks&#x60;.  This parameter offers flexibility for users to customize the expansion of specific resources related to the agent.  | [optional] 
 **include_deleted** | **bool**| When requesting entities, set to &#x60;true&#x60; if you want to see deleted entities. | [optional] 

### Return type

[**EndpointAgentGet200Response**](EndpointAgentGet200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The agent&#39;s current state. |  -  |
**401** | Unauthorized |  -  |
**403** | Insufficient permissions to query endpoint |  -  |
**404** | Not found |  -  |
**429** | Exhausted rate limit for the organization |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoint_agent_update**
> EndpointAgentGet200Response endpoint_agent_update(agent_id, aid=aid, expand=expand, endpoint_agent_update=endpoint_agent_update)

Update endpoint agent

Updates the agent with the specified `agent_id`. This API supports the modification of the following fields:  * `name`  * `licenseType`  Any attempt to update fields other than those listed above, with a value different from their current value, will result in a 400 Bad Request response. 

### Example

* Bearer Authentication (BearerAuth):

```python
import endpoint_agents
from endpoint_agents.models.endpoint_agent_get200_response import EndpointAgentGet200Response
from endpoint_agents.models.endpoint_agent_update import EndpointAgentUpdate
from endpoint_agents.models.expand import Expand
from endpoint_agents.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.thousandeyes.com
# See configuration.py for a list of all supported configuration parameters.
configuration = endpoint_agents.Configuration(
    host = "https://api.thousandeyes.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = endpoint_agents.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with endpoint_agents.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = endpoint_agents.ManageAgentsApi(api_client)
    agent_id = 'agent_id_example' # str | The identifier of the agent to operate on.
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)
    expand = [endpoint_agents.Expand()] # List[Expand] | This optional parameter allows you to control the expansion of test resources associated with the agent. By default, no expansion occurs when this query parameter is omitted. To expand the \"clients\" resource, include the query parameter `?expand=clients`.  For multiple expansions, you have two options:    * Separate the values with commas. For example, `?expandAgent=clients,tasks`. * Specify the parameter multiple times. For example, `?expandAgent=clients&expandAgent=tasks`.  This parameter offers flexibility for users to customize the expansion of specific resources related to the agent.  (optional)
    endpoint_agent_update = endpoint_agents.EndpointAgentUpdate() # EndpointAgentUpdate | Fields to modify on the agent (optional)

    try:
        # Update endpoint agent
        api_response = api_instance.endpoint_agent_update(agent_id, aid=aid, expand=expand, endpoint_agent_update=endpoint_agent_update)
        print("The response of ManageAgentsApi->endpoint_agent_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManageAgentsApi->endpoint_agent_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **str**| The identifier of the agent to operate on. | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 
 **expand** | [**List[Expand]**](Expand.md)| This optional parameter allows you to control the expansion of test resources associated with the agent. By default, no expansion occurs when this query parameter is omitted. To expand the \&quot;clients\&quot; resource, include the query parameter &#x60;?expand&#x3D;clients&#x60;.  For multiple expansions, you have two options:    * Separate the values with commas. For example, &#x60;?expandAgent&#x3D;clients,tasks&#x60;. * Specify the parameter multiple times. For example, &#x60;?expandAgent&#x3D;clients&amp;expandAgent&#x3D;tasks&#x60;.  This parameter offers flexibility for users to customize the expansion of specific resources related to the agent.  | [optional] 
 **endpoint_agent_update** | [**EndpointAgentUpdate**](EndpointAgentUpdate.md)| Fields to modify on the agent | [optional] 

### Return type

[**EndpointAgentGet200Response**](EndpointAgentGet200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The agent&#39;s current state. |  -  |
**401** | Unauthorized |  -  |
**403** | Insufficient permissions to query endpoint |  -  |
**404** | Not found |  -  |
**429** | Exhausted rate limit for the organization |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoint_agents_list**
> EndpointAgentsList200Response endpoint_agents_list(max=max, cursor=cursor, aid=aid, expand=expand, include_deleted=include_deleted, use_all_permitted_aids=use_all_permitted_aids, agent_name=agent_name, computer_name=computer_name)

List endpoint agents

Retrieves a list of endpoint agents in a given account group.  If there are no agents in the specified account group, it returns an empty array. 

### Example

* Bearer Authentication (BearerAuth):

```python
import endpoint_agents
from endpoint_agents.models.endpoint_agents_list200_response import EndpointAgentsList200Response
from endpoint_agents.models.expand import Expand
from endpoint_agents.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.thousandeyes.com
# See configuration.py for a list of all supported configuration parameters.
configuration = endpoint_agents.Configuration(
    host = "https://api.thousandeyes.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = endpoint_agents.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with endpoint_agents.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = endpoint_agents.ManageAgentsApi(api_client)
    max = 5 # float | (Optional) Maximum number of objects to return. (optional)
    cursor = 'cursor_example' # str | (Optional) Opaque cursor used for pagination. Clients should use `next` value from `_links` instead of this parameter. (optional)
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)
    expand = [endpoint_agents.Expand()] # List[Expand] | This optional parameter allows you to control the expansion of test resources associated with the agent. By default, no expansion occurs when this query parameter is omitted. To expand the \"clients\" resource, include the query parameter `?expand=clients`.  For multiple expansions, you have two options:    * Separate the values with commas. For example, `?expandAgent=clients,tasks`. * Specify the parameter multiple times. For example, `?expandAgent=clients&expandAgent=tasks`.  This parameter offers flexibility for users to customize the expansion of specific resources related to the agent.  (optional)
    include_deleted = false # bool | When requesting entities, set to `true` if you want to see deleted entities. (optional)
    use_all_permitted_aids = False # bool | Set to `true` to load data from all accounts the user has access to. (optional) (default to False)
    agent_name = 'agent_name_example' # str | Returns only agents with the specified name.  This is an exact match only.  (optional)
    computer_name = 'computer_name_example' # str | Returns only agents with the specified computer name. This is an exact match only.  (optional)

    try:
        # List endpoint agents
        api_response = api_instance.endpoint_agents_list(max=max, cursor=cursor, aid=aid, expand=expand, include_deleted=include_deleted, use_all_permitted_aids=use_all_permitted_aids, agent_name=agent_name, computer_name=computer_name)
        print("The response of ManageAgentsApi->endpoint_agents_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManageAgentsApi->endpoint_agents_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **max** | **float**| (Optional) Maximum number of objects to return. | [optional] 
 **cursor** | **str**| (Optional) Opaque cursor used for pagination. Clients should use &#x60;next&#x60; value from &#x60;_links&#x60; instead of this parameter. | [optional] 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 
 **expand** | [**List[Expand]**](Expand.md)| This optional parameter allows you to control the expansion of test resources associated with the agent. By default, no expansion occurs when this query parameter is omitted. To expand the \&quot;clients\&quot; resource, include the query parameter &#x60;?expand&#x3D;clients&#x60;.  For multiple expansions, you have two options:    * Separate the values with commas. For example, &#x60;?expandAgent&#x3D;clients,tasks&#x60;. * Specify the parameter multiple times. For example, &#x60;?expandAgent&#x3D;clients&amp;expandAgent&#x3D;tasks&#x60;.  This parameter offers flexibility for users to customize the expansion of specific resources related to the agent.  | [optional] 
 **include_deleted** | **bool**| When requesting entities, set to &#x60;true&#x60; if you want to see deleted entities. | [optional] 
 **use_all_permitted_aids** | **bool**| Set to &#x60;true&#x60; to load data from all accounts the user has access to. | [optional] [default to False]
 **agent_name** | **str**| Returns only agents with the specified name.  This is an exact match only.  | [optional] 
 **computer_name** | **str**| Returns only agents with the specified computer name. This is an exact match only.  | [optional] 

### Return type

[**EndpointAgentsList200Response**](EndpointAgentsList200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Insufficient permissions to query endpoint |  -  |
**429** | Exhausted rate limit for the organization |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoint_agents_search**
> EndpointAgentsSearch200Response endpoint_agents_search(agent_search_request, max=max, cursor=cursor, aid=aid, expand=expand, include_deleted=include_deleted)

Filter endpoint agents

Retrieves a list of endpoint agents within the specified account group that match the specified filters.  If no agents meet the filter criteria, the API returns an empty array. 

### Example

* Bearer Authentication (BearerAuth):

```python
import endpoint_agents
from endpoint_agents.models.agent_search_request import AgentSearchRequest
from endpoint_agents.models.endpoint_agents_search200_response import EndpointAgentsSearch200Response
from endpoint_agents.models.expand import Expand
from endpoint_agents.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.thousandeyes.com
# See configuration.py for a list of all supported configuration parameters.
configuration = endpoint_agents.Configuration(
    host = "https://api.thousandeyes.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = endpoint_agents.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with endpoint_agents.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = endpoint_agents.ManageAgentsApi(api_client)
    agent_search_request = endpoint_agents.AgentSearchRequest() # AgentSearchRequest | The filter options for advanced search filtering for agents.
    max = 5 # float | (Optional) Maximum number of objects to return. (optional)
    cursor = 'cursor_example' # str | (Optional) Opaque cursor used for pagination. Clients should use `next` value from `_links` instead of this parameter. (optional)
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)
    expand = [endpoint_agents.Expand()] # List[Expand] | This optional parameter allows you to control the expansion of test resources associated with the agent. By default, no expansion occurs when this query parameter is omitted. To expand the \"clients\" resource, include the query parameter `?expand=clients`.  For multiple expansions, you have two options:    * Separate the values with commas. For example, `?expandAgent=clients,tasks`. * Specify the parameter multiple times. For example, `?expandAgent=clients&expandAgent=tasks`.  This parameter offers flexibility for users to customize the expansion of specific resources related to the agent.  (optional)
    include_deleted = false # bool | When requesting entities, set to `true` if you want to see deleted entities. (optional)

    try:
        # Filter endpoint agents
        api_response = api_instance.endpoint_agents_search(agent_search_request, max=max, cursor=cursor, aid=aid, expand=expand, include_deleted=include_deleted)
        print("The response of ManageAgentsApi->endpoint_agents_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManageAgentsApi->endpoint_agents_search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_search_request** | [**AgentSearchRequest**](AgentSearchRequest.md)| The filter options for advanced search filtering for agents. | 
 **max** | **float**| (Optional) Maximum number of objects to return. | [optional] 
 **cursor** | **str**| (Optional) Opaque cursor used for pagination. Clients should use &#x60;next&#x60; value from &#x60;_links&#x60; instead of this parameter. | [optional] 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 
 **expand** | [**List[Expand]**](Expand.md)| This optional parameter allows you to control the expansion of test resources associated with the agent. By default, no expansion occurs when this query parameter is omitted. To expand the \&quot;clients\&quot; resource, include the query parameter &#x60;?expand&#x3D;clients&#x60;.  For multiple expansions, you have two options:    * Separate the values with commas. For example, &#x60;?expandAgent&#x3D;clients,tasks&#x60;. * Specify the parameter multiple times. For example, &#x60;?expandAgent&#x3D;clients&amp;expandAgent&#x3D;tasks&#x60;.  This parameter offers flexibility for users to customize the expansion of specific resources related to the agent.  | [optional] 
 **include_deleted** | **bool**| When requesting entities, set to &#x60;true&#x60; if you want to see deleted entities. | [optional] 

### Return type

[**EndpointAgentsSearch200Response**](EndpointAgentsSearch200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Insufficient permissions to query endpoint |  -  |
**429** | Exhausted rate limit for the organization |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

