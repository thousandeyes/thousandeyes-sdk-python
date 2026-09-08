# thousandeyes_sdk.cloud_insights_integrations.CloudInsightsIntegrationPolicySettingsApi

All URIs are relative to *https://api.thousandeyes.com/v7*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_aws_integration_policy_settings**](CloudInsightsIntegrationPolicySettingsApi.md#get_aws_integration_policy_settings) | **GET** /cloud-insights/integration/aws/policy/settings | Get AWS integration policy settings
[**get_azure_integration_policy_settings**](CloudInsightsIntegrationPolicySettingsApi.md#get_azure_integration_policy_settings) | **GET** /cloud-insights/integration/azure/policy/settings | Get Azure integration policy settings
[**update_aws_integration_policy_settings**](CloudInsightsIntegrationPolicySettingsApi.md#update_aws_integration_policy_settings) | **PUT** /cloud-insights/integration/aws/policy/settings | Update AWS integration policy settings
[**update_azure_integration_policy_settings**](CloudInsightsIntegrationPolicySettingsApi.md#update_azure_integration_policy_settings) | **PUT** /cloud-insights/integration/azure/policy/settings | Update Azure integration policy settings


# **get_aws_integration_policy_settings**
> AwsIntegrationPolicySetting get_aws_integration_policy_settings(aid=aid)

Get AWS integration policy settings

Retrieves the AWS integration policy settings for the authenticated account group. Use this endpoint to audit which AWS resource group types and AWS regions are enabled, and whether CloudTrail is enabled, for Cloud Insights inventory monitoring. 

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.cloud_insights_integrations
from thousandeyes_sdk.cloud_insights_integrations.models.aws_integration_policy_setting import AwsIntegrationPolicySetting
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
    api_instance = thousandeyes_sdk.cloud_insights_integrations.CloudInsightsIntegrationPolicySettingsApi(api_client)
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Get AWS integration policy settings
        api_response = api_instance.get_aws_integration_policy_settings(aid=aid)
        print("The response of CloudInsightsIntegrationPolicySettingsApi->get_aws_integration_policy_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudInsightsIntegrationPolicySettingsApi->get_aws_integration_policy_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

[**AwsIntegrationPolicySetting**](AwsIntegrationPolicySetting.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json, application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | AWS integration policy settings returned successfully. |  -  |
**401** | Unauthorized |  -  |
**403** | Insufficient permissions to query endpoint |  -  |
**404** | Not found |  -  |
**429** | Exhausted rate limit for the organization |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_azure_integration_policy_settings**
> AzureIntegrationPolicySetting get_azure_integration_policy_settings(aid=aid)

Get Azure integration policy settings

Retrieves the Azure integration policy settings for the authenticated account group. Use this endpoint to review which Azure resource group types are monitored and inspect the subscriptions policy rules that gate which subscriptions ThousandEyes inventories. 

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.cloud_insights_integrations
from thousandeyes_sdk.cloud_insights_integrations.models.azure_integration_policy_setting import AzureIntegrationPolicySetting
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
    api_instance = thousandeyes_sdk.cloud_insights_integrations.CloudInsightsIntegrationPolicySettingsApi(api_client)
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Get Azure integration policy settings
        api_response = api_instance.get_azure_integration_policy_settings(aid=aid)
        print("The response of CloudInsightsIntegrationPolicySettingsApi->get_azure_integration_policy_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudInsightsIntegrationPolicySettingsApi->get_azure_integration_policy_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

[**AzureIntegrationPolicySetting**](AzureIntegrationPolicySetting.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json, application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Azure integration policy settings returned successfully. |  -  |
**401** | Unauthorized |  -  |
**403** | Insufficient permissions to query endpoint |  -  |
**404** | Not found |  -  |
**429** | Exhausted rate limit for the organization |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_aws_integration_policy_settings**
> AwsIntegrationPolicySetting update_aws_integration_policy_settings(aws_integration_policy_setting, aid=aid)

Update AWS integration policy settings

Updates the AWS integration policy settings for the authenticated account group. This endpoint lets you enable or disable specific AWS resource group types, adjust the set of AWS regions to inventory, and control whether CloudTrail is enabled for inventory monitoring. 

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.cloud_insights_integrations
from thousandeyes_sdk.cloud_insights_integrations.models.aws_integration_policy_setting import AwsIntegrationPolicySetting
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
    api_instance = thousandeyes_sdk.cloud_insights_integrations.CloudInsightsIntegrationPolicySettingsApi(api_client)
    aws_integration_policy_setting = thousandeyes_sdk.cloud_insights_integrations.AwsIntegrationPolicySetting() # AwsIntegrationPolicySetting | 
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Update AWS integration policy settings
        api_response = api_instance.update_aws_integration_policy_settings(aws_integration_policy_setting, aid=aid)
        print("The response of CloudInsightsIntegrationPolicySettingsApi->update_aws_integration_policy_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudInsightsIntegrationPolicySettingsApi->update_aws_integration_policy_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aws_integration_policy_setting** | [**AwsIntegrationPolicySetting**](AwsIntegrationPolicySetting.md)|  | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

[**AwsIntegrationPolicySetting**](AwsIntegrationPolicySetting.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json, application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | AWS integration policy settings updated successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Insufficient permissions to query endpoint |  -  |
**404** | Not found |  -  |
**429** | Exhausted rate limit for the organization |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_azure_integration_policy_settings**
> AzureIntegrationPolicySetting update_azure_integration_policy_settings(azure_integration_policy_setting, aid=aid)

Update Azure integration policy settings

Updates the Azure integration policy settings for the authenticated account group. This endpoint lets you enable or disable Azure resource group types and manage the subscriptions policy (rules plus default action) that controls which Azure subscriptions are inventoried. 

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.cloud_insights_integrations
from thousandeyes_sdk.cloud_insights_integrations.models.azure_integration_policy_setting import AzureIntegrationPolicySetting
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
    api_instance = thousandeyes_sdk.cloud_insights_integrations.CloudInsightsIntegrationPolicySettingsApi(api_client)
    azure_integration_policy_setting = thousandeyes_sdk.cloud_insights_integrations.AzureIntegrationPolicySetting() # AzureIntegrationPolicySetting | 
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Update Azure integration policy settings
        api_response = api_instance.update_azure_integration_policy_settings(azure_integration_policy_setting, aid=aid)
        print("The response of CloudInsightsIntegrationPolicySettingsApi->update_azure_integration_policy_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudInsightsIntegrationPolicySettingsApi->update_azure_integration_policy_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **azure_integration_policy_setting** | [**AzureIntegrationPolicySetting**](AzureIntegrationPolicySetting.md)|  | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

[**AzureIntegrationPolicySetting**](AzureIntegrationPolicySetting.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json, application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Azure integration policy settings updated successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Insufficient permissions to query endpoint |  -  |
**404** | Not found |  -  |
**429** | Exhausted rate limit for the organization |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

