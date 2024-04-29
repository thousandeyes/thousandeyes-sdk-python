# coding: utf-8

"""
    Endpoint Agents API

    Manage ThousandEyes Endpoint Agents using this API.   For more information about Endpoint Agents, see [Endpoint Agents](https://docs.thousandeyes.com/product-documentation/global-vantage-points/endpoint-agents).

    The version of the OpenAPI document: 7.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from endpoint_agents.models.endpoint_agent_bulk_transfer207_response import EndpointAgentBulkTransfer207Response

class TestEndpointAgentBulkTransfer207Response(unittest.TestCase):
    """EndpointAgentBulkTransfer207Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EndpointAgentBulkTransfer207Response:
        """Test EndpointAgentBulkTransfer207Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EndpointAgentBulkTransfer207Response`
        """
        model = EndpointAgentBulkTransfer207Response()
        if include_optional:
            return EndpointAgentBulkTransfer207Response(
                items = [{"status":200,"detail":"Initiated","request":{"agentId":"5d0764ac-7e42-4ec8-a0d4-39fc53edccba","fromAid":"1234","toAid":"12345"}},{"status":400,"detail":"Missing from-account id","request":{"agentId":"5d0764ac-7e42-4ec8-a0d5-39fc53ed1234","fromAid":"xxx","toAid":"12345"}},{"status":403,"detail":"User does not have permission on 'to' aid","request":{"agentId":"5d0764ac-7e42-4ec8-a0d5-39fc53ed7890","fromAid":"1234","toAid":"12345"}}]
            )
        else:
            return EndpointAgentBulkTransfer207Response(
        )
        """

    def testEndpointAgentBulkTransfer207Response(self):
        """Test EndpointAgentBulkTransfer207Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()