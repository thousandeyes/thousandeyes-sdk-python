# coding: utf-8

"""
    Agents API

     ## Overview Manage all agents available to your account in ThousandEyes, including both Cloud and Enterprise Agents.

    The version of the OpenAPI document: 7.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from agents.models.cloud_enterprise_agents import CloudEnterpriseAgents

class TestCloudEnterpriseAgents(unittest.TestCase):
    """CloudEnterpriseAgents unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CloudEnterpriseAgents:
        """Test CloudEnterpriseAgents
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CloudEnterpriseAgents`
        """
        model = CloudEnterpriseAgents()
        if include_optional:
            return CloudEnterpriseAgents(
                agents = [
                    null
                    ]
            )
        else:
            return CloudEnterpriseAgents(
        )
        """

    def testCloudEnterpriseAgents(self):
        """Test CloudEnterpriseAgents"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
