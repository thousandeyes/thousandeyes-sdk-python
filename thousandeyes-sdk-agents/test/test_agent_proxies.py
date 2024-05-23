# coding: utf-8

"""
    Agents API

     ## Overview Manage all agents available to your account in ThousandEyes, including both Cloud and Enterprise Agents.

    The version of the OpenAPI document: 7.0.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from thousandeyes_sdk.agents.models.agent_proxies import AgentProxies

class TestAgentProxies(unittest.TestCase):
    """AgentProxies unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AgentProxies:
        """Test AgentProxies
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AgentProxies`
        """
        model = AgentProxies()
        if include_optional:
            return AgentProxies(
                agent_proxies = [
                    thousandeyes_sdk.agents.models.agent_proxy.AgentProxy(
                        aid = '1234', 
                        auth_type = 'basic', 
                        bypass_list = ["10.0.0.0/16","*.thousandeyes.com"], 
                        last_modified = '2022-07-17T22:00:54Z', 
                        location = 'proxy.thousandeyes.com:3128', 
                        is_local_configured = True, 
                        name = 'Test Proxy - Auth Type - BASIC', 
                        password = '****', 
                        proxy_id = '281474976710706', 
                        type = 'static', 
                        user = 'user1', )
                    ],
                links = thousandeyes_sdk.agents.models.self_links.SelfLinks(
                    self = thousandeyes_sdk.agents.models.link.Link(
                        href = 'https://api.thousandeyes.com/v7/link/to/resource/id', 
                        templated = True, 
                        type = '', 
                        deprecation = '', 
                        name = '', 
                        profile = '', 
                        title = '', 
                        hreflang = '', ), )
            )
        else:
            return AgentProxies(
        )
        """

    def testAgentProxies(self):
        """Test AgentProxies"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
