# coding: utf-8

"""
    Instant Tests API

    The Instant Tests API endpoint lets you create and run new instant tests. You will need to be a regular user or have the following permissions:   * `API Access`   * `View tests`  The response does not include the immediate test results. Use the Test Results endpoints to get test results after creating and executing an instant test. You can find the URLs for these endpoints in the _links section of the test definition that is returned when you create the instant test. 

    The version of the OpenAPI document: 7.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from instant_tests.models.cloud_enterprise_agent_type import CloudEnterpriseAgentType

class TestCloudEnterpriseAgentType(unittest.TestCase):
    """CloudEnterpriseAgentType unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCloudEnterpriseAgentType(self):
        """Test CloudEnterpriseAgentType"""
        # inst = CloudEnterpriseAgentType()

if __name__ == '__main__':
    unittest.main()
