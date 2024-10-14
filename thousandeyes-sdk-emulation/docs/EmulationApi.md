# thousandeyes_sdk.emulation.EmulationApi

All URIs are relative to *https://api.thousandeyes.com/v7*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_emulated_device**](EmulationApi.md#create_emulated_device) | **POST** /emulated-devices | Create emulated device
[**get_emulated_devices**](EmulationApi.md#get_emulated_devices) | **GET** /emulated-devices | List emulated devices
[**get_user_agents**](EmulationApi.md#get_user_agents) | **GET** /user-agents | List user-agents


# **create_emulated_device**
> EmulatedDeviceResponse create_emulated_device(emulated_device, aid=aid)

Create emulated device

Creates a new device for emulation.

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.emulation
from thousandeyes_sdk.emulation.models.emulated_device import EmulatedDevice
from thousandeyes_sdk.emulation.models.emulated_device_response import EmulatedDeviceResponse
from thousandeyes_sdk.emulation.rest import ApiException
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
    api_instance = thousandeyes_sdk.emulation.EmulationApi(api_client)
    emulated_device = thousandeyes_sdk.emulation.EmulatedDevice() # EmulatedDevice | 
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Create emulated device
        api_response = api_instance.create_emulated_device(emulated_device, aid=aid)
        print("The response of EmulationApi->create_emulated_device:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmulationApi->create_emulated_device: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **emulated_device** | [**EmulatedDevice**](EmulatedDevice.md)|  | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

[**EmulatedDeviceResponse**](EmulatedDeviceResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json, application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**401** | Unauthorized |  -  |
**403** | Insufficient permissions to query endpoint |  -  |
**404** | Not found |  -  |
**429** | Exhausted rate limit for the organization |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_emulated_devices**
> EmulatedDeviceResponses get_emulated_devices(expand=expand)

List emulated devices

Retrieves a list of emulated devices available for browser tests.

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.emulation
from thousandeyes_sdk.emulation.models.emulated_device_responses import EmulatedDeviceResponses
from thousandeyes_sdk.emulation.models.expand_emulated_device_options import ExpandEmulatedDeviceOptions
from thousandeyes_sdk.emulation.rest import ApiException
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
    api_instance = thousandeyes_sdk.emulation.EmulationApi(api_client)
    expand = [thousandeyes_sdk.emulation.ExpandEmulatedDeviceOptions()] # List[ExpandEmulatedDeviceOptions] | Optional query parameter that controls whether user-agent templates are included in the response. By default, user-agent templates are not included. To include them, add `?expand=user-agent` to the request.  (optional)

    try:
        # List emulated devices
        api_response = api_instance.get_emulated_devices(expand=expand)
        print("The response of EmulationApi->get_emulated_devices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmulationApi->get_emulated_devices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **expand** | [**List[ExpandEmulatedDeviceOptions]**](ExpandEmulatedDeviceOptions.md)| Optional query parameter that controls whether user-agent templates are included in the response. By default, user-agent templates are not included. To include them, add &#x60;?expand&#x3D;user-agent&#x60; to the request.  | [optional] 

### Return type

[**EmulatedDeviceResponses**](EmulatedDeviceResponses.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_agents**
> UserAgents get_user_agents(aid=aid)

List user-agents

Retrieves a list of user-agent strings.

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.emulation
from thousandeyes_sdk.emulation.models.user_agents import UserAgents
from thousandeyes_sdk.emulation.rest import ApiException
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
    api_instance = thousandeyes_sdk.emulation.EmulationApi(api_client)
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # List user-agents
        api_response = api_instance.get_user_agents(aid=aid)
        print("The response of EmulationApi->get_user_agents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmulationApi->get_user_agents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

[**UserAgents**](UserAgents.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

