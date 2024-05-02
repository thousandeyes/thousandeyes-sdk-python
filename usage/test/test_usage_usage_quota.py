# coding: utf-8

"""
    Usage API

     These usage endpoints define the following operations:  * **Usage**: Retrieve usage data for the specified time period (default is one month).          * Users must have the `View Billing` permission to access this endpoint.     * This endpoint offers visibility across all account groups within the organization.     * Users with `View Billing` permission in multiple organizations should query the endpoint with the `aid` query string parameter (see optional parameters) for each organization.  * **Quotas**: Obtain organization and account usage quotas. Additionally, users with the appropriate permissions can create, update, or delete these quotas.          * Users must have the necessary permissions to perform quota-related actions.  Refer to the Usage API endpoints for detailed usage instructions and optional parameters. 

    The version of the OpenAPI document: 7.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from usage.models.usage_usage_quota import UsageUsageQuota

class TestUsageUsageQuota(unittest.TestCase):
    """UsageUsageQuota unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UsageUsageQuota:
        """Test UsageUsageQuota
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UsageUsageQuota`
        """
        model = UsageUsageQuota()
        if include_optional:
            return UsageUsageQuota(
                month_start = '2020-01-05T08:00Z',
                month_end = '2020-02-05T08:00Z',
                cloud_units_included = 4320000000,
                endpoint_agents_included = 200,
                endpoint_agents_essentials_included = 10,
                endpoint_agents_embedded_included = 10,
                enterprise_agents_included = 25
            )
        else:
            return UsageUsageQuota(
        )
        """

    def testUsageUsageQuota(self):
        """Test UsageUsageQuota"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
