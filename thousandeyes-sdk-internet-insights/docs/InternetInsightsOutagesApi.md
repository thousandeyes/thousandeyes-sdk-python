# thousandeyes_sdk.internet_insights.InternetInsightsOutagesApi

All URIs are relative to *https://api.thousandeyes.com/v7*

Method | HTTP request | Description
------------- | ------------- | -------------
[**filter_outages**](InternetInsightsOutagesApi.md#filter_outages) | **POST** /internet-insights/outages/filter | List network and application outages
[**get_app_outage**](InternetInsightsOutagesApi.md#get_app_outage) | **GET** /internet-insights/outages/app/{outageId} | Retrieve application outage
[**get_network_outage**](InternetInsightsOutagesApi.md#get_network_outage) | **GET** /internet-insights/outages/net/{outageId} | Retrieve network outage


# **filter_outages**
> ApiOutagesResponse filter_outages(api_outage_filter, aid=aid)

List network and application outages

Returns a list of network and application outages using a filter object. Advanced Filter persistance is not currently supported.  <b>Note:</b> Support for pagination will be added in the future.   ## Samples Queries with Different Filter Permutations   ### Window  ```  curl --location --request POST 'https://api.thousandeyes.com/v7/internet-insights/outages/filter' --header 'Authorization: Bearer $token --header 'Accept-Encoding: application/gzip' --header 'Content-Type: application/json' --data-raw '{   \"window\" : \"1d\"   }' ```  ### Date Range ``` curl --location --request POST 'https://api.thousandeyes.com/v7/internet-insights/outages/filter' --header 'Authorization: Bearer $token' --header 'Content-Type: application/json' --data-raw '{     \"startDate\": \"2022-03-01T01:30:00Z\",     \"endDate\"  : \"2022-03-01T23:30:15Z\"   }' ```  ### Date Range with Scope ``` curl --location --request POST 'https://api.thousandeyes.com/v7/internet-insights/outages/filter' --header 'Authorization: Bearer $token' --header 'Content-Type: application/json' --data-raw '{     \"startDate\": \"2022-03-01T01:30:00Z\",     \"endDate\"  : \"2022-03-01T23:30:15Z\",     \"outageScope\": \"with-affected-test\"   }' ``` ### Date Range with Network ```   curl --location --request POST 'https://api.thousandeyes.com/v7/internet-insights/outages/filter'   --header 'Authorization: Bearer $token'   --header 'Content-Type: application/json'   --data-raw '{       \"startDate\": \"2022-03-01T01:30:00Z\",       \"endDate\"  : \"2022-03-01T23:30:15Z\",       \"interfaceNetwork\":  [\"Telianet\"]     }' ```  ### Date Range with Application ``` curl --location --request POST 'https://api.thousandeyes.com/v7/internet-insights/outages/filter'   --header 'Authorization: Bearer $token'   --header 'Content-Type: application/json'   --data-raw '{       \"startDate\": \"2022-03-01T01:30:00Z\",       \"endDate\"  : \"2022-03-01T23:30:15Z\",       \"applicationName\": [\"Google\"]   }' ``` ### Date Range with Provider ``` curl --location --request POST 'https://api.thousandeyes.com/v7/internet-insights/outages/filter' --header 'Authorization: Bearer $token' --header 'Content-Type: application/json' --data-raw '{       \"startDate\": \"2022-03-01T01:30:00Z\",       \"endDate\"  : \"2022-03-01T23:30:15Z\",       \"providerName\": [\"Century Link\", \"Microsoft\"]   }'  ``` ### Date Range with Application and Scope ``` curl --location --request POST 'https://api.thousandeyes.com/v7/internet-insights/outages/filter' --header 'Authorization: Bearer $token' --header 'Content-Type: application/json' --data-raw '{     \"startDate\": \"2022-03-01T01:30:00Z\",     \"endDate\"  : \"2022-03-01T23:30:15Z\",     \"outageScope\": \"all\",     \"applicationName\": [\"Google\"] }' ``` 

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.internet_insights
from thousandeyes_sdk.internet_insights.models.api_outage_filter import ApiOutageFilter
from thousandeyes_sdk.internet_insights.models.api_outages_response import ApiOutagesResponse
from thousandeyes_sdk.internet_insights.rest import ApiException
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
    api_instance = thousandeyes_sdk.internet_insights.InternetInsightsOutagesApi(api_client)
    api_outage_filter = thousandeyes_sdk.internet_insights.ApiOutageFilter() # ApiOutageFilter | 
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # List network and application outages
        api_response = api_instance.filter_outages(api_outage_filter, aid=aid)
        print("The response of InternetInsightsOutagesApi->filter_outages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InternetInsightsOutagesApi->filter_outages: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_outage_filter** | [**ApiOutageFilter**](ApiOutageFilter.md)|  | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

[**ApiOutagesResponse**](ApiOutagesResponse.md)

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

# **get_app_outage**
> ApiApplicationOutageDetails get_app_outage(outage_id, aid=aid)

Retrieve application outage

Returns the details of an application outage. 

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.internet_insights
from thousandeyes_sdk.internet_insights.models.api_application_outage_details import ApiApplicationOutageDetails
from thousandeyes_sdk.internet_insights.rest import ApiException
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
    api_instance = thousandeyes_sdk.internet_insights.InternetInsightsOutagesApi(api_client)
    outage_id = 'F73E24F17E4996923196826A208BB572508A8EB13BEE14B0' # str | 
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Retrieve application outage
        api_response = api_instance.get_app_outage(outage_id, aid=aid)
        print("The response of InternetInsightsOutagesApi->get_app_outage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InternetInsightsOutagesApi->get_app_outage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **outage_id** | **str**|  | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

[**ApiApplicationOutageDetails**](ApiApplicationOutageDetails.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **get_network_outage**
> ApiNetworkOutageDetails get_network_outage(outage_id, aid=aid)

Retrieve network outage

Returns the details of a network outage. 

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.internet_insights
from thousandeyes_sdk.internet_insights.models.api_network_outage_details import ApiNetworkOutageDetails
from thousandeyes_sdk.internet_insights.rest import ApiException
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
    api_instance = thousandeyes_sdk.internet_insights.InternetInsightsOutagesApi(api_client)
    outage_id = '694D8656960F34F76489BCE5E9BCD58EC53027462740D75F' # str | 
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Retrieve network outage
        api_response = api_instance.get_network_outage(outage_id, aid=aid)
        print("The response of InternetInsightsOutagesApi->get_network_outage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InternetInsightsOutagesApi->get_network_outage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **outage_id** | **str**|  | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

[**ApiNetworkOutageDetails**](ApiNetworkOutageDetails.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
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

