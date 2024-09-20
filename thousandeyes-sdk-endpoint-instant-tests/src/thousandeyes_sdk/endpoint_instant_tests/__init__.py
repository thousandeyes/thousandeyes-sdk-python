# coding: utf-8

# flake8: noqa

"""
    Endpoint Instant Scheduled Tests API

     You can create and execute a new endpoint instant scheduled test within ThousandEyes using this API. The test parameters are specified in the `POST` data.  The following applies to the Endpoint Instant Scheduled Tests API:  * To initiate the creation and execution of an instant scheduled test, the user must possess the `Edit endpoint tests` permission.  * Upon successful creation of an instant scheduled test, the API responds with an HTTP/201 CREATED status code and return the test definition. * It's important to note that the response does not include the results of the instant scheduled test. To retrieve test results, users can utilize the Endpoint Test Data endpoints. The URLs for these API test data endpoints are provided within the test definition output when an instant scheduled test is created. 

    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


# import apis into sdk package
from thousandeyes_sdk.endpoint_instant_tests.api.agent_to_server_endpoint_instant_scheduled_tests_api import AgentToServerEndpointInstantScheduledTestsApi
from thousandeyes_sdk.endpoint_instant_tests.api.http_server_endpoint_instant_scheduled_tests_api import HTTPServerEndpointInstantScheduledTestsApi
from thousandeyes_sdk.endpoint_instant_tests.api.run_endpoint_instant_scheduled_tests_api import RunEndpointInstantScheduledTestsApi


# import models into sdk package
from thousandeyes_sdk.endpoint_instant_tests.models.endpoint_agent_labels_selector_config import EndpointAgentLabelsSelectorConfig
from thousandeyes_sdk.endpoint_instant_tests.models.endpoint_agent_selector_config import EndpointAgentSelectorConfig
from thousandeyes_sdk.endpoint_instant_tests.models.endpoint_agent_to_server_instant_test import EndpointAgentToServerInstantTest
from thousandeyes_sdk.endpoint_instant_tests.models.endpoint_agent_to_server_test import EndpointAgentToServerTest
from thousandeyes_sdk.endpoint_instant_tests.models.endpoint_all_agents_selector_config import EndpointAllAgentsSelectorConfig
from thousandeyes_sdk.endpoint_instant_tests.models.endpoint_http_server_base_test import EndpointHttpServerBaseTest
from thousandeyes_sdk.endpoint_instant_tests.models.endpoint_http_server_instant_test import EndpointHttpServerInstantTest
from thousandeyes_sdk.endpoint_instant_tests.models.endpoint_http_server_test import EndpointHttpServerTest
from thousandeyes_sdk.endpoint_instant_tests.models.endpoint_instant_test import EndpointInstantTest
from thousandeyes_sdk.endpoint_instant_tests.models.endpoint_run_scheduled_instant_test_result import EndpointRunScheduledInstantTestResult
from thousandeyes_sdk.endpoint_instant_tests.models.endpoint_scheduled_test_type import EndpointScheduledTestType
from thousandeyes_sdk.endpoint_instant_tests.models.endpoint_specific_agents_selector_config import EndpointSpecificAgentsSelectorConfig
from thousandeyes_sdk.endpoint_instant_tests.models.endpoint_test import EndpointTest
from thousandeyes_sdk.endpoint_instant_tests.models.endpoint_test_agent_selector_type import EndpointTestAgentSelectorType
from thousandeyes_sdk.endpoint_instant_tests.models.endpoint_test_auth_type import EndpointTestAuthType
from thousandeyes_sdk.endpoint_instant_tests.models.endpoint_test_links import EndpointTestLinks
from thousandeyes_sdk.endpoint_instant_tests.models.endpoint_test_protocol import EndpointTestProtocol
from thousandeyes_sdk.endpoint_instant_tests.models.endpoint_test_self_link import EndpointTestSelfLink
from thousandeyes_sdk.endpoint_instant_tests.models.error import Error
from thousandeyes_sdk.endpoint_instant_tests.models.link import Link
from thousandeyes_sdk.endpoint_instant_tests.models.test_interval import TestInterval
from thousandeyes_sdk.endpoint_instant_tests.models.test_label import TestLabel
from thousandeyes_sdk.endpoint_instant_tests.models.test_probe_mode_response import TestProbeModeResponse
from thousandeyes_sdk.endpoint_instant_tests.models.test_ssl_version_id import TestSslVersionId
from thousandeyes_sdk.endpoint_instant_tests.models.unauthorized_error import UnauthorizedError
from thousandeyes_sdk.endpoint_instant_tests.models.validation_error import ValidationError
from thousandeyes_sdk.endpoint_instant_tests.models.validation_error_item import ValidationErrorItem
