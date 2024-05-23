# coding: utf-8

"""
    Administrative API

    ## Overview Manage users, accounts, and account groups in the ThousandEyes platform using the Administrative API. This API provides the following endpoints that define the operations to manage your organization:     * `/account-groups`: Account groups are used to divide an organization into different sections. These endpoints can be used to create, retrieve, update and delete account groups.   * `/users`: Create, retrieve, update and delete users within an organization.    * `/roles`: Create, retrieve and update roles for the current user.    * `/permissions`: Retrieve all assignable permissions. Used in the context of modifying roles.    * `/audit-user-events`: Retrieve all activity log events.    For more information about the administrative models, see [Account Management](https://docs.thousandeyes.com/product-documentation/user-management).

    The version of the OpenAPI document: 7.0.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from thousandeyes_sdk.admin.models.role_detail import RoleDetail

class TestRoleDetail(unittest.TestCase):
    """RoleDetail unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RoleDetail:
        """Test RoleDetail
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RoleDetail`
        """
        model = RoleDetail()
        if include_optional:
            return RoleDetail(
                name = 'Organization Admin',
                role_id = '35',
                is_builtin = True,
                permissions = [{"label":"View reports","permissionId":1,"isManagementPermission":true,"permission":"REPORT_READ"},{"label":"View snapshots","permissionId":51,"isManagementPermission":false,"permission":"REPORT_SNAPSHOTS_READ"}],
                links = thousandeyes_sdk.admin.models.self_links.SelfLinks(
                    self = thousandeyes_sdk.admin.models.link.Link(
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
            return RoleDetail(
        )
        """

    def testRoleDetail(self):
        """Test RoleDetail"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
