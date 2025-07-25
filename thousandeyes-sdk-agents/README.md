# thousandeyes-sdk-agents

## Overview
Manage Cloud and Enterprise Agents available to your account in ThousandEyes.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 7.0.54
- Generator version: 7.6.0
- Build package: com.thousandeyes.api.codegen.ThousandeyesPythonGenerator

## Requirements.

Python 3.8+

## Installation & Usage
### pip install

Install directly via PyPi:

```sh
pip install thousandeyes-sdk-agents
```
(you may need to run `pip` with root permission: `sudo pip install thousandeyes-sdk-agents`)

Then import the package:
```python
import thousandeyes_sdk.agents
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import thousandeyes_sdk.agents
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the installation procedure and then run the following:

```python

import thousandeyes_sdk.core
import thousandeyes_sdk.agents
from thousandeyes_sdk.core.exceptions import ApiException
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
    api_instance = thousandeyes_sdk.agents.AgentProxiesApi(api_client)
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # List Enterprise Agent Proxies
        api_response = api_instance.get_agents_proxies(aid=aid)
        print("The response of AgentProxiesApi->get_agents_proxies:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AgentProxiesApi->get_agents_proxies: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.thousandeyes.com/v7*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AgentProxiesApi* | [**get_agents_proxies**](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-agents/docs/AgentProxiesApi.md#get_agents_proxies) | **GET** /agents/proxies | List Enterprise Agent Proxies
*CloudAndEnterpriseAgentNotificationRulesApi* | [**get_agents_notification_rule**](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-agents/docs/CloudAndEnterpriseAgentNotificationRulesApi.md#get_agents_notification_rule) | **GET** /agents/notification-rules/{notificationRuleId} | Retrieve agent notification rule
*CloudAndEnterpriseAgentNotificationRulesApi* | [**get_agents_notification_rules**](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-agents/docs/CloudAndEnterpriseAgentNotificationRulesApi.md#get_agents_notification_rules) | **GET** /agents/notification-rules | List agent notification rules
*CloudAndEnterpriseAgentsApi* | [**delete_agent**](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-agents/docs/CloudAndEnterpriseAgentsApi.md#delete_agent) | **DELETE** /agents/{agentId} | Delete Enterprise Agent
*CloudAndEnterpriseAgentsApi* | [**get_agent**](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-agents/docs/CloudAndEnterpriseAgentsApi.md#get_agent) | **GET** /agents/{agentId} | Retrieve Cloud and Enterprise Agent
*CloudAndEnterpriseAgentsApi* | [**get_agents**](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-agents/docs/CloudAndEnterpriseAgentsApi.md#get_agents) | **GET** /agents | List Cloud and Enterprise Agents
*CloudAndEnterpriseAgentsApi* | [**update_agent**](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-agents/docs/CloudAndEnterpriseAgentsApi.md#update_agent) | **PUT** /agents/{agentId} | Update Enterprise Agent
*EnterpriseAgentClusterApi* | [**assign_agent_to_cluster**](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-agents/docs/EnterpriseAgentClusterApi.md#assign_agent_to_cluster) | **POST** /agents/{agentId}/cluster/assign | Add member to Enterprise Agent cluster
*EnterpriseAgentClusterApi* | [**unassign_agent_from_cluster**](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-agents/docs/EnterpriseAgentClusterApi.md#unassign_agent_from_cluster) | **POST** /agents/{agentId}/cluster/unassign | Remove member from Enterprise Agent cluster
*TestsAssignmentOnAgentsApi* | [**assign_tests**](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-agents/docs/TestsAssignmentOnAgentsApi.md#assign_tests) | **POST** /agents/{agentId}/tests/assign | Assign tests to an agent
*TestsAssignmentOnAgentsApi* | [**overwrite_tests**](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-agents/docs/TestsAssignmentOnAgentsApi.md#overwrite_tests) | **POST** /agents/{agentId}/tests/override | Overwrite tests assigned to an agent
*TestsAssignmentOnAgentsApi* | [**unassign_tests**](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-agents/docs/TestsAssignmentOnAgentsApi.md#unassign_tests) | **POST** /agents/{agentId}/tests/unassign | Unassign tests from an agent


## Documentation For Models

 - [AccountGroup](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-agents/docs/AccountGroup.md)
 - [AgentBase](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-agents/docs/AgentBase.md)
 - [AgentClusterAssignRequest](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-agents/docs/AgentClusterAssignRequest.md)
 - [AgentClusterUnassignRequest](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-agents/docs/AgentClusterUnassignRequest.md)
 - [AgentDetails](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-agents/docs/AgentDetails.md)
 - [AgentDetailsExpand](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-agents/docs/AgentDetailsExpand.md)
 - [AgentIpv6Policy](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-agents/docs/AgentIpv6Policy.md)
 - [AgentLabel](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-agents/docs/AgentLabel.md)
 - [AgentListExpand](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-agents/docs/AgentListExpand.md)
 - [AgentNotification](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-agents/docs/AgentNotification.md)
 - [AgentProxies](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-agents/docs/AgentProxies.md)
 - [AgentProxy](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-agents/docs/AgentProxy.md)
 - [AgentRequest](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-agents/docs/AgentRequest.md)
 - [AgentResponse](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-agents/docs/AgentResponse.md)
 - [AgentTestsAssignRequest](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-agents/docs/AgentTestsAssignRequest.md)
 - [AlertEmail](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-agents/docs/AlertEmail.md)
 - [AlertIntegrationBase](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-agents/docs/AlertIntegrationBase.md)
 - [AlertIntegrationType](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-agents/docs/AlertIntegrationType.md)
 - [CloudAgentDetail](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-agents/docs/CloudAgentDetail.md)
 - [CloudEnterpriseAgent](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-agents/docs/CloudEnterpriseAgent.md)
 - [CloudEnterpriseAgentType](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-agents/docs/CloudEnterpriseAgentType.md)
 - [CloudEnterpriseAgents](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-agents/docs/CloudEnterpriseAgents.md)
 - [ClusterMember](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-agents/docs/ClusterMember.md)
 - [EnterpriseAgent](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-agents/docs/EnterpriseAgent.md)
 - [EnterpriseAgentClusterDetail](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-agents/docs/EnterpriseAgentClusterDetail.md)
 - [EnterpriseAgentData](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-agents/docs/EnterpriseAgentData.md)
 - [EnterpriseAgentDetail](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-agents/docs/EnterpriseAgentDetail.md)
 - [EnterpriseAgentIpv6Policy](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-agents/docs/EnterpriseAgentIpv6Policy.md)
 - [EnterpriseAgentResponseExpands](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-agents/docs/EnterpriseAgentResponseExpands.md)
 - [EnterpriseAgentState](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-agents/docs/EnterpriseAgentState.md)
 - [Error](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-agents/docs/Error.md)
 - [ErrorDetail](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-agents/docs/ErrorDetail.md)
 - [ErrorDetailCode](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-agents/docs/ErrorDetailCode.md)
 - [InterfaceIpMapping](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-agents/docs/InterfaceIpMapping.md)
 - [Link](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-agents/docs/Link.md)
 - [ListNotificationRulesResponse](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-agents/docs/ListNotificationRulesResponse.md)
 - [NotificationRule](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-agents/docs/NotificationRule.md)
 - [NotificationRuleDetail](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-agents/docs/NotificationRuleDetail.md)
 - [NotificationRules](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-agents/docs/NotificationRules.md)
 - [ProxyAuthType](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-agents/docs/ProxyAuthType.md)
 - [ProxyType](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-agents/docs/ProxyType.md)
 - [SelfLinks](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-agents/docs/SelfLinks.md)
 - [SimpleAgent](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-agents/docs/SimpleAgent.md)
 - [SimpleEnterpriseAgent](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-agents/docs/SimpleEnterpriseAgent.md)
 - [SimpleTest](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-agents/docs/SimpleTest.md)
 - [TestInterval](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-agents/docs/TestInterval.md)
 - [TestLinks](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-agents/docs/TestLinks.md)
 - [TestSelfLink](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-agents/docs/TestSelfLink.md)
 - [TestType](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-agents/docs/TestType.md)
 - [UnauthorizedError](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-agents/docs/UnauthorizedError.md)
 - [ValidationError](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-agents/docs/ValidationError.md)
 - [ValidationErrorItem](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-agents/docs/ValidationErrorItem.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="BearerAuth"></a>
### BearerAuth

- **Type**: Bearer authentication


## Author

<a href="mailto:api-team@thousandeyes.com">ThousandEyes API Team </a>


