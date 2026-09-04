# thousandeyes_sdk.cloud_insights_integrations.CloudInsightsIntegrationsApi

All URIs are relative to *https://api.thousandeyes.com/v7*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_aws_flow_logs_monitoring_integration**](CloudInsightsIntegrationsApi.md#create_aws_flow_logs_monitoring_integration) | **POST** /cloud-insights/integration/aws/flow-logs | Create AWS flow logs monitoring integration
[**create_aws_inventory_monitoring_integration**](CloudInsightsIntegrationsApi.md#create_aws_inventory_monitoring_integration) | **POST** /cloud-insights/integration/aws/inventory | Create AWS inventory monitoring integration
[**create_azure_flow_logs_monitoring_integration**](CloudInsightsIntegrationsApi.md#create_azure_flow_logs_monitoring_integration) | **POST** /cloud-insights/integration/azure/flow-logs | Create Azure flow logs monitoring integration
[**create_azure_inventory_monitoring_integration**](CloudInsightsIntegrationsApi.md#create_azure_inventory_monitoring_integration) | **POST** /cloud-insights/integration/azure/inventory | Create Azure inventory monitoring integration
[**delete_aws_monitoring_integration**](CloudInsightsIntegrationsApi.md#delete_aws_monitoring_integration) | **DELETE** /cloud-insights/integration/aws/{integrationId} | Delete AWS integration
[**delete_azure_monitoring_integration**](CloudInsightsIntegrationsApi.md#delete_azure_monitoring_integration) | **DELETE** /cloud-insights/integration/azure/{integrationId} | Delete Azure integration
[**get_all_aws_monitoring_integrations**](CloudInsightsIntegrationsApi.md#get_all_aws_monitoring_integrations) | **GET** /cloud-insights/integration/aws | List AWS integrations
[**get_all_azure_monitoring_integrations**](CloudInsightsIntegrationsApi.md#get_all_azure_monitoring_integrations) | **GET** /cloud-insights/integration/azure | List Azure integrations
[**get_aws_flowlogs_monitoring_integration_policies**](CloudInsightsIntegrationsApi.md#get_aws_flowlogs_monitoring_integration_policies) | **GET** /cloud-insights/integration/aws/flow-logs/policies | Get AWS flow logs monitoring IAM policies
[**get_aws_inventory_monitoring_integration_policies**](CloudInsightsIntegrationsApi.md#get_aws_inventory_monitoring_integration_policies) | **GET** /cloud-insights/integration/aws/inventory/policies | Get AWS inventory monitoring IAM policies
[**get_aws_monitoring_integration**](CloudInsightsIntegrationsApi.md#get_aws_monitoring_integration) | **GET** /cloud-insights/integration/aws/{integrationId} | Get AWS integration
[**get_azure_monitoring_integration**](CloudInsightsIntegrationsApi.md#get_azure_monitoring_integration) | **GET** /cloud-insights/integration/azure/{integrationId} | Get Azure integration
[**update_azure_flow_logs_monitoring_integration**](CloudInsightsIntegrationsApi.md#update_azure_flow_logs_monitoring_integration) | **PUT** /cloud-insights/integration/azure/flow-logs/{integrationId} | Update Azure flow logs monitoring integration
[**update_azure_inventory_monitoring_integration**](CloudInsightsIntegrationsApi.md#update_azure_inventory_monitoring_integration) | **PUT** /cloud-insights/integration/azure/inventory/{integrationId} | Update Azure inventory monitoring integration


# **create_aws_flow_logs_monitoring_integration**
> AwsMonitoringIntegration create_aws_flow_logs_monitoring_integration(aws_flow_logs_integration_request, aid=aid)

Create AWS flow logs monitoring integration

Creates a new AWS flow logs monitoring integration.

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.cloud_insights_integrations
from thousandeyes_sdk.cloud_insights_integrations.models.aws_flow_logs_integration_request import AwsFlowLogsIntegrationRequest
from thousandeyes_sdk.cloud_insights_integrations.models.aws_monitoring_integration import AwsMonitoringIntegration
from thousandeyes_sdk.cloud_insights_integrations.rest import ApiException
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
    api_instance = thousandeyes_sdk.cloud_insights_integrations.CloudInsightsIntegrationsApi(api_client)
    aws_flow_logs_integration_request = thousandeyes_sdk.cloud_insights_integrations.AwsFlowLogsIntegrationRequest() # AwsFlowLogsIntegrationRequest | 
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Create AWS flow logs monitoring integration
        api_response = api_instance.create_aws_flow_logs_monitoring_integration(aws_flow_logs_integration_request, aid=aid)
        print("The response of CloudInsightsIntegrationsApi->create_aws_flow_logs_monitoring_integration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudInsightsIntegrationsApi->create_aws_flow_logs_monitoring_integration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aws_flow_logs_integration_request** | [**AwsFlowLogsIntegrationRequest**](AwsFlowLogsIntegrationRequest.md)|  | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

[**AwsMonitoringIntegration**](AwsMonitoringIntegration.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json, application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | AWS flow logs monitoring integration created successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Insufficient permissions to query endpoint |  -  |
**404** | Not found |  -  |
**429** | Exhausted rate limit for the organization |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_aws_inventory_monitoring_integration**
> AwsMonitoringIntegration create_aws_inventory_monitoring_integration(aws_inventory_integration_request, aid=aid)

Create AWS inventory monitoring integration

Creates a new AWS inventory monitoring integration.

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.cloud_insights_integrations
from thousandeyes_sdk.cloud_insights_integrations.models.aws_inventory_integration_request import AwsInventoryIntegrationRequest
from thousandeyes_sdk.cloud_insights_integrations.models.aws_monitoring_integration import AwsMonitoringIntegration
from thousandeyes_sdk.cloud_insights_integrations.rest import ApiException
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
    api_instance = thousandeyes_sdk.cloud_insights_integrations.CloudInsightsIntegrationsApi(api_client)
    aws_inventory_integration_request = thousandeyes_sdk.cloud_insights_integrations.AwsInventoryIntegrationRequest() # AwsInventoryIntegrationRequest | 
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Create AWS inventory monitoring integration
        api_response = api_instance.create_aws_inventory_monitoring_integration(aws_inventory_integration_request, aid=aid)
        print("The response of CloudInsightsIntegrationsApi->create_aws_inventory_monitoring_integration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudInsightsIntegrationsApi->create_aws_inventory_monitoring_integration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aws_inventory_integration_request** | [**AwsInventoryIntegrationRequest**](AwsInventoryIntegrationRequest.md)|  | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

[**AwsMonitoringIntegration**](AwsMonitoringIntegration.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json, application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | AWS inventory monitoring integration created successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Insufficient permissions to query endpoint |  -  |
**404** | Not found |  -  |
**429** | Exhausted rate limit for the organization |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_azure_flow_logs_monitoring_integration**
> AzureMonitoringIntegration create_azure_flow_logs_monitoring_integration(azure_flow_logs_integration_request, aid=aid)

Create Azure flow logs monitoring integration

Creates a new Azure flow logs monitoring integration.

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.cloud_insights_integrations
from thousandeyes_sdk.cloud_insights_integrations.models.azure_flow_logs_integration_request import AzureFlowLogsIntegrationRequest
from thousandeyes_sdk.cloud_insights_integrations.models.azure_monitoring_integration import AzureMonitoringIntegration
from thousandeyes_sdk.cloud_insights_integrations.rest import ApiException
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
    api_instance = thousandeyes_sdk.cloud_insights_integrations.CloudInsightsIntegrationsApi(api_client)
    azure_flow_logs_integration_request = thousandeyes_sdk.cloud_insights_integrations.AzureFlowLogsIntegrationRequest() # AzureFlowLogsIntegrationRequest | 
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Create Azure flow logs monitoring integration
        api_response = api_instance.create_azure_flow_logs_monitoring_integration(azure_flow_logs_integration_request, aid=aid)
        print("The response of CloudInsightsIntegrationsApi->create_azure_flow_logs_monitoring_integration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudInsightsIntegrationsApi->create_azure_flow_logs_monitoring_integration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **azure_flow_logs_integration_request** | [**AzureFlowLogsIntegrationRequest**](AzureFlowLogsIntegrationRequest.md)|  | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

[**AzureMonitoringIntegration**](AzureMonitoringIntegration.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json, application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Azure flow logs monitoring integration created successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Insufficient permissions to query endpoint |  -  |
**404** | Not found |  -  |
**429** | Exhausted rate limit for the organization |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_azure_inventory_monitoring_integration**
> AzureMonitoringIntegration create_azure_inventory_monitoring_integration(azure_inventory_integration_request, aid=aid)

Create Azure inventory monitoring integration

Creates a new Azure inventory monitoring integration.

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.cloud_insights_integrations
from thousandeyes_sdk.cloud_insights_integrations.models.azure_inventory_integration_request import AzureInventoryIntegrationRequest
from thousandeyes_sdk.cloud_insights_integrations.models.azure_monitoring_integration import AzureMonitoringIntegration
from thousandeyes_sdk.cloud_insights_integrations.rest import ApiException
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
    api_instance = thousandeyes_sdk.cloud_insights_integrations.CloudInsightsIntegrationsApi(api_client)
    azure_inventory_integration_request = thousandeyes_sdk.cloud_insights_integrations.AzureInventoryIntegrationRequest() # AzureInventoryIntegrationRequest | 
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Create Azure inventory monitoring integration
        api_response = api_instance.create_azure_inventory_monitoring_integration(azure_inventory_integration_request, aid=aid)
        print("The response of CloudInsightsIntegrationsApi->create_azure_inventory_monitoring_integration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudInsightsIntegrationsApi->create_azure_inventory_monitoring_integration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **azure_inventory_integration_request** | [**AzureInventoryIntegrationRequest**](AzureInventoryIntegrationRequest.md)|  | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

[**AzureMonitoringIntegration**](AzureMonitoringIntegration.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json, application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Azure inventory monitoring integration created successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Insufficient permissions to query endpoint |  -  |
**404** | Not found |  -  |
**429** | Exhausted rate limit for the organization |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_aws_monitoring_integration**
> delete_aws_monitoring_integration(integration_id, aid=aid)

Delete AWS integration

Deletes a specific AWS inventory or flow logs monitoring integration using the AWS integration ID.

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.cloud_insights_integrations
from thousandeyes_sdk.cloud_insights_integrations.rest import ApiException
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
    api_instance = thousandeyes_sdk.cloud_insights_integrations.CloudInsightsIntegrationsApi(api_client)
    integration_id = 'e9c3bf02-a48c-4aa8-9e5f-898800d6f569' # str | The unique ID of the AWS or Azure inventory or flow logs monitoring integration.
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Delete AWS integration
        api_instance.delete_aws_monitoring_integration(integration_id, aid=aid)
    except Exception as e:
        print("Exception when calling CloudInsightsIntegrationsApi->delete_aws_monitoring_integration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_id** | **str**| The unique ID of the AWS or Azure inventory or flow logs monitoring integration. | 
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
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Insufficient permissions to query endpoint |  -  |
**404** | Not found |  -  |
**429** | Exhausted rate limit for the organization |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_azure_monitoring_integration**
> delete_azure_monitoring_integration(integration_id, aid=aid)

Delete Azure integration

Deletes a specific Azure inventory or flow logs monitoring integration using the Azure integration ID.

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.cloud_insights_integrations
from thousandeyes_sdk.cloud_insights_integrations.rest import ApiException
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
    api_instance = thousandeyes_sdk.cloud_insights_integrations.CloudInsightsIntegrationsApi(api_client)
    integration_id = 'e9c3bf02-a48c-4aa8-9e5f-898800d6f569' # str | The unique ID of the AWS or Azure inventory or flow logs monitoring integration.
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Delete Azure integration
        api_instance.delete_azure_monitoring_integration(integration_id, aid=aid)
    except Exception as e:
        print("Exception when calling CloudInsightsIntegrationsApi->delete_azure_monitoring_integration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_id** | **str**| The unique ID of the AWS or Azure inventory or flow logs monitoring integration. | 
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
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Insufficient permissions to query endpoint |  -  |
**404** | Not found |  -  |
**429** | Exhausted rate limit for the organization |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_aws_monitoring_integrations**
> AwsMonitoringIntegrations get_all_aws_monitoring_integrations(aid=aid)

List AWS integrations

Retrieves all AWS inventory and flow logs monitoring integrations configured for the authenticated account group in ThousandEyes.

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.cloud_insights_integrations
from thousandeyes_sdk.cloud_insights_integrations.models.aws_monitoring_integrations import AwsMonitoringIntegrations
from thousandeyes_sdk.cloud_insights_integrations.rest import ApiException
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
    api_instance = thousandeyes_sdk.cloud_insights_integrations.CloudInsightsIntegrationsApi(api_client)
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # List AWS integrations
        api_response = api_instance.get_all_aws_monitoring_integrations(aid=aid)
        print("The response of CloudInsightsIntegrationsApi->get_all_aws_monitoring_integrations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudInsightsIntegrationsApi->get_all_aws_monitoring_integrations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

[**AwsMonitoringIntegrations**](AwsMonitoringIntegrations.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json, application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response is an array of integration objects, where each object represents either an Inventory Monitoring or Flow Logs Monitoring integration. Each integration includes metadata such as: id — the unique identifier of the integration; name — the user-defined name of the integration; roleArn — the AWS IAM role ARN that ThousandEyes assumes to access your AWS resources; externalId — the external identifier used for secure cross-account role assumption; monitoringType — specifies whether the integration monitors AWS inventory (inventory-monitoring) or flow logs (flow-logs-monitoring); snsTopicsArns — a list of SNS topic ARNs used for flow logs monitoring (only present for flow logs monitoring integrations); links — HAL-style link relations that provide the \&quot;self\&quot; URL for retrieving integration details. This endpoint can be used to: audit all existing AWS integrations configured for Cloud Insights, identify which integrations are set up for inventory versus flow logs monitoring, and retrieve integration IDs for further API operations such as inspection (GET /cloud-insights/integration/aws/{integrationId}) or deletion (DELETE). The response is returned as a JSON array conforming to the AwsMonitoringIntegration schema.  |  -  |
**401** | Unauthorized |  -  |
**403** | Insufficient permissions to query endpoint |  -  |
**404** | Not found |  -  |
**429** | Exhausted rate limit for the organization |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_azure_monitoring_integrations**
> AzureMonitoringIntegrations get_all_azure_monitoring_integrations(aid=aid)

List Azure integrations

Retrieves all Azure inventory and flow logs monitoring integrations configured for the authenticated account group in ThousandEyes.

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.cloud_insights_integrations
from thousandeyes_sdk.cloud_insights_integrations.models.azure_monitoring_integrations import AzureMonitoringIntegrations
from thousandeyes_sdk.cloud_insights_integrations.rest import ApiException
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
    api_instance = thousandeyes_sdk.cloud_insights_integrations.CloudInsightsIntegrationsApi(api_client)
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # List Azure integrations
        api_response = api_instance.get_all_azure_monitoring_integrations(aid=aid)
        print("The response of CloudInsightsIntegrationsApi->get_all_azure_monitoring_integrations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudInsightsIntegrationsApi->get_all_azure_monitoring_integrations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

[**AzureMonitoringIntegrations**](AzureMonitoringIntegrations.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json, application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response is an array of integration objects, where each object represents either an Azure Inventory Monitoring or Azure Flow Logs Monitoring integration. Each integration includes metadata such as: id — the unique identifier of the integration; name — the user-defined name of the integration; appId / clientId — the Azure Application (client) ID of the service principal used for authentication; password / clientSecret — the client secret value associated with the service principal (note: for security reasons, the actual secret is never returned. The response includes a masked value (\&quot;********\&quot;) instead); azureTenantId — the Azure Active Directory tenant ID associated with the integration; serviceBusQueueUrl — the Service Bus queue URL used for flow logs monitoring (only present for azure-flow-logs-monitoring integrations); monitoringType — specifies whether the integration monitors Azure resources (azure-inventory-monitoring) or Azure flow logs (azure-flow-logs-monitoring); links — HAL-style link relations that provide the \&quot;self\&quot; URL for retrieving integration details. This endpoint can be used to: audit all existing Azure integrations configured for Cloud Insights, identify which integrations are configured for inventory versus flow logs monitoring, and retrieve integration IDs for further API operations such as inspection (GET /cloud-insights/integration/azure/{integrationId}) or deletion (DELETE). The response is returned as a JSON array conforming to the AwsMonitoringIntegration schema.  |  -  |
**401** | Unauthorized |  -  |
**403** | Insufficient permissions to query endpoint |  -  |
**404** | Not found |  -  |
**429** | Exhausted rate limit for the organization |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_aws_flowlogs_monitoring_integration_policies**
> str get_aws_flowlogs_monitoring_integration_policies(aid=aid)

Get AWS flow logs monitoring IAM policies

Retrieves the AWS IAM policies required to configure an AWS flow logs monitoring integration in JSON string format for the authenticated account group.

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.cloud_insights_integrations
from thousandeyes_sdk.cloud_insights_integrations.rest import ApiException
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
    api_instance = thousandeyes_sdk.cloud_insights_integrations.CloudInsightsIntegrationsApi(api_client)
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Get AWS flow logs monitoring IAM policies
        api_response = api_instance.get_aws_flowlogs_monitoring_integration_policies(aid=aid)
        print("The response of CloudInsightsIntegrationsApi->get_aws_flowlogs_monitoring_integration_policies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudInsightsIntegrationsApi->get_aws_flowlogs_monitoring_integration_policies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

**str**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response contains a JSON object with the following policy documents under the policies key: 1) Trusted Policy — defines the trust relationship that allows ThousandEyes to assume a specified AWS IAM role via sts:AssumeRole. This includes the Principal ARN for ThousandEyes and the required ExternalId condition for secure cross-account access; 2) Permissions Policy — grants ThousandEyes read-only access to the Amazon S3 buckets where flow logs are stored. The policy includes permissions such as s3:GetObject and s3:ListBucket, scoped to the relevant flow log S3 bucket ARNs; 3) SNS Topic Access Policy — allows ThousandEyes to subscribe to Amazon SNS topics that receive flow log delivery notifications. It also enables the S3 service to publish events to those topics, ensuring ThousandEyes can be notified of new log data. This policy includes permissions for both SNS:Subscribe (for ThousandEyes) and SNS:Publish (for S3 event notifications). Use these policies when configuring the IAM role and SNS topic permissions required by ThousandEyes Cloud Insights to collect and monitor AWS flow logs data across your account. The response is returned as a JSON string in the policies object.  |  -  |
**401** | Unauthorized |  -  |
**403** | Insufficient permissions to query endpoint |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_aws_inventory_monitoring_integration_policies**
> str get_aws_inventory_monitoring_integration_policies(aid=aid)

Get AWS inventory monitoring IAM policies

Retrieves the AWS IAM policies required to configure an AWS inventory monitoring integration in JSON string format for the authenticated account group.

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.cloud_insights_integrations
from thousandeyes_sdk.cloud_insights_integrations.rest import ApiException
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
    api_instance = thousandeyes_sdk.cloud_insights_integrations.CloudInsightsIntegrationsApi(api_client)
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Get AWS inventory monitoring IAM policies
        api_response = api_instance.get_aws_inventory_monitoring_integration_policies(aid=aid)
        print("The response of CloudInsightsIntegrationsApi->get_aws_inventory_monitoring_integration_policies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudInsightsIntegrationsApi->get_aws_inventory_monitoring_integration_policies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

**str**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response includes a JSON object containing two key policy documents: 1) Trusted Policy — defines the trust relationship that allows ThousandEyes to assume a specified AWS IAM role through sts:AssumeRole. This policy includes the Principal ARN for ThousandEyes and the required ExternalId condition; 2) Permissions Policy — lists the AWS service-level read permissions needed by ThousandEyes Cloud Insights to inventory network resources. These permissions cover services such as EC2, VPC, Transit Gateway, Direct Connect, CloudFront, ELB, CloudTrail, ECS/EKS, and S3. Use these policies when creating or updating the IAM role that ThousandEyes will use for inventory monitoring. The response is returned as a JSON string in the policies object.  |  -  |
**401** | Unauthorized |  -  |
**403** | Insufficient permissions to query endpoint |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_aws_monitoring_integration**
> AwsMonitoringIntegration get_aws_monitoring_integration(integration_id, aid=aid)

Get AWS integration

Retrieves details for a specific AWS inventory or flow logs monitoring integration associated with the authenticated account group using the unique integration ID.

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.cloud_insights_integrations
from thousandeyes_sdk.cloud_insights_integrations.models.aws_monitoring_integration import AwsMonitoringIntegration
from thousandeyes_sdk.cloud_insights_integrations.rest import ApiException
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
    api_instance = thousandeyes_sdk.cloud_insights_integrations.CloudInsightsIntegrationsApi(api_client)
    integration_id = 'e9c3bf02-a48c-4aa8-9e5f-898800d6f569' # str | The unique ID of the AWS or Azure inventory or flow logs monitoring integration.
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Get AWS integration
        api_response = api_instance.get_aws_monitoring_integration(integration_id, aid=aid)
        print("The response of CloudInsightsIntegrationsApi->get_aws_monitoring_integration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudInsightsIntegrationsApi->get_aws_monitoring_integration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_id** | **str**| The unique ID of the AWS or Azure inventory or flow logs monitoring integration. | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

[**AwsMonitoringIntegration**](AwsMonitoringIntegration.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json, application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response contains a single integration object representing either: AWS inventory monitoring integration or AWS flow logs monitoring integration. Each integration includes metadata that defines its configuration: id — the unique identifier of the integration; name — the user-defined name of the integration; roleArn — the AWS IAM role ARN that ThousandEyes assumes to access your AWS resources; externalId — the external identifier used for secure cross-account role assumption; monitoringType — identifies whether the integration monitors AWS inventory (inventory-monitoring) or flow logs (flow-logs-monitoring); snsTopicsArns — a list of SNS topic ARNs associated with flow logs monitoring (only present for flow-logs-monitoring integrations); links — HAL-style link relations that include a self URL pointing to this integration resource. This endpoint is typically used to: retrieve detailed configuration information for a specific AWS integration, verify that the integration is correctly set up and associated with the expected AWS IAM role, and obtain integration details before performing deletion or troubleshooting operations.  |  -  |
**401** | Unauthorized |  -  |
**403** | Insufficient permissions to query endpoint |  -  |
**404** | Not found |  -  |
**429** | Exhausted rate limit for the organization |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_azure_monitoring_integration**
> AzureMonitoringIntegration get_azure_monitoring_integration(integration_id, aid=aid)

Get Azure integration

Retrieves details for a specific Azure inventory or flow logs monitoring integration associated with the authenticated account group using the unique integration ID.

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.cloud_insights_integrations
from thousandeyes_sdk.cloud_insights_integrations.models.azure_monitoring_integration import AzureMonitoringIntegration
from thousandeyes_sdk.cloud_insights_integrations.rest import ApiException
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
    api_instance = thousandeyes_sdk.cloud_insights_integrations.CloudInsightsIntegrationsApi(api_client)
    integration_id = 'e9c3bf02-a48c-4aa8-9e5f-898800d6f569' # str | The unique ID of the AWS or Azure inventory or flow logs monitoring integration.
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Get Azure integration
        api_response = api_instance.get_azure_monitoring_integration(integration_id, aid=aid)
        print("The response of CloudInsightsIntegrationsApi->get_azure_monitoring_integration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudInsightsIntegrationsApi->get_azure_monitoring_integration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_id** | **str**| The unique ID of the AWS or Azure inventory or flow logs monitoring integration. | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

[**AzureMonitoringIntegration**](AzureMonitoringIntegration.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json, application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response contains a single integration object representing either: Azure Inventory Monitoring integration or Azure Flow Logs Monitoring integration. Each integration includes metadata that defines its configuration: id — the unique identifier of the integration; name — the user-defined name of the integration; appId / clientId — the Azure Application (client) ID of the service principal used for authentication; password / clientSecret — the client secret value associated with the service principal (note: for security reasons, the actual secret is never returned. The response includes a masked value (\&quot;********\&quot;) instead; azureTenantId — the Azure Active Directory tenant ID for the integration; serviceBusQueueUrl — the Service Bus queue URL used for receiving Flow Logs (only present for azure-flow-logs-monitoring integrations); monitoringType — identifies whether the integration monitors Azure resources (azure-inventory-monitoring) or flow logs (azure-flow-logs-monitoring); links — HAL-style link relations that include a \&quot;self\&quot; URL pointing to this integration resource. This endpoint is typically used to: retrieve detailed configuration information for a specific Azure integration, validate that the integration credentials and type (inventory or flow logs) are correctly configured, and obtain integration details before performing update or deletion operations.  |  -  |
**401** | Unauthorized |  -  |
**403** | Insufficient permissions to query endpoint |  -  |
**404** | Not found |  -  |
**429** | Exhausted rate limit for the organization |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_azure_flow_logs_monitoring_integration**
> AzureMonitoringIntegration update_azure_flow_logs_monitoring_integration(integration_id, azure_flow_logs_integration_request, aid=aid)

Update Azure flow logs monitoring integration

Updates an existing Azure flow logs monitoring integration.

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.cloud_insights_integrations
from thousandeyes_sdk.cloud_insights_integrations.models.azure_flow_logs_integration_request import AzureFlowLogsIntegrationRequest
from thousandeyes_sdk.cloud_insights_integrations.models.azure_monitoring_integration import AzureMonitoringIntegration
from thousandeyes_sdk.cloud_insights_integrations.rest import ApiException
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
    api_instance = thousandeyes_sdk.cloud_insights_integrations.CloudInsightsIntegrationsApi(api_client)
    integration_id = 'e9c3bf02-a48c-4aa8-9e5f-898800d6f569' # str | The unique ID of the AWS or Azure inventory or flow logs monitoring integration.
    azure_flow_logs_integration_request = thousandeyes_sdk.cloud_insights_integrations.AzureFlowLogsIntegrationRequest() # AzureFlowLogsIntegrationRequest | 
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Update Azure flow logs monitoring integration
        api_response = api_instance.update_azure_flow_logs_monitoring_integration(integration_id, azure_flow_logs_integration_request, aid=aid)
        print("The response of CloudInsightsIntegrationsApi->update_azure_flow_logs_monitoring_integration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudInsightsIntegrationsApi->update_azure_flow_logs_monitoring_integration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_id** | **str**| The unique ID of the AWS or Azure inventory or flow logs monitoring integration. | 
 **azure_flow_logs_integration_request** | [**AzureFlowLogsIntegrationRequest**](AzureFlowLogsIntegrationRequest.md)|  | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

[**AzureMonitoringIntegration**](AzureMonitoringIntegration.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json, application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Azure flow logs monitoring integration updated successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Insufficient permissions to query endpoint |  -  |
**404** | Not found |  -  |
**429** | Exhausted rate limit for the organization |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_azure_inventory_monitoring_integration**
> AzureMonitoringIntegration update_azure_inventory_monitoring_integration(integration_id, azure_inventory_integration_request, aid=aid)

Update Azure inventory monitoring integration

Updates an existing Azure inventory monitoring integration.

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.cloud_insights_integrations
from thousandeyes_sdk.cloud_insights_integrations.models.azure_inventory_integration_request import AzureInventoryIntegrationRequest
from thousandeyes_sdk.cloud_insights_integrations.models.azure_monitoring_integration import AzureMonitoringIntegration
from thousandeyes_sdk.cloud_insights_integrations.rest import ApiException
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
    api_instance = thousandeyes_sdk.cloud_insights_integrations.CloudInsightsIntegrationsApi(api_client)
    integration_id = 'e9c3bf02-a48c-4aa8-9e5f-898800d6f569' # str | The unique ID of the AWS or Azure inventory or flow logs monitoring integration.
    azure_inventory_integration_request = thousandeyes_sdk.cloud_insights_integrations.AzureInventoryIntegrationRequest() # AzureInventoryIntegrationRequest | 
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Update Azure inventory monitoring integration
        api_response = api_instance.update_azure_inventory_monitoring_integration(integration_id, azure_inventory_integration_request, aid=aid)
        print("The response of CloudInsightsIntegrationsApi->update_azure_inventory_monitoring_integration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudInsightsIntegrationsApi->update_azure_inventory_monitoring_integration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_id** | **str**| The unique ID of the AWS or Azure inventory or flow logs monitoring integration. | 
 **azure_inventory_integration_request** | [**AzureInventoryIntegrationRequest**](AzureInventoryIntegrationRequest.md)|  | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

[**AzureMonitoringIntegration**](AzureMonitoringIntegration.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json, application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Azure inventory monitoring integration updated successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Insufficient permissions to query endpoint |  -  |
**404** | Not found |  -  |
**429** | Exhausted rate limit for the organization |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

