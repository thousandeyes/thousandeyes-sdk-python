# coding: utf-8

"""
    Administrative API

    ## Overview Manage users, accounts, and account groups in the ThousandEyes platform using the Administrative API. This API provides the following endpoints that define the operations to manage your organization:     * `/account-groups`: Account groups are used to divide an organization into different sections. These endpoints can be used to create, retrieve, update and delete account groups.   * `/users`: Create, retrieve, update and delete users within an organization.    * `/roles`: Create, retrieve and update roles for the current user.    * `/permissions`: Retrieve all assignable permissions. Used in the context of modifying roles.    * `/audit-user-events`: Retrieve all activity log events.    For more information about the administrative models, see [Account Management](https://docs.thousandeyes.com/product-documentation/user-management).

    The version of the OpenAPI document: 7.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from thousandeyes_sdk.admin.models.agent_base import AgentBase

class TestAgentBase(unittest.TestCase):
    """AgentBase unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AgentBase:
        """Test AgentBase
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AgentBase`
        """
        model = AgentBase()
        if include_optional:
            return AgentBase(
                ip_addresses = ["99.139.65.220","9bbd:8a0a:a257:5876:288b:6cb2:3f36:64ce"],
                public_ip_addresses = ["192.168.1.78","f9b2:3a21:f25c:d300:03f4:586d:f8d6:4e1c"],
                network = 'AT&T Services, Inc. (AS 7018)'
            )
        else:
            return AgentBase(
        )
        """

    def testAgentBase(self):
        """Test AgentBase"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
