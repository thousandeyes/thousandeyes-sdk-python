# coding: utf-8

"""
    Endpoint Agents API

    Manage ThousandEyes Endpoint Agents using this API.   For more information about Endpoint Agents, see [Endpoint Agents](https://docs.thousandeyes.com/product-documentation/global-vantage-points/endpoint-agents).

    The version of the OpenAPI document: 7.0.11
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import unittest
import thousandeyes_sdk.endpoint_agents.models

from .test_utils import assert_constructed_model_matches_example_json
from thousandeyes_sdk.endpoint_agents.api.transfer_api import TransferApi


class TestTransferApi(unittest.TestCase):
    """TransferApi unit test stubs"""

    def setUp(self) -> None:
        self.api = TransferApi()

    def tearDown(self) -> None:
        pass

    def test_transfer_endpoint_agent_models_validation(self) -> None:
        """Test case for transfer_endpoint_agent request and response models"""
        request_body_json = """
                {
                  "toAid" : "1234"
                }"""

        request_loaded_json = json.loads(request_body_json)
        request_from_json = thousandeyes_sdk.endpoint_agents.models.AgentTransferRequest.from_json(request_body_json)
        assert_constructed_model_matches_example_json(request_from_json, request_loaded_json)


    def test_transfer_endpoint_agents_models_validation(self) -> None:
        """Test case for transfer_endpoint_agents request and response models"""
        request_body_json = """
                {
                  "transfers" : [ {
                    "agentId" : "5d0764ac-7e42-4ec8-a0d4-39fc53edccba",
                    "fromAid" : "1234",
                    "toAid" : "12345"
                  }, {
                    "agentId" : "5d0764ac-7e42-4ec8-a0d4-39fc53edccba",
                    "fromAid" : "1234",
                    "toAid" : "12345"
                  } ]
                }"""

        request_loaded_json = json.loads(request_body_json)
        request_from_json = thousandeyes_sdk.endpoint_agents.models.BulkAgentTransferRequest.from_json(request_body_json)
        assert_constructed_model_matches_example_json(request_from_json, request_loaded_json)

        response_body_json = """
                {
                  "items" : [ {
                    "status" : 200,
                    "detail" : "Initiated",
                    "request" : {
                      "agentId" : "5d0764ac-7e42-4ec8-a0d4-39fc53edccba",
                      "fromAid" : "1234",
                      "toAid" : "12345"
                    }
                  }, {
                    "status" : 400,
                    "detail" : "Missing from-account id",
                    "request" : {
                      "agentId" : "5d0764ac-7e42-4ec8-a0d5-39fc53ed1234",
                      "fromAid" : "xxx",
                      "toAid" : "12345"
                    }
                  }, {
                    "status" : 403,
                    "detail" : "User does not have permission on 'to' aid",
                    "request" : {
                      "agentId" : "5d0764ac-7e42-4ec8-a0d5-39fc53ed7890",
                      "fromAid" : "1234",
                      "toAid" : "12345"
                    }
                  } ]
                }"""

        response_loaded_json = json.loads(response_body_json)
        response_from_json = thousandeyes_sdk.endpoint_agents.models.BulkAgentTransferResponse.from_json(response_body_json)
        assert_constructed_model_matches_example_json(response_from_json, response_loaded_json)


if __name__ == '__main__':
    unittest.main()
