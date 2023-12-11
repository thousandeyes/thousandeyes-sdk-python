# test_templates_api.TestTemplateEndpointsApi

All URIs are relative to *https://api.thousandeyes.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_test_template**](TestTemplateEndpointsApi.md#create_test_template) | **POST** /v7/tests/templates | Create a test template.
[**delete_test_template**](TestTemplateEndpointsApi.md#delete_test_template) | **DELETE** /v7/tests/templates/{id} | Delete a test template
[**deploy_user_template**](TestTemplateEndpointsApi.md#deploy_user_template) | **POST** /v7/tests/templates/{id}/deploy | Deploy a test template.
[**get_user_org_test_template**](TestTemplateEndpointsApi.md#get_user_org_test_template) | **GET** /v7/tests/templates/{id} | Retrieve a test template
[**get_user_org_test_templates**](TestTemplateEndpointsApi.md#get_user_org_test_templates) | **GET** /v7/tests/templates | List all test templates.
[**update_test_template**](TestTemplateEndpointsApi.md#update_test_template) | **PUT** /v7/tests/templates/{id} | Update a test template


# **create_test_template**
> TestTemplate create_test_template(test_template_upsert, aid=aid)

Create a test template.

Creates a test template.

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import test_templates_api
from test_templates_api.models.test_template import TestTemplate
from test_templates_api.models.test_template_upsert import TestTemplateUpsert
from test_templates_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.thousandeyes.com
# See configuration.py for a list of all supported configuration parameters.
configuration = test_templates_api.Configuration(
    host = "https://api.thousandeyes.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = test_templates_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with test_templates_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = test_templates_api.TestTemplateEndpointsApi(api_client)
    test_template_upsert = test_templates_api.TestTemplateUpsert() # TestTemplateUpsert | The test template to create or update.
    aid = '2067' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Create a test template.
        api_response = api_instance.create_test_template(test_template_upsert, aid=aid)
        print("The response of TestTemplateEndpointsApi->create_test_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestTemplateEndpointsApi->create_test_template: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_template_upsert** | [**TestTemplateUpsert**](TestTemplateUpsert.md)| The test template to create or update. | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

[**TestTemplate**](TestTemplate.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  * Location -  <br>  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_test_template**
> delete_test_template(id, aid=aid)

Delete a test template

Deletes a test template using its ID.

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import test_templates_api
from test_templates_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.thousandeyes.com
# See configuration.py for a list of all supported configuration parameters.
configuration = test_templates_api.Configuration(
    host = "https://api.thousandeyes.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = test_templates_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with test_templates_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = test_templates_api.TestTemplateEndpointsApi(api_client)
    id = 'fcbb89a7-61cf-4616-9c4f-828fa3cb4684' # str | The ID of the test template
    aid = '2067' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Delete a test template
        api_instance.delete_test_template(id, aid=aid)
    except Exception as e:
        print("Exception when calling TestTemplateEndpointsApi->delete_test_template: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the test template | 
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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deploy_user_template**
> deploy_user_template(id, deploy_test_template, aid=aid)

Deploy a test template.

Deploys a test template to create tests, alert rules, and dashboards defined by the template. You can deploy templates to easily create new tests.   To deploy test templates, you must specify `userInputValues` required by the template in the request body. `userInputValues` enables you to specify a minimum set of user values required to configure the tests from a test template. This way, you do not have to edit all the details of each test configuration. If necessary, you can edit the test details directly in the template.   ### Considerations  Consider the following when deploying a test template:  * To deploy a test template, you must first create the template or use one of ThousandEyes' predefined test templates.  * The deployment strategy allows you to specify what should happen to a particular asset in the event that a test template is redeployed.    When you attempt to deploy a test template that has already been deployed, the API service compares any assets that have not yet been deployed with the assets that were deployed in the previous deployment (the comparison is done using the **asset key**; the asset keys are simply the object keys used in the `tests`, `labels`, `alertRules`, and `dashboards` fields). By default, if the configuration of a particular asset has not changed from the previous deployment, that asset is ignored.       If a change is detected:    * If the asset is a test, a new test is created with the new configuration.   * If the asset is not a test, the asset is updated.  * You can create new resources such as tests, alert rules, labels, dashboards, and modify existing resources defined in test templates, overwriting the default configurations.  * You can also use existing resources (such as those created outside the test template deployment flow) by adding their ID either in the raw test template or using the overrides when deploying the template. See example usage below for the raw test template sample.  **Note**: The test template API does not currently track \"live\" configuration of assets. Any changes made to assets outside of the test template API will not be considered when comparing changes during the redeployment scenario.  ### Example usage:  ```POST /v7/tests/templates/fcbb89a7-61cf-4616-9c4f-828fa3cb4684/deploy  {   \"userInputValues\": {     \"interval\": 120,     \"target\": \"https://microsoft.com\",     \"agents\": [{\"agentId\":11}],     \"domain\": \"microsoft.com\"   },   \"name\":\"Microsoft Suite\",   \"tests\": {     \"secondPageLoadTest\": {       \"httpInterval\": 120,       \"interval\": 120,       \"testId\": 182481,       \"type\": \"page-load\",       \"url\": \"https://microsoft.com\",       \"testName\": \"Microsoft Suite - Second Page Load\",       \"agents\": [         {           \"agentId\": 11         }       ]     }   } } ``` #### Raw Test Template Sample  ``` {   ...   \"tests\": {       \"existingTest\": {           \"testId\": \"123\", //The API will only try to update this test; will never create it           \"type\": \"http-server\",           ....       },       ...   },   ... } ```

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import test_templates_api
from test_templates_api.models.deploy_test_template import DeployTestTemplate
from test_templates_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.thousandeyes.com
# See configuration.py for a list of all supported configuration parameters.
configuration = test_templates_api.Configuration(
    host = "https://api.thousandeyes.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = test_templates_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with test_templates_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = test_templates_api.TestTemplateEndpointsApi(api_client)
    id = 'fcbb89a7-61cf-4616-9c4f-828fa3cb4684' # str | The ID of the test template
    deploy_test_template = test_templates_api.DeployTestTemplate() # DeployTestTemplate | Deploy test template
    aid = '2067' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Deploy a test template.
        api_instance.deploy_user_template(id, deploy_test_template, aid=aid)
    except Exception as e:
        print("Exception when calling TestTemplateEndpointsApi->deploy_user_template: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the test template | 
 **deploy_test_template** | [**DeployTestTemplate**](DeployTestTemplate.md)| Deploy test template | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_org_test_template**
> TestTemplate get_user_org_test_template(id, aid=aid)

Retrieve a test template

Retrieves a test template using its ID.

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import test_templates_api
from test_templates_api.models.test_template import TestTemplate
from test_templates_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.thousandeyes.com
# See configuration.py for a list of all supported configuration parameters.
configuration = test_templates_api.Configuration(
    host = "https://api.thousandeyes.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = test_templates_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with test_templates_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = test_templates_api.TestTemplateEndpointsApi(api_client)
    id = 'fcbb89a7-61cf-4616-9c4f-828fa3cb4684' # str | The ID of the test template
    aid = '2067' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Retrieve a test template
        api_response = api_instance.get_user_org_test_template(id, aid=aid)
        print("The response of TestTemplateEndpointsApi->get_user_org_test_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestTemplateEndpointsApi->get_user_org_test_template: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the test template | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

[**TestTemplate**](TestTemplate.md)

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_org_test_templates**
> TestTemplateCollection get_user_org_test_templates(aid=aid)

List all test templates.

Retrieves a list of all your test templates

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import test_templates_api
from test_templates_api.models.test_template_collection import TestTemplateCollection
from test_templates_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.thousandeyes.com
# See configuration.py for a list of all supported configuration parameters.
configuration = test_templates_api.Configuration(
    host = "https://api.thousandeyes.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = test_templates_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with test_templates_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = test_templates_api.TestTemplateEndpointsApi(api_client)
    aid = '2067' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # List all test templates.
        api_response = api_instance.get_user_org_test_templates(aid=aid)
        print("The response of TestTemplateEndpointsApi->get_user_org_test_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestTemplateEndpointsApi->get_user_org_test_templates: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

[**TestTemplateCollection**](TestTemplateCollection.md)

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_test_template**
> TestTemplate update_test_template(id, test_template_upsert, aid=aid)

Update a test template

Updates an existing test template. This operation overwrites the existing test template object with the object sent in the request. If a partial update is required, it is recommended that you retrieve the test template and modify the test template object before updating it.

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import test_templates_api
from test_templates_api.models.test_template import TestTemplate
from test_templates_api.models.test_template_upsert import TestTemplateUpsert
from test_templates_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.thousandeyes.com
# See configuration.py for a list of all supported configuration parameters.
configuration = test_templates_api.Configuration(
    host = "https://api.thousandeyes.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = test_templates_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with test_templates_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = test_templates_api.TestTemplateEndpointsApi(api_client)
    id = 'fcbb89a7-61cf-4616-9c4f-828fa3cb4684' # str | The ID of the test template
    test_template_upsert = test_templates_api.TestTemplateUpsert() # TestTemplateUpsert | The test template to create or update.
    aid = '2067' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Update a test template
        api_response = api_instance.update_test_template(id, test_template_upsert, aid=aid)
        print("The response of TestTemplateEndpointsApi->update_test_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestTemplateEndpointsApi->update_test_template: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the test template | 
 **test_template_upsert** | [**TestTemplateUpsert**](TestTemplateUpsert.md)| The test template to create or update. | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

[**TestTemplate**](TestTemplate.md)

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

