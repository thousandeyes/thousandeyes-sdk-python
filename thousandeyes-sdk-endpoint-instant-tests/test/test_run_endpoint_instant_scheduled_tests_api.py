# coding: utf-8

"""
    Endpoint Instant Scheduled Tests API

     You can create and execute a new endpoint instant scheduled test within ThousandEyes using this API. The test parameters are specified in the `POST` data.  The following applies to the Endpoint Instant Scheduled Tests API:  * To initiate the creation and execution of an instant scheduled test, the user must possess the `Edit endpoint tests` permission.  * Upon successful creation of an instant scheduled test, the API responds with an HTTP/201 CREATED status code and return the test definition. * It's important to note that the response does not include the results of the instant scheduled test. To retrieve test results, users can utilize the Endpoint Test Data endpoints. The URLs for these API test data endpoints are provided within the test definition output when an instant scheduled test is created. 

    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import unittest
import thousandeyes_sdk.endpoint_instant_tests.models

from .test_utils import assert_constructed_model_matches_example_json
from thousandeyes_sdk.endpoint_instant_tests.api.run_endpoint_instant_scheduled_tests_api import RunEndpointInstantScheduledTestsApi


class TestRunEndpointInstantScheduledTestsApi(unittest.TestCase):
    """RunEndpointInstantScheduledTestsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = RunEndpointInstantScheduledTestsApi()

    def tearDown(self) -> None:
        pass

    def test_run_endpoint_scheduled_instant_test_models_validation(self) -> None:
        """Test case for run_endpoint_scheduled_instant_test request and response models"""

        response_body_json = """
                {
                  "message" : "Successfully reran the instant scheduled test with testId=765231567"
                }"""

        response_loaded_json = json.loads(response_body_json)
        response_from_json = thousandeyes_sdk.endpoint_instant_tests.models.EndpointRunScheduledInstantTestResult.from_json(response_body_json)
        assert_constructed_model_matches_example_json(response_from_json, response_loaded_json)


if __name__ == '__main__':
    unittest.main()
