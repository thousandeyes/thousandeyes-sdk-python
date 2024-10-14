# thousandeyes_sdk.agents.EnterpriseAgentClusterApi

All URIs are relative to *https://api.thousandeyes.com/v7*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assign_agent_to_cluster**](EnterpriseAgentClusterApi.md#assign_agent_to_cluster) | **POST** /agents/{agentId}/cluster/assign | Add member to Enterprise Agent cluster
[**unassign_agent_from_cluster**](EnterpriseAgentClusterApi.md#unassign_agent_from_cluster) | **POST** /agents/{agentId}/cluster/unassign | Remove member from Enterprise Agent cluster


# **assign_agent_to_cluster**
> AgentDetails assign_agent_to_cluster(agent_id, agent_cluster_assign_request, aid=aid, expand=expand)

Add member to Enterprise Agent cluster

Adding a member to an Enterprise Agent cluster converts a standalone Enterprise Agent to an Enterprise Agent cluster. If the agent represented by the path {agentId} is not already a cluster, it will be converted to a cluster.  The response will be a single Enterprise Agent Cluster. The converted Enterprise Agents will become cluster members, and can be returned using the `?expand=cluster-member` parameter.  This operation requires users to have the `Edit agents in account group` permission.  Upon successful cluster creation, the response includes:  * Information about the new cluster in the response body.  * Each cluster member receives a unique `memberId` within the cluster.  * The `memberId` value is not linked to the original `agentId` used in the request URL or POST body.  * The cluster name is based on the agent whose `agentId` is present in the request URL.  **Example - converting a single agent** ``` curl -X POST https://api.thousandeyes.com/v7/agents/64965/cluster/assign  -H \"Authorization: Bearer $Bearer_token\"  ````  **Example - converting multiple agents** ``` curl https://api.thousandeyes.com/v7/agents/64965/cluster/assign \\ '{\"agents\":[   \"2277\",   \"1234\" ]}' \\ -H \"content-type:application/json\" \\ -H \"Authorization: Bearer $Bearer_token\"  ````

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.agents
from thousandeyes_sdk.agents.models.agent_cluster_assign_request import AgentClusterAssignRequest
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
    api_instance = thousandeyes_sdk.agents.EnterpriseAgentClusterApi(api_client)
    agent_id = '281474976710706' # str | Unique ID for the Enterprise Agent cluster to add new agents to.
    agent_cluster_assign_request = thousandeyes_sdk.agents.AgentClusterAssignRequest() # AgentClusterAssignRequest | 
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)
    expand = [thousandeyes_sdk.agents.AgentDetailsExpand()] # List[AgentDetailsExpand] | Optional parameter, off by default. Indicates which agent sub-resource to expand. For example, if you wish to expand the `clusterMembers` sub-resource, pass the `?expand=cluster-member` query. (optional)

    try:
        # Add member to Enterprise Agent cluster
        api_response = api_instance.assign_agent_to_cluster(agent_id, agent_cluster_assign_request, aid=aid, expand=expand)
        print("The response of EnterpriseAgentClusterApi->assign_agent_to_cluster:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnterpriseAgentClusterApi->assign_agent_to_cluster: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **str**| Unique ID for the Enterprise Agent cluster to add new agents to. | 
 **agent_cluster_assign_request** | [**AgentClusterAssignRequest**](AgentClusterAssignRequest.md)|  | 
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

# **unassign_agent_from_cluster**
> CloudEnterpriseAgents unassign_agent_from_cluster(agent_id, agent_cluster_unassign_request, aid=aid, expand=expand)

Remove member from Enterprise Agent cluster

Converts a cluster with a single or multiple Enterprise Agent members back to a standalone Enterprise Agent(s). This operation can also be used to remove one or more members from an Enterprise Agent cluster. Removed members revert to being standalone Enterprise Agents. If all members are removed from the cluster, the Enterprise Agent Cluster is deleted.  The response is an list of agents, containing both the Enterprise Agent Cluster (if it still exists), and the removed members, now as standalone Enterprise Agents. This operation is exclusive to Enterprise Agent clusters and can be accessed only by users with the `Edit agents in account group` permission.  On successful completion, the response contains the following information:  * The updated cluster information is provided in the response body, unless all members are removed from the cluster.  * Information about each removed member, now a standalone agent.  * When a non-last member is removed from the cluster, it receives a new `agentId` value. This new `agentId` is different from the `agentId` the agent had before joining the cluster, and it is also unrelated to the `memberId` value the agent had while being a part of the cluster.  * If all members are removed from the cluster, the cluster itself is converted back to a standalone Enterprise Agent too. Such standalone agent inherits the old cluster’s `agentId` value. The last `memberId` listed in the POST body inherits the cluster’s `agentId` value.  **Example - removing a single member** ``` curl -X POST https://api.thousandeyes.com/v7/agents/64965/cluster/unassign   \\ '{\"members\":[\"55974\"]}' \\ -H \"content-type:application/json\" \\ -H \"Authorization: Bearer $Bearer_token\"  ```  **Example - removing multiple members** ``` curl https://api.thousandeyes.com/v7/agents/64965/cluster/unassign \\ '{\"members\":[     \"55974\",     \"12313\"]  }' \\ -H \"content-type:application/json\" \\ -H \"Authorization: Bearer $Bearer_token\"  ```

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.agents
from thousandeyes_sdk.agents.models.agent_cluster_unassign_request import AgentClusterUnassignRequest
from thousandeyes_sdk.agents.models.agent_details_expand import AgentDetailsExpand
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
    api_instance = thousandeyes_sdk.agents.EnterpriseAgentClusterApi(api_client)
    agent_id = '281474976710706' # str | Unique ID for the Enterprise Agent cluster to remove agents from.
    agent_cluster_unassign_request = thousandeyes_sdk.agents.AgentClusterUnassignRequest() # AgentClusterUnassignRequest | 
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)
    expand = [thousandeyes_sdk.agents.AgentDetailsExpand()] # List[AgentDetailsExpand] | Optional parameter, off by default. Indicates which agent sub-resource to expand. For example, if you wish to expand the `clusterMembers` sub-resource, pass the `?expand=cluster-member` query. (optional)

    try:
        # Remove member from Enterprise Agent cluster
        api_response = api_instance.unassign_agent_from_cluster(agent_id, agent_cluster_unassign_request, aid=aid, expand=expand)
        print("The response of EnterpriseAgentClusterApi->unassign_agent_from_cluster:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnterpriseAgentClusterApi->unassign_agent_from_cluster: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **str**| Unique ID for the Enterprise Agent cluster to remove agents from. | 
 **agent_cluster_unassign_request** | [**AgentClusterUnassignRequest**](AgentClusterUnassignRequest.md)|  | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 
 **expand** | [**List[AgentDetailsExpand]**](AgentDetailsExpand.md)| Optional parameter, off by default. Indicates which agent sub-resource to expand. For example, if you wish to expand the &#x60;clusterMembers&#x60; sub-resource, pass the &#x60;?expand&#x3D;cluster-member&#x60; query. | [optional] 

### Return type

[**CloudEnterpriseAgents**](CloudEnterpriseAgents.md)

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

