# coding: utf-8

"""
    Agents API

     ## Overview Manage all agents available to your account in ThousandEyes, including both Cloud and Enterprise Agents.

    The version of the OpenAPI document: 7.0.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from thousandeyes_sdk.agents.models.agent import Agent

class TestAgent(unittest.TestCase):
    """Agent unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Agent:
        """Test Agent
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Agent`
        """
        model = Agent()
        if include_optional:
            return Agent(
                ip_addresses = ["99.139.65.220","9bbd:8a0a:a257:5876:288b:6cb2:3f36:64ce"],
                public_ip_addresses = ["192.168.1.78","f9b2:3a21:f25c:d300:03f4:586d:f8d6:4e1c"],
                network = 'AT&T Services, Inc. (AS 7018)',
                agent_id = '281474976710706',
                agent_name = 'thousandeyes-stg-va-254',
                location = 'San Francisco Bay Area',
                country_id = 'US',
                enabled = True,
                prefix = '99.128.0.0/11',
                verify_ssl_certificates = True,
                agent_type = 'enterprise-cluster'
            )
        else:
            return Agent(
                agent_type = 'enterprise-cluster',
        )
        """

    def testAgent(self):
        """Test Agent"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()