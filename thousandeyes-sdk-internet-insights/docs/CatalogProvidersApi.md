# thousandeyes_sdk.internet_insights.CatalogProvidersApi

All URIs are relative to *https://api.thousandeyes.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**catalog_provider_list**](CatalogProvidersApi.md#catalog_provider_list) | **POST** /v7/internet-insights/catalog/providers/filter | List catalog providers
[**get_catalog_provider**](CatalogProvidersApi.md#get_catalog_provider) | **GET** /v7/internet-insights/catalog/providers/{providerId} | Retrieve a catalog provider


# **catalog_provider_list**
> ApiCatalogProviderResponse catalog_provider_list(api_catalog_provider_filter, aid=aid)

List catalog providers

Returns a list of catalog providers using the specified filters. Returns high-level information about each catalog provider. For more details about a specific provider, call the Get a catalog provider endpoint.  <b>Note:</b> Support for pagination will be added in the future. 

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.internet_insights
from thousandeyes_sdk.internet_insights.models.api_catalog_provider_filter import ApiCatalogProviderFilter
from thousandeyes_sdk.internet_insights.models.api_catalog_provider_response import ApiCatalogProviderResponse
from thousandeyes_sdk.internet_insights.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.thousandeyes.com
# See configuration.py for a list of all supported configuration parameters.
configuration = thousandeyes_sdk.client.Configuration(
    host = "https://api.thousandeyes.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = thousandeyes_sdk.client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with thousandeyes_sdk.internet_insights.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = thousandeyes_sdk.internet_insights.CatalogProvidersApi(api_client)
    api_catalog_provider_filter = thousandeyes_sdk.internet_insights.ApiCatalogProviderFilter() # ApiCatalogProviderFilter | 
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # List catalog providers
        api_response = api_instance.catalog_provider_list(api_catalog_provider_filter, aid=aid)
        print("The response of CatalogProvidersApi->catalog_provider_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CatalogProvidersApi->catalog_provider_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_catalog_provider_filter** | [**ApiCatalogProviderFilter**](ApiCatalogProviderFilter.md)|  | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

[**ApiCatalogProviderResponse**](ApiCatalogProviderResponse.md)

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
**404** | Not found |  -  |
**429** | Exhausted rate limit for the organization |  -  |
**500** | Internal server error |  -  |
**502** | Bad Gateway |  -  |
**0** | An error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_catalog_provider**
> ApiCatalogProviderDetails get_catalog_provider(provider_id, aid=aid)

Retrieve a catalog provider

Returns the details of a catalog provider. 

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.internet_insights
from thousandeyes_sdk.internet_insights.models.api_catalog_provider_details import ApiCatalogProviderDetails
from thousandeyes_sdk.internet_insights.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.thousandeyes.com
# See configuration.py for a list of all supported configuration parameters.
configuration = thousandeyes_sdk.client.Configuration(
    host = "https://api.thousandeyes.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = thousandeyes_sdk.client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with thousandeyes_sdk.internet_insights.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = thousandeyes_sdk.internet_insights.CatalogProvidersApi(api_client)
    provider_id = '85602a0a-54a7-4e97-946e-67492ef1fa26' # str | 
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Retrieve a catalog provider
        api_response = api_instance.get_catalog_provider(provider_id, aid=aid)
        print("The response of CatalogProvidersApi->get_catalog_provider:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CatalogProvidersApi->get_catalog_provider: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **str**|  | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

[**ApiCatalogProviderDetails**](ApiCatalogProviderDetails.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json, application/problem+json

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

