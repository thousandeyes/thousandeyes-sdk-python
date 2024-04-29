# coding: utf-8

"""
    Administrative API

    ## Overview Manage users, accounts, and account groups in the ThousandEyes platform using the Administrative API. This API provides the following endpoints that define the operations to manage your organization:     * `/account-groups`: Account groups are used to divide an organization into different sections. These endpoints can be used to create, retrieve, update and delete account groups.   * `/users`: Create, retrieve, update and delete users within an organization.    * `/roles`: Create, retrieve and update roles for the current user.    * `/permissions`: Retrieve all assignable permissions. Used in the context of modifying roles.    * `/audit-user-events`: Retrieve all activity log events.    For more information about the administrative models, see [Account Management](https://docs.thousandeyes.com/product-documentation/user-management).

    The version of the OpenAPI document: 7.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from admin.models.create_user201_response import CreateUser201Response

class TestCreateUser201Response(unittest.TestCase):
    """CreateUser201Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateUser201Response:
        """Test CreateUser201Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateUser201Response`
        """
        model = CreateUser201Response()
        if include_optional:
            return CreateUser201Response(
                name = 'User X',
                email = 'userx@thousandeyes.com',
                uid = '245',
                date_registered = '2020-07-17T22:00:54Z',
                login_account_group = admin.models.account_group_1.AccountGroup_1(),
                account_group_roles = [
                    admin.models.account_group_roles_account_group_roles_inner.AccountGroupRoles_accountGroupRoles_inner(
                        account_group = admin.models.account_group_1.AccountGroup_1(), 
                        roles = [
                            admin.models.role.Role()
                            ], )
                    ],
                all_account_group_roles = [
                    admin.models.role.Role()
                    ],
                links = admin.models.self_links__links.SelfLinks__links(
                    self = admin.models.link.Link(
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
            return CreateUser201Response(
        )
        """

    def testCreateUser201Response(self):
        """Test CreateUser201Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()