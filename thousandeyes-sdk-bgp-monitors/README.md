# thousandeyes-sdk-bgp-monitors

Retrieve information about BGP monitors available to your ThousandEyes account. ThousandEyes ingests BGP routing data from dozens of global BGP collectors and automatically integrates that visibility as a configurable layer under service, network, and path visualization layers.

When you specify a service URL in a test, layered BGP tests automatically track reachability and path changes for any relevant prefix. When you use an IP address as the target for a test, the ThousandEyes platform monitors the relevant internet-routed prefix. You can also create specific BGP monitoring for a prefix, and can alert on hijacks and leaks.

For more information about monitors, see [Inside-Out BGP Visibility](https://docs.thousandeyes.com/product-documentation/internet-and-wan-monitoring/tests/bgp-tests/inside-out-bgp-visibility).


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
pip install thousandeyes-sdk-bgp-monitors
```
(you may need to run `pip` with root permission: `sudo pip install thousandeyes-sdk-bgp-monitors`)

Then import the package:
```python
import thousandeyes_sdk.bgp_monitors
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import thousandeyes_sdk.bgp_monitors
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the installation procedure and then run the following:

```python

import thousandeyes_sdk.core
import thousandeyes_sdk.bgp_monitors
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
    api_instance = thousandeyes_sdk.bgp_monitors.BGPMonitorsApi(api_client)
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # List BGP monitors
        api_response = api_instance.get_bgp_monitors(aid=aid)
        print("The response of BGPMonitorsApi->get_bgp_monitors:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BGPMonitorsApi->get_bgp_monitors: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.thousandeyes.com/v7*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*BGPMonitorsApi* | [**get_bgp_monitors**](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-bgp-monitors/docs/BGPMonitorsApi.md#get_bgp_monitors) | **GET** /monitors | List BGP monitors


## Documentation For Models

 - [Error](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-bgp-monitors/docs/Error.md)
 - [Link](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-bgp-monitors/docs/Link.md)
 - [Monitor](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-bgp-monitors/docs/Monitor.md)
 - [MonitorType](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-bgp-monitors/docs/MonitorType.md)
 - [Monitors](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-bgp-monitors/docs/Monitors.md)
 - [SelfLinks](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-bgp-monitors/docs/SelfLinks.md)
 - [UnauthorizedError](https://github.com/thousandeyes/thousandeyes-sdk-python//tree/main/thousandeyes-sdk-bgp-monitors/docs/UnauthorizedError.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="BearerAuth"></a>
### BearerAuth

- **Type**: Bearer authentication


## Author

<a href="mailto:api-team@thousandeyes.com">ThousandEyes API Team </a>


